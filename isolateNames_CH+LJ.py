#Creates a list of dictionaries of all LJ URIs and CH URIs as key to their foaf:name


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
            ljNames[s] = o

##print (len(ljNames))

#define function to dump to json

def json_write(data):
    with open (file, 'w') as f:
        f.write(json.dumps(data, indent=4))


file = 'LJ_allNames.json'
print (json_write(ljNames))



#Repeat the same process for the CH data:

#create data graph for CHtriples
ch = Graph()

#Parse and add triples to the graph
ch.parse("chAddressBook.nt", format="nt")

chNames = {}

for s,p,o in ch:

    if 'foaf/0.1/name' in p:
        if s not in chNames:
            chNames[s] = o

##print (len(chNames))

#json dump (call the function)

file = 'CH_allNames.json'
print (json_write(chNames))









