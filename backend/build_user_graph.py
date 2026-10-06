# backend/build_user_graph.py

import json
import networkx as nx

DATA_PATH = "data/reviews.json"
GRAPH_PATH = "data/user_graph.gml"


def build_user_graph():
    print("🔗 Building user graph...")

    with open(DATA_PATH, "r") as f:
        reviews = json.load(f)

    G = nx.Graph()

    # Group users by product
    product_users = {}

    for r in reviews:
        product = r["product_id"]
        user = r["user_id"]

        if product not in product_users:
            product_users[product] = set()

        product_users[product].add(user)

    # Create edges
    for users in product_users.values():
        users = list(users)
        for i in range(len(users)):
            for j in range(i + 1, len(users)):
                G.add_edge(users[i], users[j])

    nx.write_gml(G, GRAPH_PATH)
    print(f"✅ Graph saved to {GRAPH_PATH}")


if __name__ == "__main__":
    build_user_graph()
