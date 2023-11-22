# tags-stack-overflow

## Summary

This dataset is derived from tags on Stack Overflow posts. The raw data was
downloaded from
https://archive.org/details/stackexchange

Each simplex corresponds to all of the tags used in a post, and each node in a
simplex corresponds to a tag. The times are the time of the post in millisecond
but normalized so that the earliest tag starts at 0.

## Statistics

Some basic statistics of this dataset are:
* number of nodes: 49,998
* number of timestamped simplices: 14,458,875
* number of unique simplices: 5,675,497
* number of edges in projected graph: 4,147,302

## Data:

Source: [tags-stack-overflow dataset](https://www.cs.cornell.edu/~arb/data/tags-stack-overflow/)

## References

If you use this data, please cite the following paper:
* [Simplicial closure and higher-order link prediction](https://doi.org/10.1073/pnas.1800683115). Austin R. Benson, Rediet Abebe, Michael T. Schaub, Ali Jadbabaie, and Jon Kleinberg. Proceedings of the National Academy of Sciences (PNAS), 2018.