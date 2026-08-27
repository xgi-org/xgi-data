import json
import re
from pathlib import Path

index_file = Path(__file__).parent / "index.json"
readme_file = Path(__file__).parent / "README.md"

HEADER = """
# XGI-DATA
 
This is a repository of openly available hypergraph datasets in JSON format with documentation more extensively describing the datasets. They are hosted in the [XGI Community](https://zenodo.org/communities/xgi) on Zenodo and a table of statistics can be found on [Read The Docs](https://xgi.readthedocs.io/en/stable/xgi-data.html). This is loosely inspired by [Datasheets for Datasets](https://arxiv.org/abs/1803.09010) by Gebru et al. All datasets are stored in [Hypergraph Interchange Format (HIF)](https://github.com/HIF-org/HIF-standard).

## Data sets available on xgi-data

Currently available data sets are:
"""

FOOTER = """
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
"""


def zenodo_record_url(url):
    """Extract the Zenodo record URL from a Zenodo file URL."""
    match = re.search(r"zenodo.org/records/(\d+)", url)

    if match:
        return f"https://zenodo.org/records/{match.group(1)}"

    return None


def generate_dataset_list(index):
    """Generate the Markdown list of datasets."""
    lines = []
    for name in sorted(index):
        metadata = index[name]
        url = metadata.get("url", "")

        record_url = zenodo_record_url(url)

        if record_url:
            lines.append(f"* [{name}]({record_url})")
        else:
            lines.append(f"* [{name}]()")

    return "\n".join(lines)


with index_file.open("r", encoding="utf-8") as f:
    index = json.load(f)

if not isinstance(index, dict):
    raise ValueError("index.json must contain a JSON object/dictionary.")

dataset_list = generate_dataset_list(index)

readme = HEADER + dataset_list + "\n\n" + FOOTER.lstrip()

readme_file.write_text(readme, encoding="utf-8")

print(f"Generated {readme_file}")
print(f"Included {len(index)} datasets.")
