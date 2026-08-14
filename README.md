
# XGI-DATA
 
This is a repository of openly available hypergraph datasets in JSON format with documentation more extensively describing the datasets. They are hosted in the [XGI Community](https://zenodo.org/communities/xgi) on Zenodo and a table of statistics can be found on [Read The Docs](https://xgi.readthedocs.io/en/stable/xgi-data.html). There is also a rudimentary inspection script for checking that datasets are in the proper format. This is loosely inspired by [Datasheets for Datasets](https://arxiv.org/abs/1803.09010) by Gebru et al. All datasets are stored in [Hypergraph Interchange Format (HIF)](https://github.com/HIF-org/HIF-standard).

## Data sets available on xgi-data

Currently available data sets are:
* [biochem-cocitations](https://zenodo.org/records/20601519)
* [coauth-dblp](https://zenodo.org/records/10155873)
* [coauth-mag-geology](https://zenodo.org/records/10928443)
* [coauth-mag-history](https://zenodo.org/records/13151009)
* [congress-bills](https://zenodo.org/records/10928561)
* [contact-high-school](https://zenodo.org/records/10155802)
* [contact-primary-school](https://zenodo.org/records/10155810)
* [cs-cocitations](https://zenodo.org/records/19477689)
* [dawn](https://zenodo.org/records/10155779)
* [diseasome](https://zenodo.org/records/10155812)
* [disgenenet](https://zenodo.org/records/10155817)
* [email-enron](https://zenodo.org/records/10155819)
* [email-eu](https://zenodo.org/records/10155823)
* [eventernote-events](https://zenodo.org/records/11151063)
* [eventernote-places](https://zenodo.org/records/11263394)
* [hospital-lyon](https://zenodo.org/records/10155825)
* [house-bills](https://zenodo.org/records/10957691)
* [house-committees](https://zenodo.org/records/10957702)
* [hypertext-conference](https://zenodo.org/records/10206136)
* [hyperbard](https://zenodo.org/records/11211879)
* [invs13](https://zenodo.org/records/10206151)
* [invs15](https://zenodo.org/records/10206154)
* [kaggle-whats-cooking](https://zenodo.org/records/10157609)
* [malawi-village](https://zenodo.org/records/10206147)
* [math-cocitations](https://zenodo.org/records/20601560)
* [ndc-classes](https://zenodo.org/records/10155772)
* [ndc-substances](https://zenodo.org/records/10929019)
* [neuro-cocitations](https://zenodo.org/records/20601541)
* [physics-cocitations](https://zenodo.org/records/20601460)
* [plant-pollinator-mpl-014](https://zenodo.org/records/14561179)
* [plant-pollinator-mpl-015](https://zenodo.org/records/13754154)
* [plant-pollinator-mpl-016](https://zenodo.org/records/13754237)
* [plant-pollinator-mpl-021](https://zenodo.org/records/14561215)
* [plant-pollinator-mpl-034](https://zenodo.org/records/14561227)
* [plant-pollinator-mpl-044](https://zenodo.org/records/14561246)
* [plant-pollinator-mpl-046](https://zenodo.org/records/14561257)
* [plant-pollinator-mpl-049](https://zenodo.org/records/13754332)
* [plant-pollinator-mpl-057](https://zenodo.org/records/14561268)
* [plant-pollinator-mpl-062](https://zenodo.org/records/13753744)
* [science-gallery](https://zenodo.org/records/10206142)
* [senate-bills](https://zenodo.org/records/10957697)
* [senate-committees](https://zenodo.org/records/10957699)
* [sfhh-conference](https://zenodo.org/records/10198859)
* [tags-ask-ubuntu](https://zenodo.org/records/10155835)
* [tags-math-sx](https://zenodo.org/records/10155845)
* [tags-stack-overflow](https://zenodo.org/records/10155885)
* [threads-ask-ubuntu](https://zenodo.org/records/10373311)
* [threads-math-sx](https://zenodo.org/records/10373324)
* [threads-stack-overflow](https://zenodo.org/records/10373328)

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
