# XGI-DATA
 
This is a repository of openly available hypergraph datasets in JSON format with documentation more extensively describing the datasets. There is also a rudimentary inspection script for checking that datasets are in the proper format. This is loosely inspired by [Datasheets for Datasets](https://arxiv.org/abs/1803.09010) by Gebru et al.

## Overview of the xgi-data format
The xgi-data format for hypergraph data sets is a JSON data structure with the following structure:
* "hypergraph-data": This tag accesses the attributes of the entire hypergraph dataset such as the authors or dataset name.
* "node-data": This tag accesses the nodes of the hypergraph and their associated properties as a dictionary where the keys are node IDs and the corresponding values are dictionaries. If a node doesn't have any properties, the associated dictionary is empty.
  * "name": This tag accesses the node's name if there is one that is different from the ID specified in the hyperedges.
  * Other tags are user-specified based on the particular attributes provided by the dataset.
* "edge-data": This tag accesses the hyperedges of the hypergraph and their associated attributes.
  * "name": This tag accesses the edge's name if one is provided.
  * "timestamp": This is the tag specifying the time associated with the hyperedge if it is given. All times are stored in ISO8601 standard.
  * Other tags are user-specified based on the particular attributes provided by the dataset.
* "edge-dict": This tag accesses the edge IDs and the corresponding nodes which participate in that hyperedge.

All IDs are strings but can be converted to other types if desired.

## Data sets available on xgi-data

Currently available data sets are:
* [coauth-dblp](https://zenodo.org/records/10155873)
* [coauth-mag-geology](https://zenodo.org/records/10155787)
* [coauth-mag-history](https://zenodo.org/records/10155796)
* [congress-bills](https://zenodo.org/records/10155800)
* [contact-high-school](https://zenodo.org/records/10155802)
* [contact-primary-school](https://zenodo.org/records/10155810)
* [dawn](https://zenodo.org/records/10155779)
* [diseasome](https://zenodo.org/records/10155812)
* [disgenenet](https://zenodo.org/records/10155817)
* [email-enron](https://zenodo.org/records/10155819)
* [email-eu](https://zenodo.org/records/10155823)
* [hospital-lyon](https://zenodo.org/records/10155825)
* [kaggle-whats-cooking](https://zenodo.org/records/10157609)
* [ndc-classes](https://zenodo.org/records/10155772)
* [ndc-substances](https://zenodo.org/records/10155831)
* [tags-ask-ubuntu](https://zenodo.org/records/10155835)
* [tags-math-sx](https://zenodo.org/records/10155845)
* [tags-stack-overflow](https://zenodo.org/records/10155885)

These datasets can be loaded with `xgi` using the following lines:
```python
import xgi
H = xgi.load_xgi_data("<dataset_name>")
```
where `<dataset_name>` is chosen from the list above.

These datasets have been taken from the following sources:
* [Data! by Austin Benson](https://www.cs.cornell.edu/~arb/data/)
* [DisGeneNet](https://www.disgenet.org/)
* [Gephi](https://github.com/gephi/gephi.github.io/)
* [SocioPatterns](http://www.sociopatterns.org/)

## Repository Description
`index.json` is a dictionary of the data sets that are currently available on xgi-data and the url where they are hosted.
The `code` folder contains the scripts used to convert hypergraph datasets into a more standard format and the JSON inspection script. This code can be adapted to convert data sets that are currently not part of xgi-data into xgi-data format.


## Checking dataset format
To check if a file has the xgi-data format, run the following command:
```
python inspect_json.py filepath.json
```

## Funding
The XGI-DATA package has been supported by NSF Grant 2121905, ["HNDS-I: Using Hypergraphs to Study Spreading Processes in Complex Social Networks"](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2121905).