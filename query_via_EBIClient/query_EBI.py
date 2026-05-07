from ols_client import EBIClient
import json

class EBI():
    def __init__(self, ontologies: List[str]):
        self.ebiclient = EBIClient()
        self.ontologies = ontologies
        self.choose_only_leafs = False

    def set_API_URL(self, new_url: str = 'https://www.ebi.ac.uk/ols4/api'):
        self.ebiclient.base_url = new_url

    def search(self, so_far_typed_search_term):
        results = []
        for onto in self.ontologies:
            response = self.ebiclient.get_response(
                path=f"v2/ontologies/{onto}/classes",
                params={
                    "search": f"*{so_far_typed_search_term}*",
                    "page": 0,
                    "size": 20,
                    "searchFields": "label^100 synonym^5 description",
                    "definedBy": onto,
                    "resolveReferences": True,
                    "manchesterSyntax": True,
                    "lang": "en",
                },
            )
            r = json.loads(response.content)

            # filter and collect responses
            for elem in r['elements']:
                if not elem['isObsolete'] and (not self.choose_only_leafs or elem['hasDirectChildren'] == False):
                    results.append([elem['label'][0], onto, elem['iri']])
        return results

# some more notes:
#
#   r['label'][0]            - to display, to search for
#   r['hasDirectChildren']   ~ is a leaf?
#       r['numDescendants'] == 0?
#   r['isObsolete'] == false
#   r['iri'] - to keep with this value (attribute, to which this is a value,
#              has iri to the rembi-cz space)
