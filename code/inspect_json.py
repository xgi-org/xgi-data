import json
import sys

from sympy import hyper


# graph parameters
filename = sys.argv[1]

with open(filename) as file:
    data = json.loads(file.read())
    try:
        hypergraph_attrs = data["hypergraph"]

        try:
            name = hypergraph_attrs["name"]
        except:
            print("Dataset name not specified!")
    except:
        print("No hypergraph attributes!")

    try:
        nodes = data["nodes"]
    except:
        print("No nodes specified!")

    try:
        hyperedges = data["hyperedges"]

        for e in hyperedges:
            try:
                members = hyperedges[e]["members"]
                for node in members:
                    if node not in nodes:
                        print(f"Edge {e} contains non-existent node {node}!")
            except:
                print(f"Edge {e} has no associated members!")

    except:
        print("No hyperedges specified!")
    # print(hyperedges)
