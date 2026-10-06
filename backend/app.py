from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Spammer Detection System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserInput(BaseModel):
    user_id: str
    review_count: int
    avg_rating: float
    rating_std: float
    avg_time_gap: float
    helpfulness_ratio: float
    avg_review_length: int
    avg_unique_ratio: float
    duplicate_review_ratio: float
    repeated_reviews: int


@app.post("/predict")
def predict(user: UserInput):
    # 🔹 Dummy logic (replace with model if needed)
    spam_score = (
        user.rating_std +
        user.duplicate_review_ratio +
        (1 - user.helpfulness_ratio)
    ) / 3

    is_spam = spam_score > 0.5

    return {
        "user_id": user.user_id,
        "spam_probability": round(spam_score, 2),
        "final_result": "SPAMMER" if is_spam else "NON-SPAMMER",
        "reason": "High spam behavior indicators" if is_spam else "Normal user behavior"
    }


@app.get("/spammer-groups")
def get_spammer_groups():
    import json
    import os

    FILE = "data/community_flags.json"

    if not os.path.exists(FILE):
        return {
            "total_groups": 0,
            "groups": []
        }

    with open(FILE, "r") as f:
        data = json.load(f)

    groups = []

    for community_id, info in data.items():
        groups.append({
            "community_id": community_id,
            "spam_ratio": round(info.get("spam_ratio", 0), 2),
            "status": "SPAMMER GROUP" if info.get("is_spam", False) else "NORMAL GROUP"
        })

    return {
        "total_groups": len(groups),
        "groups": groups
    }


