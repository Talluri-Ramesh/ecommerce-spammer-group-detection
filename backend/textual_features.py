import pandas as pd
import re

INPUT = "data/cleaned_reviews.csv"
OUTPUT = "results/textual_features.csv"

print("🔍 Loading cleaned reviews...")
df = pd.read_csv(INPUT)

print("🧹 Normalizing text...")
df["review_text"] = df["review_text"].astype(str).str.lower()
df["review_text"] = df["review_text"].apply(
    lambda x: re.sub(r"[^a-z\s]", "", x)
)

print("📏 Computing review length...")
df["review_length"] = df["review_text"].apply(lambda x: len(x.split()))

print("🧠 Computing lexical diversity...")
df["unique_ratio"] = df["review_text"].apply(
    lambda x: len(set(x.split())) / max(len(x.split()), 1)
)

print("🔁 Detecting duplicate reviews...")
df["is_duplicate"] = df.duplicated(
    subset=["user_id", "review_text"], keep=False
)

print("📊 Aggregating textual features...")
textual_features = df.groupby("user_id").agg(
    avg_review_length=("review_length", "mean"),
    avg_unique_ratio=("unique_ratio", "mean"),
    duplicate_review_ratio=("is_duplicate", "mean"),
    repeated_reviews=("is_duplicate", "sum")
).reset_index()

print("💾 Saving textual features...")
textual_features.to_csv(OUTPUT, index=False)

print("✅ STEP 11 COMPLETE")
print("Users:", len(textual_features))
