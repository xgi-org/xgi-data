# NDC substances

## Summary

This is a temporal higher-order network dataset, which here means a sequence of timestamped simplices where each simplex is a set of nodes. Under the Drug Listing Act of 1972, the U.S. Food and Drug Administration releases information on all commercial drugs going through the regulation of the agency, forming the National Drug Code (NDC) Directory. In this dataset, each simplex corresponds to an NDC code for a drug, and the nodes are substances that make up the drug. Timestamps are in days and represent when the drug was first marketed. We restricted to simplices that consist of at most 25 nodes. 


The file NDC-substances-node-labels.txt maps the node IDs to the substances.

The nth line in NDC-classes-simplex-labels.txt is the name of the drug
corresponding to the nth simplex.

## Statistics

* number of nodes: 5,311
* number of timestamped simplices: 112,405
* number of unique simplices: 10,025
* number of edges in projected graph: 88,268

## Origin of data

Source: [NDC-substances](https://www.cs.cornell.edu/~arb/data/NDC-substances/).

## References 

If you use this data, please cite the following paper:
Simplicial closure and higher-order link prediction.
Austin R. Benson, Rediet Abebe, Michael T. Schaub, Ali Jadbabaie, and Jon Kleinberg.
[Proceedings of the National Academy of Sciences (PNAS)](https://doi.org/10.1073/pnas.1800683115), 2018.