import json

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def modify_and_save_graph_with_added_nodes(file1, file2, output_file, id_key='id'):
    # Load the scene graphs from the specified files
    graph1 = load_json(file1)
    graph2 = load_json(file2)

    # Find added nodes
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

# File paths for the input and output files
input_file1 = 'dsg_back_run1.json'  # Replace with actual file path
input_file2 = 'dsg_back_run2.json'  # Replace with actual file path
output_file = 'path_to_output_file.json'  # Replace with actual file path

# Run the function with the specified file paths
modify_and_save_graph_with_added_nodes(input_file1, input_file2, output_file)
