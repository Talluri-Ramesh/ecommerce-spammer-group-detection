import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

print("🔍 Loading ML-ready dataset...")
df = pd.read_csv("results/ml_ready_dataset.csv")

print("📄 Columns in dataset:")
print(df.columns.tolist())

# -----------------------------
# Feature / Label split
# -----------------------------
X = df.drop(columns=["user_id", "label", "label_binary"])
y = df["label_binary"]

print("📊 Splitting dataset...")
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
    stratify=y
)

# -----------------------------
# Model Training
# -----------------------------
print("🤖 Training Logistic Regression...")
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# -----------------------------
# Evaluation
# -----------------------------
print("📈 Evaluating model...")
y_pred = model.predict(X_test)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("✅ STEP 16-C COMPLETE")
