import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

print("🔍 Loading ML-ready dataset...")
df = pd.read_csv("results/ml_ready_dataset.csv")

print("📄 Columns in dataset:")
print(df.columns.tolist())

# -----------------------------
# Feature / Label split
# -----------------------------
X = df.drop(columns=["user_id", "label", "label_binary", "sps_score"])
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
# Random Forest Model
# -----------------------------
print("🌲 Training Random Forest (class balanced)...")
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=None,
    class_weight="balanced",
    random_state=42,
    n_jobs=-1
)

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

print("✅ STEP 16-D COMPLETE")

import joblib

joblib.dump(model, "models/spam_rf_model.pkl")
print("💾 Model saved to models/spam_rf_model.pkl")
