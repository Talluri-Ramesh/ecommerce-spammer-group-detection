import json

COMMUNITY_FILE = "data/user_communities.json"
COMMUNITY_FLAGS_FILE = "data/community_flags.json"
SPAM_LABEL_FILE = "data/user_spam_labels.json"
OUTPUT_FILE = "data/user_community_risk.json"


def assign_community_risk():
    print("⚠️ Assigning community risk to users...")

    with open(COMMUNITY_FILE, "r") as f:
        user_communities = json.load(f)

    with open(COMMUNITY_FLAGS_FILE, "r") as f:
        community_flags = json.load(f)

    with open(SPAM_LABEL_FILE, "r") as f:
        user_spam_labels = json.load(f)

    user_risk = {}

    for user_id, community_id in user_communities.items():
        community_key = f"community_{community_id}"

        community_info = community_flags.get(community_key, {})

        user_risk[user_id] = {
            "community_id": community_id,
            "community_flag": community_info.get("is_spam_community", 0),
            "community_spam_ratio": community_info.get("spam_ratio", 0.0),
            "ml_prediction": user_spam_labels.get(user_id, {}).get("ml_prediction", 0)
        }

    with open(OUTPUT_FILE, "w") as f:
        json.dump(user_risk, f, indent=4)

    print(f"✅ User community risk saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    assign_community_risk()
