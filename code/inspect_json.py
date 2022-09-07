import json
import sys

# graph parameters
filename = sys.argv[1]

with open(filename) as file:
    # load JSON file
    data = json.loads(file.read())

    # load hypergraph attributes
    try:
        hypergraph_attrs = data["hypergraph-data"]

        # Is a dataset name specified?
        try:
            name = hypergraph_attrs["name"]
        except:
            print("Dataset name not specified!")
    except:
        print("No hypergraph attributes!")

    # Are nodes specified?
    try:
        node_data = data["node-data"]
    except:
        print("No nodes specified!")

    # Are hyperedges specified?
    try:
        edge_data = data["edge-data"]

    except:
        print("No hyperedges specified!")

    try:
        edges = data["edge-dict"]
        for e in edges:
            # are the nodes in the hyperedges in the list of nodes?
            if e not in edge_data:
                print(f"edge {e} not in the list of edges.")
            try:
                members = edges[e]
                for node in members:
                    if node not in node_data:
                        print(f"Edge {e} contains non-existent node {node}!")
            except:
                print(f"Edge {e} has no associated members!")

    except:
        print("No hyperedges specified!")

print("Inspection complete.")
