
# XGI-DATA
 
This is a repository of openly available hypergraph datasets in JSON format with documentation more extensively describing the datasets. They are hosted in the [XGI Community](https://zenodo.org/communities/xgi) on Zenodo and a table of statistics can be found on [Read The Docs](https://xgi.readthedocs.io/en/stable/xgi-data.html). This is loosely inspired by [Datasheets for Datasets](https://arxiv.org/abs/1803.09010) by Gebru et al. All datasets are stored in [Hypergraph Interchange Format (HIF)](https://github.com/HIF-org/HIF-standard).

## Data sets available on xgi-data

Currently available data sets are:
* [a-blue-start](https://zenodo.org/records/19713302)
* [arxiv-kaggle](https://zenodo.org/records/15808027)
* [biochem-cocitations](https://zenodo.org/records/20601519)
* [coauth-dblp](https://zenodo.org/records/21905305)
* [coauth-mag-geology](https://zenodo.org/records/21906243)
* [coauth-mag-history](https://zenodo.org/records/21909251)
* [congress-bills](https://zenodo.org/records/21909280)
* [contact-high-school](https://zenodo.org/records/21909303)
* [contact-primary-school](https://zenodo.org/records/21909335)
* [cs-cocitations](https://zenodo.org/records/19477689)
* [dawn](https://zenodo.org/records/21909345)
* [diseasome](https://zenodo.org/records/21909416)
* [email-enron](https://zenodo.org/records/21909507)
* [email-eu](https://zenodo.org/records/21909519)
* [eventernote-events](https://zenodo.org/records/21917912)
* [eventernote-places](https://zenodo.org/records/21917851)
* [hospital-lyon](https://zenodo.org/records/21935628)
* [house-bills]()
* [house-committees](https://zenodo.org/records/21935676)
* [hyperbard](https://zenodo.org/records/21935772)
* [hypertext-conference](https://zenodo.org/records/21936138)
* [invs13](https://zenodo.org/records/21937109)
* [invs15](https://zenodo.org/records/21937140)
* [kaggle-whats-cooking](https://zenodo.org/records/21937157)
* [malawi-village](https://zenodo.org/records/21937170)
* [math-cocitations](https://zenodo.org/records/20601560)
* [ndc-classes](https://zenodo.org/records/21937180)
* [ndc-substances](https://zenodo.org/records/21937240)
* [neuro-cocitations](https://zenodo.org/records/20601541)
* [physics-cocitations](https://zenodo.org/records/20601460)
* [plant-pollinator-mpl-014](https://zenodo.org/records/21937333)
* [plant-pollinator-mpl-015](https://zenodo.org/records/21937438)
* [plant-pollinator-mpl-016](https://zenodo.org/records/21938203)
* [plant-pollinator-mpl-021](https://zenodo.org/records/21938213)
* [plant-pollinator-mpl-034](https://zenodo.org/records/21938218)
* [plant-pollinator-mpl-044](https://zenodo.org/records/21938231)
* [plant-pollinator-mpl-046](https://zenodo.org/records/21938240)
* [plant-pollinator-mpl-049](https://zenodo.org/records/21938279)
* [plant-pollinator-mpl-057](https://zenodo.org/records/21938299)
* [plant-pollinator-mpl-062](https://zenodo.org/records/21938320)
* [recipe-rec](https://zenodo.org/records/14003376)
* [science-gallery](https://zenodo.org/records/21938382)
* [senate-bills](https://zenodo.org/records/21938408)
* [senate-committees](https://zenodo.org/records/21938419)
* [sfhh-conference](https://zenodo.org/records/21938430)
* [tags-ask-ubuntu](https://zenodo.org/records/21938441)
* [tags-math-sx](https://zenodo.org/records/21938463)
* [tags-stack-overflow](https://zenodo.org/records/21938788)
* [threads-ask-ubuntu](https://zenodo.org/records/21938799)
* [threads-math-sx](https://zenodo.org/records/21938817)
* [threads-stack-overflow](https://zenodo.org/records/21938825)

These datasets can be loaded with `xgi` using the following lines:
```python
import xgi
H = xgi.load_xgi_data("<dataset_name>")
```
where `<dataset_name>` is chosen from the list above.

These datasets have been taken from the following sources:
* [Data! by Austin Benson](https://www.cs.cornell.edu/~arb/data/)
* [Gephi](https://github.com/gephi/gephi.github.io/)
* [SocioPatterns](http://www.sociopatterns.org/)

## Repository Description
`index.json` is a dictionary of the data sets that are currently available on xgi-data and the url where they are hosted.
The `code` folder contains the scripts used to convert hypergraph datasets into a more standard format and the JSON inspection script. This code can be adapted to convert data sets that are currently not part of xgi-data into xgi-data format.

## Funding
The XGI-DATA package has been supported by NSF Grant 2121905, ["HNDS-I: Using Hypergraphs to Study Spreading Processes in Complex Social Networks"](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2121905).
