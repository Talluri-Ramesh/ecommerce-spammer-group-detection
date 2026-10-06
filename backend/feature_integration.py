import pandas as pd

BEHAVIORAL = "results/user_features.csv"
TEXTUAL = "results/textual_features.csv"
OUTPUT = "results/master_features.csv"

print("🔍 Loading feature files...")
df_behavioral = pd.read_csv(BEHAVIORAL)
df_textual = pd.read_csv(TEXTUAL)

print("🔗 Merging features...")
df_master = pd.merge(
    df_behavioral,
    df_textual,
    on="user_id",
    how="inner"
)

print("🧹 Handling missing values...")
df_master = df_master.fillna(0)

print("💾 Saving master feature vector...")
df_master.to_csv(OUTPUT, index=False)

print("✅ STEP 12 COMPLETE")
print("Users in master vector:", len(df_master))
