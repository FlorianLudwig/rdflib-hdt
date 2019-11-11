"""proof of concept hdt in rdflib
"""

import rdflib.store
import hdt


def empty():
    return
    yield


class HDTStore(rdflib.store.Store):
    def __init__(self, configuration=None, identifier=None):
        self.doc:hdt.HDTDocument = None

    def __len__(self):
        if self.doc is None:
            return 0

        return self.doc.total_triples

    def open(self, path:str):
        self.doc = hdt.HDTDocument(path)

    def triples(self, query, context):
        query = [part if part else "" for part in query]
        triples, cardinality = self.doc.search_triples(*query)
        for triple in triples:
            yield triple, empty()

