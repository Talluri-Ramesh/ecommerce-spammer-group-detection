import pandas as pd

print("🔍 Loading ML-ready dataset...")
df = pd.read_csv("results/ml_ready_dataset.csv")

print("📄 Columns:")
print(df.columns.tolist())

print("🧠 Separating features and labels...")

X = df.drop(columns=["user_id", "label", "label_binary"])
y = df["label_binary"]

print("📊 Feature matrix shape:", X.shape)
print("🏷️ Label vector shape:", y.shape)

print("📁 Saving separated datasets...")
X.to_csv("results/X_features.csv", index=False)
y.to_csv("results/y_labels.csv", index=False)

print("✅ STEP 16-B COMPLETE")

