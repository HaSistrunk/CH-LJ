
#This script creates a json file from a list of all CH dbpedia URIs


from rdflib import Graph
import json


#create data graph for CH triples
ch = Graph()

#Parse source, adding the resulting triples to the Graph.
#The file source is specified with a parameter added for format
ch.parse("chAddressBook.nt", format="nt")


#create dictionary to fill with sweet, sweet, names
chNames = { }

#loop through triples finding all with foaf name property
for s, p, o in ch:
    if "foaf/0.1/name" in p:
        if s not in chNames:
            #fill dictionary with subject(URI) as key and object(name) as value
            chNames[s] = [o]

#write out json file
with open ('CH_allNames.json', 'w') as f:
    f.write(json.dumps(chNames ,indent=4))

print(len(chNames))
