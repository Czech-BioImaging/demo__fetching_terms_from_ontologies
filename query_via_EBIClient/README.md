This example is based on the [BioImage Archive's `gide-search`
`utils`](https://github.com/BioImage-Archive/gide-search/tree/main/src/gide_search/utils).

### How to install

```bash
git clone git@github.com:BioImage-Archive/gide-search.git
cd gide-search
pixi init
```

### How to use

```python
from query_EBI import EBI as Q
q = Q(['fbbi', 'obi'])

# for inspiration of what ontologies (and what are they shortnames) are supported:
q.list_all_ontologies_from_the_source()

q.search("confocal")

# returns a list of tripples
# - item label of an ontology
# - ontology shortname from which this label is taken
# - IRI of the found item
```
