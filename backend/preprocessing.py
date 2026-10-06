import pandas as pd
import re

RAW_DATA = "data/Reviews.csv"
CLEAN_DATA = "data/cleaned_reviews.csv"

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-z\s]", "", text)
    return text.strip()

def preprocess():
    print("🔍 Loading dataset...")
    df = pd.read_csv(RAW_DATA)

    print("📛 Renaming columns...")
    df.rename(columns={
        "Id": "id",
        "ProductId": "product_id",
        "UserId": "user_id",
        "ProfileName": "profile_name",
        "HelpfulnessNumerator": "helpful_num",
        "HelpfulnessDenominator": "helpful_den",
        "Score": "rating",
        "Time": "timestamp",
        "Summary": "summary",
        "Text": "review_text"
    }, inplace=True)

    print("🧹 Removing missing values...")
    df.dropna(subset=["user_id", "product_id", "rating", "timestamp"], inplace=True)

    print("⏱ Converting timestamp...")
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")

    print("📝 Cleaning review text...")
    df["review_text"] = df["review_text"].apply(clean_text)

    print("🗑 Removing duplicates...")
    df.drop_duplicates(subset=["user_id", "product_id", "timestamp"], inplace=True)

    print("💾 Saving cleaned data...")
    df.to_csv(CLEAN_DATA, index=False)

    print("✅ Preprocessing completed")
    print("Records:", len(df))

if __name__ == "__main__":
    preprocess()
