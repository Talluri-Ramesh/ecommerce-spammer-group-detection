import json
from ml_inference import predict_user

INPUT_FILE = "data/user_features.json"
OUTPUT_FILE = "data/user_spam_labels.json"


def generate_spam_labels():
    print("🧪 Generating user spam labels...")

    # Load user features
    with open(INPUT_FILE, "r") as f:
        user_data = json.load(f)

    spam_labels = {}

    for user_id, features in user_data.items():
        # Run ML prediction
        result = predict_user(features)

        spam_labels[user_id] = {
            "ml_prediction": int(result["prediction"]),
            "spam_probability": float(result["spam_probability"])
        }

    # Save output
    with open(OUTPUT_FILE, "w") as f:
        json.dump(spam_labels, f, indent=4)

    print(f"✅ Spam labels saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    generate_spam_labels()
