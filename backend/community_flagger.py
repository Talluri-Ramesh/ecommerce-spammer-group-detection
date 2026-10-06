import json
from collections import defaultdict

COMMUNITY_FILE = "data/user_communities.json"
SPAM_LABEL_FILE = "data/user_spam_labels.json"
OUTPUT_FILE = "data/community_flags.json"

SPAM_THRESHOLD = 0.1  # 60% spam users → spam community


def flag_spam_communities():
    print(" Flagging spam communities...")

    with open(COMMUNITY_FILE, "r") as f:
        user_communities = json.load(f)

    with open(SPAM_LABEL_FILE, "r") as f:
        user_spam_labels = json.load(f)

    # Group users by community
    community_users = defaultdict(list)
    for user_id, community_id in user_communities.items():
        community_users[str(community_id)].append(user_id)

    community_flags = {}

    for community_id, users in community_users.items():
        spam_count = 0
        total_users = len(users)

        for user_id in users:
            if user_id in user_spam_labels:
                if user_spam_labels[user_id]["ml_prediction"] == 1:
                    spam_count += 1

        spam_ratio = spam_count / total_users if total_users > 0 else 0

        community_flags[f"community_{community_id}"] = {
            "total_users": total_users,
            "spam_users": spam_count,
            "spam_ratio": round(spam_ratio, 2),
            "is_spam_community": 1 if spam_ratio >= SPAM_THRESHOLD else 0
        }

    with open(OUTPUT_FILE, "w") as f:
        json.dump(community_flags, f, indent=4)

    print(f"✅ Community flags saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    flag_spam_communities()
