import json

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def modify_and_save_graph_with_added_nodes(file1, file2, output_file, id_key='id'):
    # Load the scene graphs
    graph1 = load_json(file1)
    graph2 = load_json(file2)

    # Find added nodes as before
    def node_signature(node):
        return frozenset({k: v for k, v in node.items() if k != id_key}.items())

    nodes1 = {node_signature(node) for node in graph1}
    nodes2 = {node_signature(node) for node in graph2}

    added_nodes_signatures = nodes2 - nodes1

    # Modify the color of added nodes in graph2
    for node in graph2:
        if node_signature(node) in added_nodes_signatures:
            node['color'] = 'green'  # Change the color to green

    # Save the modified graph2 to a new JSON file
    with open(output_file, 'w') as file:
        json.dump(graph2, file)

# Example scene graphs with IDs
example_graph1_with_ids = [
    {"id": 1, "type": "chair", "color": "blue"},
    {"id": 2, "type": "table", "color": "red"}
]

example_graph2_with_ids = [
    {"id": 3, "type": "chair", "color": "blue"},
    {"id": 4, "type": "table", "color": "red"},
    {"id": 5, "type": "lamp", "color": "yellow"}  # initially not green
]

# Writing these example graphs to JSON files
with open("example_graph1_with_ids.json", "w") as file:
    json.dump(example_graph1_with_ids, file)

with open("example_graph2_with_ids.json", "w") as file:
    json.dump(example_graph2_with_ids, file)

# File paths for the example
input_file1 = 'example_graph1_with_ids.json'
input_file2 = 'example_graph2_with_ids.json'
output_file = 'modified_graph2.json'

# Run the function with the example files
modify_and_save_graph_with_added_nodes(input_file1, input_file2, output_file)

# For demonstration, let's load and display the content of the modified file
with open(output_file, 'r') as file:
    modified_graph = json.load(file)

modified_graph

# Output:
