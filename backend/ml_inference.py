import joblib
import pandas as pd

MODEL_PATH = "models/spam_rf_model.pkl"

FEATURE_COLUMNS = [
    "review_count",
    "avg_rating",
    "rating_std",
    "avg_time_gap",
    "helpfulness_ratio",
    "avg_review_length",
    "avg_unique_ratio",
    "duplicate_review_ratio",
    "repeated_reviews"
]

print("🔄 Loading trained model...")
model = joblib.load(MODEL_PATH)
print("✅ Model loaded")

def predict_user(user_features: dict):
    """
    user_features: dict containing ONLY the feature columns
    """
    df = pd.DataFrame([user_features])

    # Ensure correct feature order
    df = df[FEATURE_COLUMNS]

    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

    return {
        "prediction": int(prediction),
        "spam_probability": round(probability, 4)
    }


# -----------------------------
# Sample Test
# -----------------------------
if __name__ == "__main__":
    sample_user = {
        "review_count": 120,
        "avg_rating": 4.8,
        "rating_std": 0.1,
        "avg_time_gap": 2.5,
        "helpfulness_ratio": 0.02,
        "avg_review_length": 20,
        "avg_unique_ratio": 0.4,
        "duplicate_review_ratio": 0.85,
        "repeated_reviews": 15
    }

    result = predict_user(sample_user)
    print("\n🧪 Prediction Result:")
    print(result)
