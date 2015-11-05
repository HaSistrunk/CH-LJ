#Creates dictionary of all LJ URIs as key to their foaf:name


from rdflib import Graph
import json


#create data graph for LJ triples 
lj = Graph()

#Parse source, adding the resulting triples to the Graph.
#The file source is specified with a parameter added for format
lj.parse("lj_data.nt", format="nt")

ljNames = {}

#loop through triples to create dictionary
for s,p,o in lj:

    if 'foaf/0.1/name' in p:
        if s not in ljNames:
            ljNames[s] = [o]

print (len(ljNames))

#Write out json files
with open ('LJ_allNames.json', 'w') as f:
    f.write(json.dumps(ljNames, indent=4))








