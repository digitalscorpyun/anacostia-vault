import os
import re
import networkx as nx
from collections import defaultdict

# Path to your Obsidian vault (modify this)
VAULT_PATH = r"C:\Users\digitalscorpyun\Anacostia"

# Define weak link threshold (notes with fewer than this number of links are weak)
WEAK_LINK_THRESHOLD = 3

# Regex pattern to detect Obsidian [[wikilinks]]
LINK_PATTERN = r"\[\[(.*?)\]\]"

def get_markdown_files(vault_path):
    """Retrieve all markdown files in the Obsidian vault."""
    return [os.path.join(root, file)
            for root, _, files in os.walk(vault_path)
            for file in files if file.endswith(".md")]

def extract_links_from_file(file_path):
    """Extract all wikilinks from a given markdown file."""
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    return re.findall(LINK_PATTERN, content)

def build_graph(vault_path):
    """Create a directed graph representing the linking structure."""
    graph = nx.DiGraph()
    backlinks = defaultdict(set)

    for file_path in get_markdown_files(vault_path):
        note_name = os.path.basename(file_path).replace(".md", "")
        links = extract_links_from_file(file_path)

        # Add nodes (notes)
        graph.add_node(note_name)

        # Track backlinks
        for link in links:
            graph.add_edge(note_name, link)
            backlinks[link].add(note_name)

    return graph, backlinks

def find_weakly_connected_notes(graph):
    """Identify notes with fewer than the threshold number of links."""
    weak_notes = [node for node, degree in graph.degree() if degree < WEAK_LINK_THRESHOLD]
    return weak_notes

def suggest_links(weak_notes, backlinks):
    """Suggest potential links based on common backlinks and metadata."""
    recommendations = {}

    for note in weak_notes:
        suggested_links = set()

        # Find notes that link to the same sources as this weak note
        for linked_note in backlinks.get(note, []):
            suggested_links.update(backlinks.get(linked_note, []))

        # Remove self-links
        suggested_links.discard(note)

        if suggested_links:
            recommendations[note] = list(suggested_links)[:3]  # Suggest up to 3 new links

    return recommendations

def main():
    print("🔍 Scanning Obsidian vault for weakly connected notes...")
    
    graph, backlinks = build_graph(VAULT_PATH)
    weak_notes = find_weakly_connected_notes(graph)

    print(f"⚠️ Found {len(weak_notes)} weakly connected notes (less than {WEAK_LINK_THRESHOLD} links).")

    if not weak_notes:
        print("✅ No weak notes detected!")
        return

    recommendations = suggest_links(weak_notes, backlinks)

    print("\n📌 Suggested Fixes for Weakly Connected Notes:")
    for note, suggested_links in recommendations.items():
        print(f"  - **{note}** → Consider linking to: {', '.join(suggested_links)}")

    print("\n📂 Saving report to `weak_notes_report.txt`...")
    with open("weak_notes_report.txt", "w", encoding="utf-8") as report:
        for note, suggested_links in recommendations.items():
            report.write(f"{note}: {', '.join(suggested_links)}\n")

    print("✅ Report saved! Open `weak_notes_report.txt` for suggestions.")

if __name__ == "__main__":
    main()
