'''import json

# Function to load JSON data from a file
def load_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Function to find new nodes and extract their ID and name
def find_and_extract_new_nodes(old_data, new_data):
    old_node_ids = {node['id'] for node in old_data['nodes']}
    new_node_info = []
    for node in new_data['nodes']:
        if node['id'] not in old_node_ids:
            # Extract ID and name
            node_id = node['id']
            node_name = node.get('name', 'No name provided')  # Default if no name is available
            new_node_info.append(f"ID: {node_id}, Name: {node_name}")
    return new_node_info

# Function to save the extracted information to a text file
def save_to_text(data, filename):
    with open(filename, 'w') as file:
        for line in data:
            file.write(line + '\n')

# Function to save JSON data to a file
def save_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

# Load the JSON files
first_json = load_json('dsg_obj_backend_run1.json')
second_json = load_json('dsg_obj_backend_run2.json')

# Find new nodes and extract their ID and name
added_node_info = find_and_extract_new_nodes(first_json, second_json)

# Save the new node information to a text file
save_to_text(added_node_info, 'added_nodes_info.txt')'''
import json

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def save_to_text_file(data, file_path):
    with open(file_path, 'w') as file:
        for line in data:
            file.write(f"{line}\n")

def get_node_id_and_name(node):
    node_id = node.get('id')
    node_name = node.get('attributes', {}).get('name', 'No name')  # Adjusted for nested 'name'
    return node_id, node_name

def process_files(file1_path, file2_path, output_file_path, text_file1, text_file2, added_nodes_file):
    graph1 = load_json(file1_path)
    graph2 = load_json(file2_path)

    # Extract nodes and their IDs from both graphs
    nodes1 = {node['id']: node for node in graph1['nodes']}
    nodes2 = {node['id']: node for node in graph2['nodes']}

    # Save nodes and their IDs to text files
    save_to_text_file([f"ID: {id}, Name: {get_node_id_and_name(node)[1]}" for id, node in nodes1.items()], text_file1)
    save_to_text_file([f"ID: {id}, Name: {get_node_id_and_name(node)[1]}" for id, node in nodes2.items()], text_file2)

    # Find added nodes in graph2
    added_nodes = {id: node for id, node in nodes2.items() if id not in nodes1}
    
    # Change color of added nodes to green in graph2 and save the modified graph
    for node in added_nodes.values():
        if 'attributes' in node:
            node['attributes']['color'] = [0, 255, 0]  # RGB for green

    with open(output_file_path, 'w') as file:
        json.dump(graph2, file, indent=4)

    # Save added nodes to a text file
    save_to_text_file([f"ID: {id}, Name: {get_node_id_and_name(node)[1]}" for id, node in added_nodes.items()], added_nodes_file)

# Usage
file1_path = 'dsg_obj_backend_run1.json'
file2_path = 'dsg_obj_backend_run2.json'
output_file_path = 'modified_dsg_obj_backend_run2.json'
text_file1 = 'nodes_file1.txt'
text_file2 = 'nodes_file2.txt'
added_nodes_file = 'added_nodes.txt'

process_files(file1_path, file2_path, output_file_path, text_file1, text_file2, added_nodes_file)
