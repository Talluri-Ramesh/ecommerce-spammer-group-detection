import pandas as pd
import numpy as np

INPUT = "data/cleaned_reviews.csv"
OUTPUT = "results/user_features.csv"

print("🔍 Loading cleaned reviews...")
df = pd.read_csv(INPUT)

# ---------- TIMESTAMP FIX ----------
print("⏱ Normalizing timestamp column...")

df["timestamp"] = pd.to_datetime(
    df["timestamp"],
    errors="coerce"
)

# Drop rows where timestamp conversion failed
df = df.dropna(subset=["timestamp"])

# Convert datetime to seconds
df["timestamp"] = df["timestamp"].astype("int64") // 10**9

# ---------- SORTING ----------
print("⏱ Sorting by user & time...")
df = df.sort_values(["user_id", "timestamp"])

# ---------- TEMPORAL FEATURES ----------
print("🧠 Computing time gaps...")
df["time_gap"] = df.groupby("user_id")["timestamp"].diff()
df["time_gap"] = df["time_gap"].fillna(0)

# ---------- BEHAVIORAL FEATURES ----------
print("📊 Computing behavioral features...")

user_features = df.groupby("user_id").agg(
    review_count=("review_text", "count"),
    avg_rating=("rating", "mean"),
    rating_std=("rating", "std"),
    avg_time_gap=("time_gap", "mean"),
    helpfulness_ratio=("helpful_num", lambda x: x.sum() / (df.loc[x.index, "helpful_den"].sum() + 1))
).reset_index()

user_features["rating_std"] = user_features["rating_std"].fillna(0)

print("💾 Saving user features...")
user_features.to_csv(OUTPUT, index=False)

print("✅ STEP 10 COMPLETE")
print("Users:", len(user_features))

