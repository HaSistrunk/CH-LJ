#Replace the non-dbpedia URIs in the master csv with their common names using
#the lj data foaf:name.

import csv
from rdflib import Graph

links = [ ]
lined_up = { }

lj = Graph()
lj.parse("lj_data.nt", format="nt")

#open CSV file to write out URI, commonName
with open('relates_linksreplaced.csv', 'w', newline='') as f:
    writer = csv.writer(f)

#parse master list of source-targets
    with open('relatesMASTER.csv', 'r') as f:
        reader = csv.reader(f)

#find all the links
        for a_row in reader:
            if "http" in a_row[0]:
                links.append(a_row[0])

            if "http" in a_row[1]:
                links.append(a_row[1])

#get the commonName for each link
        for s,p,o in lj:
            if "foaf/0.1/name" in p:
                for a_link in links:
                    if a_link==str(s):
                        lined_up[a_link] = str(o)

                    writer.writerows([[a_link, str(o)]])


            #finish script -> need to find the URIs beginning for 'http' in
            #the relatesMASTER.csv and replace them with the corresponding
            #foaf:name from the lj data. Can do this through finding matching
            #URIs.
