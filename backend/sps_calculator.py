def calculate_sps(features: dict) -> float:
    score = 0.0

    if features["duplicate_review_ratio"] > 0.5:
        score += 0.3

    if features["repeated_reviews"] > 10:
        score += 0.2

    if features["avg_rating"] < 2.5:
        score += 0.2

    if features["avg_time_gap"] < 10:
        score += 0.2

    if features["helpfulness_ratio"] < 0.1:
        score += 0.1

    return round(min(score, 1.0), 2)
