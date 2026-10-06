import networkx as nx
import json
from networkx.algorithms.community import louvain_communities

GRAPH_PATH = "data/user_graph.gml"
OUTPUT_PATH = "data/user_communities.json"


def detect_communities():
    print("🔍 Loading user graph...")
    G = nx.read_gml(GRAPH_PATH)

    print("🧠 Running Louvain community detection...")
    communities = louvain_communities(G, seed=42)

    user_community_map = {}

    for idx, community in enumerate(communities):
        for user in community:
            user_community_map[user] = idx

    with open(OUTPUT_PATH, "w") as f:
        json.dump(user_community_map, f, indent=4)

    print(f"✅ Communities saved to {OUTPUT_PATH}")
    print(f"📊 Total communities detected: {len(communities)}")


if __name__ == "__main__":
    detect_communities()
