import json

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def save_to_text_file(data, file_path):
    with open(file_path, 'w') as file:
        for line in data:
            file.write(f"{line}\n")

def get_comparison_key(node):
    # Extracts the 'position' and 'name' from the node's 'attributes', converting 'position' to a tuple
    return (
        tuple(node.get('attributes', {}).get('position', [])),  # Convert 'position' to a tuple
        node.get('attributes', {}).get('name')
    )

def has_required_attributes(node):
    # Checks if the node has 'position' and 'name' in its 'attributes'
    attributes = node.get('attributes', {})
    return all(key in attributes for key in ['position', 'name'])

def process_files(file1_path, file2_path, output_file_path, text_file1, text_file2, added_nodes_file):
    graph1 = load_json(file1_path)
    graph2 = load_json(file2_path)

    # Filter nodes with required attributes and create dictionaries with comparison keys
    filtered_nodes1 = filter(has_required_attributes, graph1['nodes'])
    filtered_nodes2 = filter(has_required_attributes, graph2['nodes'])
    keys1 = {get_comparison_key(node): node for node in filtered_nodes1}
    keys2 = {get_comparison_key(node): node for node in filtered_nodes2}

    # Identify added or changed nodes in graph2
    added_or_changed_nodes = [node for key, node in keys2.items() if key not in keys1]

    # Change color of added or changed nodes to green in graph2 and save the modified graph
    for node in added_or_changed_nodes:
        if 'attributes' in node:
            node['attributes']['color'] = [0, 255, 0]  # RGB for green

    with open(output_file_path, 'w') as file:
        json.dump(graph2, file, indent=4)

    # Save nodes and their IDs, positions, and names to text files
    save_to_text_file([f"ID: {node['id']}, Position: {key[0]}, Name: {key[1]}" for key, node in keys1.items()], text_file1)
    save_to_text_file([f"ID: {node['id']}, Position: {key[0]}, Name: {key[1]}" for key, node in keys2.items()], text_file2)
    save_to_text_file([f"ID: {node['id']}, Position: {get_comparison_key(node)[0]}, Name: {get_comparison_key(node)[1]}" for node in added_or_changed_nodes], added_nodes_file)

# File paths (replace with actual paths)
file1_path = 'dsg_obj_backend_run1.json'
file2_path = 'dsg_obj_backend_run2.json'
output_file_path = 'modified_dsg_obj_backend_run2.json'
text_file1 = 'nodes_file1.txt'
text_file2 = 'nodes_file2.txt'
added_nodes_file = 'added_nodes.txt'

process_files(file1_path, file2_path, output_file_path, text_file1, text_file2, added_nodes_file)
