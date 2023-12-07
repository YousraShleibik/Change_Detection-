import json

def save_node_ids_and_labels(file_path, output_file):
    # Load the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)

    results = []  # List to hold the results

    # Check if 'nodes' key exists
    if 'nodes' in data and isinstance(data['nodes'], list):
        for node in data['nodes']:
            if 'id' in node and 'name' in node:
                node_id = node['id']
                label = node['name']
                results.append({"Node ID": node_id, "Label": label})
            else:
                # Optionally, add a message for nodes missing fields
                missing_fields = [field for field in ['id', 'name'] if field not in node]
                results.append({"Missing Fields": ', '.join(missing_fields)})

    # Save the results to a JSON file
    with open(output_file, 'w') as outfile:
        json.dump(results, outfile, indent=4)

# Example usage
file_path = './dsg_back_run1.json'
output_file_path = 'node_ids_and_labels.json'
save_node_ids_and_labels(file_path, output_file_path)

# Note: Replace 'path_to_your_json_file.json' with the actual path to your JSON file






