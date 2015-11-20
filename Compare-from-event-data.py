#this script finds the dBpedia URI matches between the LJ dataset and the
#CH event performers (there are more DBpedia URI's in the event data than
#in the addressbook.nt file). It saves the dbpedia matches to a list.

from rdflib import Graph
import json

ch = Graph()

ch.parse("ch_linkedJazz.nt", format="nt")

#Create data graph for LJ and parse the source, adding triples to graph
lj = Graph()
lj.parse("lj_data.nt", format="nt")

matches = []

#create a list of CH objects that match LJ subjects 
for s,p,o in ch:
    for a,b,c in lj:
        if o==a: #only the dbpedia URIs
            if o not in matches:
                matches.append(o)
matches.sort()

#print (len(matches)) #prints 268

with open ('LJ_DB_matches_from_events.json', 'w') as f:
    f.write(json.dumps(matches, indent=4))




