#This script creates two json files: one from a list of all LJ dbpedia URIs and
#one from all LJ mints


from rdflib import Graph
import json


#create data graph for LJ triples 
lj = Graph()

#Parse source, adding the resulting triples to the Graph.
#The file source is specified with a parameter added for format
lj.parse("lj_data.nt", format="nt")

dbpediaLJ = []
mintsLJ = []

#loop through, find 'dbpedia' in subject
for s,p,o in lj:

    if 'dbpedia' in s:
        if s not in dbpediaLJ:
            dbpediaLJ.append(s)

    else:
#loop to find 'linkedjazz in subject
        if 'linkedjazz' in s:
            if s not in mintsLJ:
                mintsLJ.append(s)

#number of dbpedia URIs
print ('dbpedia entities:', len(dbpediaLJ))

#number of LJ mints
print ('LJ mints:', len(mintsLJ))


#Write out list of dbpedia names to json
with open ('LJ_dbpedia.json', 'w') as f:
    f.write(json.dumps(dbpediaLJ, indent=4))

#Write out list of LJ mint names to json
with open ('LJ-mints.json', 'w') as f:
    f.write(json.dumps(mintsLJ, indent=4))



