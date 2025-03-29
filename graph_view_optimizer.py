<<<<<<< HEAD
import os
import re
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict
import sys

# Use provided command-line argument as vault path or fallback to default
VAULT_PATH = sys.argv[1] if len(sys.argv) > 1 else r"C:\Users\miker\OneDrive\Documents\Anacostia"

# Define your core hub notes for interlinking
HUB_NOTES = {
    "roadmap-anacostia-vault",
    "00-index",
    "africana-studies-overview",
    "ai-ml-overview",
    "personal-development-digitalscorpyun"
}

def get_links(file_path):
    """Extract [[wikilinks]] from a markdown file and return them as a set."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        return set(re.findall(r'\[\[(.*?)\]\]', content))

def analyze_graph():
    """Analyze and visualize the knowledge graph by recursively scanning subdirectories."""
    G = nx.Graph()
    all_files = []

    # Recursively collect all markdown files from subdirectories
    for root, dirs, files in os.walk(VAULT_PATH):
        for file in files:
            if file.endswith(".md"):
                relative_path = os.path.relpath(os.path.join(root, file), VAULT_PATH)
                normalized_name = relative_path.replace("\\", "/").replace(".md", "")
                all_files.append(normalized_name)

    # Ensure all files are nodes in the graph
    for file in all_files:
        G.add_node(file)

    # Track links
    links = defaultdict(set)

    for file in all_files:
        file_path = os.path.join(VAULT_PATH, file + ".md")
        extracted_links = get_links(file_path)
        links[file] = extracted_links

        for linked_file in extracted_links:
            linked_file = linked_file.strip()
            if linked_file in all_files:
                G.add_edge(file, linked_file)

    # Identify orphaned and weakly connected notes
    orphaned_notes = [f for f in G.nodes if G.degree(f) == 0]
    weakly_connected_notes = [f for f in G.nodes if G.degree(f) == 1]

    # Connect orphaned notes to hub notes
    for orphan in orphaned_notes:
        for hub in HUB_NOTES:
            if hub in all_files:
                G.add_edge(orphan, hub)

    # Print summary
    print("\n=== Graph View Analysis Report ===\n")
    print("🔴 Orphaned Notes (No In/Out Links):", orphaned_notes or "None")
    print("🟡 Weakly Connected Notes (Only 1 Link):", weakly_connected_notes or "None")
    print("🟢 Graph Optimization Complete!")

    # Graph visualization
    if G.number_of_nodes() > 0:
        pos = nx.spring_layout(G, seed=42, k=0.5)
        plt.figure(figsize=(14, 9))
        nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='gray', node_size=2500, font_size=10)
        plt.title("Obsidian Vault Graph View (Recursive Scan)")
        plt.show()
    else:
        print("⚠️ No graph data to display!")

if __name__ == "__main__":
    analyze_graph()
=======
import os
import re
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict
import sys

# Use provided command-line argument as vault path or fallback to default
VAULT_PATH = sys.argv[1] if len(sys.argv) > 1 else r"C:\Users\miker\OneDrive\Documents\Anacostia"

# Define your core hub notes for interlinking
HUB_NOTES = {
    "roadmap-anacostia-vault",
    "00-index",
    "africana-studies-overview",
    "ai-ml-overview",
    "personal-development-digitalscorpyun"
}

def get_links(file_path):
    """Extract [[wikilinks]] from a markdown file and return them as a set."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        return set(re.findall(r'\[\[(.*?)\]\]', content))

def analyze_graph():
    """Analyze and visualize the knowledge graph by recursively scanning subdirectories."""
    G = nx.Graph()
    all_files = []

    # Recursively collect all markdown files from subdirectories
    for root, dirs, files in os.walk(VAULT_PATH):
        for file in files:
            if file.endswith(".md"):
                relative_path = os.path.relpath(os.path.join(root, file), VAULT_PATH)
                normalized_name = relative_path.replace("\\", "/").replace(".md", "")
                all_files.append(normalized_name)

    # Ensure all files are nodes in the graph
    for file in all_files:
        G.add_node(file)

    # Track links
    links = defaultdict(set)

    for file in all_files:
        file_path = os.path.join(VAULT_PATH, file + ".md")
        extracted_links = get_links(file_path)
        links[file] = extracted_links

        for linked_file in extracted_links:
            linked_file = linked_file.strip()
            if linked_file in all_files:
                G.add_edge(file, linked_file)

    # Identify orphaned and weakly connected notes
    orphaned_notes = [f for f in G.nodes if G.degree(f) == 0]
    weakly_connected_notes = [f for f in G.nodes if G.degree(f) == 1]

    # Connect orphaned notes to hub notes
    for orphan in orphaned_notes:
        for hub in HUB_NOTES:
            if hub in all_files:
                G.add_edge(orphan, hub)

    # Print summary
    print("\n=== Graph View Analysis Report ===\n")
    print("🔴 Orphaned Notes (No In/Out Links):", orphaned_notes or "None")
    print("🟡 Weakly Connected Notes (Only 1 Link):", weakly_connected_notes or "None")
    print("🟢 Graph Optimization Complete!")

    # Graph visualization
    if G.number_of_nodes() > 0:
        pos = nx.spring_layout(G, seed=42, k=0.5)
        plt.figure(figsize=(14, 9))
        nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='gray', node_size=2500, font_size=10)
        plt.title("Obsidian Vault Graph View (Recursive Scan)")
        plt.show()
    else:
        print("⚠️ No graph data to display!")

if __name__ == "__main__":
    analyze_graph()
>>>>>>> 769b11b2f1b8510b1da5db510583301e7c9784a9
