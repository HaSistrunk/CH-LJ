#Replace the non-dbpedia URIs in the master csv with their common names using
#the lj data foaf:name. 

import csv
from rdflib import Graph

alls = [ ]

lj = Graph()
lj.parse("lj_data.nt", format="nt")

with open('relatesMASTER.csv', 'w') as f:
    relationships = csv.writer(f)

    for someone in relationships:
        for s,p,o in lj:

            #finish script -> need to find the URIs beginning for 'http' in
            #the relatesMASTER.csv and replace them with the corresponding
            #foaf:name from the lj data. Can do this through finding matching
            #URIs.


