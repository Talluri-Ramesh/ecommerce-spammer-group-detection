def final_spam_decision(sps_score: float, community_flag: int, ml_prediction: int):
    """
    Combines SPS score, community detection flag, and ML prediction
    to make a final spam decision.
    """

    # Rule-based decision logic
    if sps_score > 0.7 and ml_prediction == 1:
        return {
            "final_label": 1,
            "reason": "High SPS score and ML-based spam prediction"
        }

    if community_flag == 1 and ml_prediction == 1:
        return {
            "final_label": 1,
            "reason": "Community-based spam group detected"
        }

    return {
        "final_label": 0,
        "reason": "User appears legitimate"
    }
