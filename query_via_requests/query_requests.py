import requests
import json

class Requests():
    def __init__(self, ontologies: List[str], ontologies_server_url: str = 'https://www.ebi.ac.uk'):
        self.url = ontologies_server_url
        self.url_path = '/ols4/api/select'
        self.ontologies = ontologies
        self.choose_only_leafs = False

    def set_API_URL(self, new_url: str = 'https://www.ebi.ac.uk'):
        self.url = new_url

    def search(self, so_far_typed_search_term):
        results = []
        for onto in self.ontologies:
            params = { 'q':so_far_typed_search_term, 'ontology':onto, 'rows':20 }
            response = requests.get(self.url+self.url_path, params=params, timeout=5)

            # filter and collect responses
            for elem in response.json()['response']['docs']:
                results.append([ elem['label'], onto, elem['iri'] ])
        return results
