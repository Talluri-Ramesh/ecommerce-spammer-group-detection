import pandas as pd

FEATURES_PATH = "results/master_features.csv"
SPS_PATH = "results/sps_scores.csv"
OUTPUT_PATH = "results/final_features_with_sps.csv"

print("🔍 Loading master features...")
features = pd.read_csv(FEATURES_PATH)

print("📊 Loading SPS scores...")
sps = pd.read_csv(SPS_PATH)

# Rename column for consistency
sps = sps.rename(columns={"SPS": "sps_score"})

print("🔗 Merging SPS with features...")
merged = features.merge(
    sps[["user_id", "sps_score", "label"]],
    on="user_id",
    how="left"
)

merged.to_csv(OUTPUT_PATH, index=False)

print("✅ Merge complete!")
print(f"📁 Saved to {OUTPUT_PATH}")
