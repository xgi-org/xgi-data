# tags-ask-ubuntu

## Summary

This is a temporal higher-order network dataset, which here means a sequence of timestamped simplices where each simplex is a set of nodes. In this dataset, nodes are tags and simplices are the sets of tags applied to questions on math.stackexchange.com. 

Each simplex corresponds to all of the tags used in a post, and each node in a
simplex corresponds to a tag. The times are the time of the post in millisecond
but normalized so that the earliest tag starts at 0.

## Statistics

Some basic statistics of this dataset are:
* number of nodes: 1,629
* number of timestamped simplices: 822,059
* number of unique simplices: 174,933
* number of edges in projected graph: 91,685

## Source of original data

Source: [tags-math-sx dataset](https://www.cs.cornell.edu/~arb/data/tags-math-sx/)

## References

If you use this data, please cite the following paper:
* [Simplicial closure and higher-order link prediction](https://doi.org/10.1073/pnas.1800683115). Austin R. Benson, Rediet Abebe, Michael T. Schaub, Ali Jadbabaie, and Jon Kleinberg. Proceedings of the National Academy of Sciences (PNAS), 2018.