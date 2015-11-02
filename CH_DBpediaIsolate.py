
#This script creates a json file from a list of all CH dbpedia URIs


from rdflib import Graph
import json


#create data graph for CH triples
ch = Graph()

#Parse source, adding the resulting triples to the Graph.
#The file source is specified with a parameter added for format
ch.parse("ch_linkedJazz.nt", format="nt")


#create list of all triples in ch
chlist = []
mintsCH = []

#loop through, find 'dbpedia' in object (not all objects are names so I am foregoing counting all of them)
for s,p,o in ch:

    if 'dbpedia' in o:
        if o not in chlist:
            #build list from objects because subject repeats
            chlist.append(o)
    
    else:
        if "data.carnegiehall" in o:
            if o not in mintsCH:
                mintsCH.append(o)

    # print(len(ch))

# #convert to string
chstring = ' '.join(chlist)
mintstring = ' '.join(mintsCH)

# print (chstring)

#write out json file
with open ('CH_dbpedia.json', 'w') as f:
    f.write(json.dumps(chlist ,indent=4))
    
with open ('CH_mints.json', 'w') as f:
    f.write(json.dumps(mintsCH ,indent=4))
    
    
