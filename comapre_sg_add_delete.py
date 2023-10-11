# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 10:44:21 2023

@author: yasoo
"""

import json

def read_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def save_json(data, file_path):
    with open(file_path, 'w') as f:
        json.dump(data, f)

def detect_changes(graph1, graph2):
    changes = {}

    # Serialize each node and edge to a string to make them hashable
    nodes1_set = set(json.dumps(node, sort_keys=True) for node in graph1['nodes'])
    nodes2_set = set(json.dumps(node, sort_keys=True) for node in graph2['nodes'])

    added_nodes = nodes2_set - nodes1_set
    deleted_nodes = nodes1_set - nodes2_set

    if added_nodes:
        changes['nodes'] = [dict(json.loads(node_str), color=[128, 128, 128]) for node_str in added_nodes]  # Grey
    if deleted_nodes:
        changes['nodes'] = [dict(json.loads(node_str), color=[255, 255, 0]) for node_str in deleted_nodes]  # Yellow

    edges1_set = set(json.dumps(edge, sort_keys=True) for edge in graph1['edges'])
    edges2_set = set(json.dumps(edge, sort_keys=True) for edge in graph2['edges'])

    added_edges = edges2_set - edges1_set
    deleted_edges = edges1_set - edges2_set

    if added_edges:
        changes['edges'] = [dict(json.loads(edge_str), color=[128, 128, 128]) for edge_str in added_edges]  # Grey
    if deleted_edges:
        changes['edges'] = [dict(json.loads(edge_str), color=[255, 255, 0]) for edge_str in deleted_edges]  # Yellow

    return changes

def main():
    graph1 = read_json('old-dsg.json')
    graph2 = read_json('new-dsg.json')
    
    changes = detect_changes(graph1, graph2)
    
    save_json(changes, 'changes_add_del1.json')

if __name__ == '__main__':
    main()
