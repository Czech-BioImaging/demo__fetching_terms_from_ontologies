# Welcome

What can be found here:

- [Python example of fetching of terms (labels) from selected ontologies, EBI](query_via_EBIClient)
- [Python example of fetching of terms (labels) from selected ontologies, requests](query_via_requests)

Both should provide information to enable any GUI to mimic the interactive discovery
of ontology terms that are matching to the currently typed-in string. Example of such
behaviour can be examined here [at OLS web service](https://www.ebi.ac.uk/ols4/ontologies/fbbi/).

## Ontologies Sources

### Through the official OLS service

The examples are based primarily against the [EMBL-EBI Ontology Lookup Service
(OLS)](https://www.ebi.ac.uk/ols4/).

### Through an own instance of `gide-search`

It seems to be possible to [run own ontologies hosting server using the BioImage Archive's
`gide-search`](https://github.com/BioImage-Archive/gide-search#api). This, nevertheless,
seems to start the whole study records proxy (to the underlying archives -- sources of truth).
