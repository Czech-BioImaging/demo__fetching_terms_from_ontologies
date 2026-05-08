This example is using the standard Python `requests` package.

### How to install

#### Using the prepared `pixi` environment

```bash
pixi shell
```

### How to use

```python
from query_requests import Requests
q = Requests(['fbbi', 'obi'])

q.search("confocal")

# returns a list of tripples
# - item label of an ontology
# - ontology shortname from which this label is taken
# - IRI of the found item
```
