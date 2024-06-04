# Contributing

## Adding a dataset to XGI-DATA

### Creating a JSON file for a dataset
1. Create a script titled `import_<dataset name>.py`. Choose a dataset name that is concise, yet descriptive.
2. Convert the raw data into an `xgi` hypergraph, using the above script. Examples of importing are in the [code](/code/) folder.
3. Save the dataset to a JSON file using the `xgi.write_json()` [method](https://xgi.readthedocs.io/en/stable/api/readwrite/xgi.readwrite.json.html#module-xgi.readwrite.json).

### Adding to Zenodo
1. Navigate to the [XGI page](https://zenodo.org/communities/xgi) on Zenodo.
2. Click the "New Upload" button. This should prompt you to log into Zenodo and will bring up the form to upload a new dataset.
3. Enter the information in the "new upload" form:
   1. In the "Files" section, drag and drop the file or click the "Upload files" button.
   2. When asked "Do you already have a DOI for this upload?", select "No".
   3. Under "Resource type", select "Dataset" from the dropdown list.
   4. Under "Title" enter the dataset name selected above.
   5. Under "Creators", add yourself with name, ORCID, and affiliation along with your role (typically "Data collector" or "Data curator")
   6. Under "Description" write the name of the dataset, where it is from, how it was collected, what nodes and edges are, and some basic statistics about the dataset.
   7. Under "Version", type "v0.0" if this is the first version of the dataset.
4. Click the "Submit for review" button. This will send it to the XGI-DATA moderators for review.

Once the dataset has been added to Zenodo, do the following:

### Updating Github
1. Fork XGI-DATA.
2. Move the import script created prior to the `code` folder.
3. Add an entry (in alphabetical order) in `index.json` with:
   1. The dataset name as the key (all lowercase!)
   2. The value as a dictionary `{"url": <url>}`
   3. The url can be found by going to the [XGI page](https://zenodo.org/communities/xgi) on Zenodo, and clicking on the record you just made. Then the url is `https://zenodo.org/records/<number>/<dataset name>.json`.
4. In `README.md`, add the dataset name (alphabetically) as a hyperlink with the Zenodo page url.
5. Run `get_stats.json` with the dataset name as an argument in `load_xgi_data()`. If every cell in this notebook is run, it will update the `index.json` file and add a plot of the degree/edge size distribution.