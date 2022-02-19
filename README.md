# xgi-data
 
This is a repository of openly available hypergraph datasets in JSON format with documentation more extensively describing the datasets. There is also a rudimentary inspection script for checking that datasets are in the proper format. This is loosely inspired by [Datasheets for Datasets](https://arxiv.org/abs/1803.09010) by Gebru et al.

Overview of the JSON data structure for all datasets:
* "hypergraph": This tag accesses the attributes of the entire hypergraph dataset such as the authors or dataset name.
* "nodes": This tag accesses the nodes of the hypergraph and their associated properties as a dictionary where the keys are node IDs and the corresponding values are dictionaries. If a node doesn't have any properties, the associated dictionary is empty.
  * "name": This tag accesses the node's name if there is one that is different from the ID specified in the hyperedges.
  * Other tags are user-specified based on the particular attributes provided by the dataset.
* "hyperedges": This tag accesses the hyperedges of the hypergraph and their associated attributes.
  * "members": This tag accesses the nodes which participate in that hyperedge.
  * "name": This tag accesses the edge's name if one is provided.
  * "timestamp": This is the tag specifying the time associated with the hyperedge if it is given. All times are stored in ISO8601 standard.
  * Other tags are user-specified based on the particular attributes provided by the dataset.

All IDs are strings but can be converted to other types if desired.

These datasets have been taken from the following sources:
* [Data! by Austin Benson](https://www.cs.cornell.edu/~arb/data/)

## Checking dataset format
Run the following command:
```
python inspect_json.py filepath.json
```