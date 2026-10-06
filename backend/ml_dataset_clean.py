import pandas as pd

print("🔍 Loading final features...")
df = pd.read_csv("results/final_features_with_sps.csv")

print("📄 Columns found:")
print(df.columns.tolist())

print("🧠 Creating binary labels...")
df["label_binary"] = df["label"].map({
    "SUSPICIOUS": 1,
    "NORMAL": 0
})

print("🧹 Dropping rows with missing labels...")
before = len(df)
df = df.dropna(subset=["label_binary"])
after = len(df)

print(f"Removed {before - after} rows")

print("📁 Saving ML-ready dataset...")
df.to_csv("results/ml_ready_dataset.csv", index=False)

print("✅ STEP 16-A COMPLETE")
print(df["label_binary"].value_counts())
