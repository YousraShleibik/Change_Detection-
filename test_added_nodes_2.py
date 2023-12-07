import json

# Function to load JSON data from a file
def load_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Function to find and update new nodes
def update_new_nodes(old_data, new_data):
    old_node_ids = {node['id'] for node in old_data['nodes']}
    for node in new_data['nodes']:
        if node['id'] not in old_node_ids:
            # Set the color to green (assuming RGB format)
            node['attributes']['color'] = [0, 255, 0]

# Function to save JSON data to a file
def save_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

# Load the JSON files
first_json = load_json('dsg_obj_backend_run1.json')
second_json = load_json('dsg_obj_backend_run2.json')

# Update new nodes in the second JSON file
update_new_nodes(first_json, second_json)

# Save the modified second JSON file
save_json(second_json, 'modified_second_json_file.json')
