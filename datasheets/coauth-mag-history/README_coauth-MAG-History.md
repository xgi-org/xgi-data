# coauth-MAG-History

## Summary

This is a temporal higher-order network dataset, which here means a sequence of timestamped simplices where each simplex is a set of nodes. In this dataset, nodes are authors and a simplex is a publication marked with the "History" tag in the Microsoft Academic Graph. Timestamps are the year of publication. 

## Statistics

Some basic statistics of this dataset are:
* number of nodes: 1,014,734
* number of timestamped simplices: 1,812,511
* number of unique simplices: 895,668
* number of edges in projected graph: 1,156,914

## Changelog

- v1.2: fixed year format with PR #31 https://github.com/xgi-org/xgi-data/pull/31 
- v1.1: removed restriction on edge size (was max 25 nodes) with PR #22 https://github.com/xgi-org/xgi-data/pull/22

## Source of original data

Source: [coauth-MAG-History dataset](https://www.cs.cornell.edu/~arb/data/coauth-MAG-History/)

## References

If you use this data, please cite the following papers:

* [Simplicial closure and higher-order link prediction](https://doi.org/10.1073/pnas.1800683115). 
Austin R. Benson, Rediet Abebe, Michael T. Schaub, Ali Jadbabaie, and Jon Kleinberg. 
Proceedings of the National Academy of Sciences (PNAS), 2018.

* [An overview of Microsoft Academic Service (MAS) and applications[(https://doi.org/10.1145/2740908.2742839).
Arnab Sinha, Zhihong Shen, Yang Song, Hao Ma, Darrin Eide, Bo-June Hsu, and Kuansan Wang. 
Proceedings of WWW, 2015. 