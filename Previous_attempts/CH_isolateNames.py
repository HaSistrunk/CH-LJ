#This script loops through the chAddressBook.net and creates a dictionary
#of CH URIs (people) as they key, and their foaf:Name as the value.


from rdflib import Graph
import json


#create data graph for CH triples
ch = Graph()

#Parse source, adding the resulting triples to the Graph.
#The file source is specified with a parameter added for format
ch.parse("chAddressBook.nt", format="nt")


#create dictionary to fill with CH names
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

#print(len(chNames)) #19197 people
