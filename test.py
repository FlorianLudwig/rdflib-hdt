import sys
import time

import rdflib.store
import hdt

import rdflib_hdt


WD = rdflib.Namespace("http://www.wikidata.org/entity/")
WDT = rdflib.Namespace("http://www.wikidata.org/prop/")
WIKIBASE = rdflib.Namespace("http://wikiba.se/ontology-beta#")
SCHEMA = rdflib.Namespace("http://schema.org/")

namespaces = {
    "wd": WD,
    "wdt": WDT,
    "wikibase": WIKIBASE,
    "schema": SCHEMA,
}


def main():
    store = rdflib_hdt.HDTStore()
    # tested with wikidata set from http://www.rdfhdt.org/datasets/
    store.open(sys.argv[1])
    graph = rdflib.Graph(store)

    t = time.time()
    qres = graph.query(
    """
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wds: <http://www.wikidata.org/entity/statement/>
PREFIX wdv: <http://www.wikidata.org/value/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX wikibase: <http://wikiba.se/ontology#>
PREFIX p: <http://www.wikidata.org/prop/>
PREFIX ps: <http://www.wikidata.org/prop/statement/>
PREFIX pq: <http://www.wikidata.org/prop/qualifier/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX bd: <http://www.bigdata.com/rdf#>

SELECT ?work
WHERE
{
  ?work wdt:P31/wdt:P279* wd:Q838948.
}
LIMIT 1000
""", initNs=namespaces)

    for row in qres:
        print(row)

    print(time.time() - t)


if __name__ == "__main__":
    main()