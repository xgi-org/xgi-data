import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import xgi

output_stats = True
output_file = True

data_folder = "data"

dataset_folder = "disgenenet"
edges = "disGene.txt"
genes = "gene_associations.tsv"
diseases = "disease_associations.tsv"

edgelist_file = os.path.join(data_folder, dataset_folder, edges)
genes_file = os.path.join(data_folder, dataset_folder, genes)
diseases_file = os.path.join(data_folder, dataset_folder, diseases)

H = xgi.read_bipartite_edgelist(edgelist_file)
H["name"] = "disgenenet"

gene_data = pd.read_csv(genes_file, delimiter="\t")
node_attr = {str(id): {"symbol": val} for id, val in zip(gene_data["geneId"], gene_data["geneSymbol"]) if str(id) in H.nodes}

xgi.set_node_attributes(H, node_attr)

disease_data = pd.read_csv(diseases_file, delimiter="\t")
edge_attr = {str(id): {"name": val} for id, val in zip(disease_data["diseaseId"], disease_data["diseaseName"]) if str(id) in H.edges}

xgi.set_edge_attributes(H, edge_attr)

if output_stats:
    print((H.num_nodes, H.num_edges))

    print([len(c) for c in xgi.connected_components(H)])

    plt.figure(figsize=(8, 4))
    plt.subplot(121)

    degrees, counts = np.unique(H.nodes.degree.asnumpy(), return_counts=True)
    plt.loglog(degrees, counts / H.num_nodes, "ko", markersize=2)
    plt.title("Degree distribution")
    plt.xlabel(r"$k$", fontsize=16)
    plt.ylabel(r"$P(k)$", fontsize=16)
    plt.subplot(122)
    sizes, counts = np.unique(H.edges.size.asnumpy(), return_counts=True)
    plt.loglog(sizes, counts / H.num_edges, "ko", markersize=2)
    plt.title("Edge size distribution")
    plt.xlabel(r"$m$", fontsize=16)
    plt.ylabel(r"$P(m)$", fontsize=16)
    plt.tight_layout()
    plt.savefig("data/disgenenet/stats.png", dpi=300)
    plt.show()


if output_file:
    xgi.write_json(H, os.path.join(data_folder, dataset_folder, "disgenenet.json"))
