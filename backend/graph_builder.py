import pandas as pd
import networkx as nx
from itertools import combinations

INPUT = "data/cleaned_reviews.csv"
OUTPUT = "results/user_graph.gml"

print("🔍 Loading cleaned reviews...")
df = pd.read_csv(INPUT)

# Normalize column names
df.columns = [c.lower() for c in df.columns]

# Auto-detect columns
user_col = "user_id"
product_col = "product_id"

if "rating" in df.columns:
    rating_col = "rating"
elif "score" in df.columns:
    rating_col = "score"
else:
    raise Exception("❌ No rating column found!")

if "timestamp" in df.columns:
    time_col = "timestamp"
elif "time" in df.columns:
    time_col = "time"
else:
    raise Exception("❌ No time column found!")

# Convert time safely
df[time_col] = pd.to_datetime(df[time_col], errors="coerce")
df = df.dropna(subset=[time_col])

# Reduce size (VERY IMPORTANT)
df = df.sample(min(60000, len(df)), random_state=42)

print("🔗 Grouping reviews by product...")
groups = df.groupby(product_col)

G = nx.Graph()

print("🧠 Building user similarity graph...")
for _, group in groups:
    users = group[[user_col, rating_col, time_col]].to_dict("records")

    for u1, u2 in combinations(users, 2):
        rating_sim = 1 - abs(u1[rating_col] - u2[rating_col]) / 5
        time_diff = abs((u1[time_col] - u2[time_col]).total_seconds())
        time_sim = 1 / (1 + time_diff)

        weight = 0.7 * rating_sim + 0.3 * time_sim

        if weight > 0.5:
            G.add_edge(u1[user_col], u2[user_col], weight=round(weight, 3))

print("💾 Saving graph...")
nx.write_gml(G, OUTPUT)

print("✅ STEP 8 COMPLETE")
print("Nodes:", G.number_of_nodes())
print("Edges:", G.number_of_edges())
