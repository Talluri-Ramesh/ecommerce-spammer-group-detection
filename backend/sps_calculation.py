import pandas as pd
from sklearn.preprocessing import MinMaxScaler

INPUT = "results/master_features.csv"
OUTPUT = "results/sps_scores.csv"

print("🔍 Loading master features...")
df = pd.read_csv(INPUT)

# ---------- SELECT FEATURES ----------
risk_features = [
    "review_count",
    "rating_std",
    "avg_time_gap",
    "avg_review_length",
    "avg_unique_ratio",
    "duplicate_review_ratio"
]

df_risk = df[risk_features].copy()

# ---------- RISK NORMALIZATION ----------
print("⚖ Normalizing risk features...")
scaler = MinMaxScaler()

df_risk_scaled = pd.DataFrame(
    scaler.fit_transform(df_risk),
    columns=risk_features
)

# ---------- RISK DIRECTION ADJUSTMENTS ----------
df_risk_scaled["avg_time_gap"] = 1 - df_risk_scaled["avg_time_gap"]
df_risk_scaled["avg_review_length"] = 1 - df_risk_scaled["avg_review_length"]
df_risk_scaled["avg_unique_ratio"] = 1 - df_risk_scaled["avg_unique_ratio"]

# ---------- SPS COMPUTATION ----------
weights = {
    "review_count": 0.20,
    "rating_std": 0.20,
    "avg_time_gap": 0.15,
    "avg_review_length": 0.15,
    "avg_unique_ratio": 0.15,
    "duplicate_review_ratio": 0.15
}

print("🧮 Calculating SPS...")
df["SPS"] = sum(
    weights[f] * df_risk_scaled[f]
    for f in risk_features
)

# ---------- LABELING ----------
def label_user(score):
    if score >= 0.6:
        return "SPAMMER"
    elif score >= 0.3:
        return "SUSPICIOUS"
    else:
        return "NORMAL"

df["label"] = df["SPS"].apply(label_user)

# ---------- SAVE ----------
output_df = df[["user_id", "SPS", "label"]]

print("💾 Saving SPS results...")
output_df.to_csv(OUTPUT, index=False)

print("✅ STEP 13 COMPLETE")
print(output_df["label"].value_counts())
