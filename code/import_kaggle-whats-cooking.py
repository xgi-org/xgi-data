import os

import matplotlib.pyplot as plt
import numpy as np
import xgi

output_stats = True
output_file = True

data_folder = "data"

dataset_name = "cat-edge-Cooking"
new_dataset_name = "kaggle-whats-cooking"

dataset_folder = f"{dataset_name}"
edges_file = "hyperedges.txt"
n_labels_file = "node-labels.txt"
e_labels_file = "hyperedge-labels.txt"
l_identities_file = "hyperedge-label-identities.txt"

edgelist_file = os.path.join(data_folder, dataset_folder, edges_file)
node_labels_file = os.path.join(data_folder, dataset_folder, n_labels_file)
edge_labels_file = os.path.join(data_folder, dataset_folder, e_labels_file)
label_identities_file = os.path.join(data_folder, dataset_folder, l_identities_file)

H = xgi.read_edgelist(edgelist_file, delimiter="\t", nodetype=int)
H["name"] = new_dataset_name

with open(node_labels_file) as f:
    node_labels = f.read().splitlines()

for i, n in enumerate(H.nodes):
    H.nodes[n].update({"name": node_labels[i]})

with open(edge_labels_file) as f:
    edge_labels = f.read().splitlines()

with open(label_identities_file) as f:
    edge_label_identities = f.read().splitlines()

for i, e in enumerate(H.edges):
    H.edges[e].update({"name": edge_label_identities[int(edge_labels[i]) - 1]})


if output_stats:
    print((H.num_nodes, H.num_edges))

    vals, counts = np.unique(
        [len(c) for c in xgi.connected_components(H)], return_counts=True
    )
    print(np.array([vals, counts]))

    plt.figure(figsize=(8, 4))
    plt.subplot(121)

    degrees, counts = np.unique(H.nodes.degree.asnumpy(), return_counts=True)
    plt.loglog(degrees, counts / H.num_nodes, "ko", markersize=2)
    plt.title("Degree distribution")
    plt.xlabel(r"$k$", fontsize=16)
    plt.ylabel(r"$P(k)$", fontsize=16)
    plt.subplot(122)
    sizes, counts = np.unique(H.edges.size.asnumpy(), return_counts=True)
    plt.plot(sizes, counts / H.num_edges, "ko", markersize=2)
    plt.title("Edge size distribution")
    plt.xlabel(r"$m$", fontsize=16)
    plt.ylabel(r"$P(m)$", fontsize=16)
    plt.tight_layout()
    plt.savefig(f"{data_folder}/{dataset_folder}/stats.png", dpi=300)
    plt.show()


if output_file:
    xgi.write_json(
        H, os.path.join(data_folder, dataset_folder, f"{new_dataset_name}.json")
    )
