# coauth-MAG-Geology

## Summary

This is a temporal higher-order network dataset, which here means a sequence of timestamped simplices where each simplex is a set of nodes. In this dataset, nodes are authors and a simplex is a publication marked with the "Geology" tag in the Microsoft Academic Graph. Timestamps are the year of publication. The projected graph is a weighted undirected graph representing how many times each pair of nodes co-appears in a simplex. We restricted to simplices that consist of at most 25 nodes. 

## Statistics

Some basic statistics of this dataset are:
* number of nodes: 1,256,385
* number of timestamped simplices: 1,590,335
* number of unique simplices: 1,207,390
* number of edges in projected graph: 512,0762

## Source of original data

Source: [coauth-MAG-Geology dataset](https://www.cs.cornell.edu/~arb/data/coauth-MAG-Geology/)

## References

If you use this data, please cite the following papers:

* [Simplicial closure and higher-order link prediction](https://doi.org/10.1073/pnas.1800683115). 
Austin R. Benson, Rediet Abebe, Michael T. Schaub, Ali Jadbabaie, and Jon Kleinberg. 
Proceedings of the National Academy of Sciences (PNAS), 2018.

* [An overview of Microsoft Academic Service (MAS) and applications[(https://doi.org/10.1145/2740908.2742839).
Arnab Sinha, Zhihong Shen, Yang Song, Hao Ma, Darrin Eide, Bo-June Hsu, and Kuansan Wang. 
Proceedings of WWW, 2015. 