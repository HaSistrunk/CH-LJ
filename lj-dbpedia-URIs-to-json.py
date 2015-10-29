#This script creates a json file from a list of all LJ dbpedia URIs


from rdflib import Graph
import re
import json


#create data graph for LJ triples 
lj = Graph()

#Parse source, adding the resulting triples to the Graph.
#The file source is specified with a parameter added for format
lj.parse("lj_data.nt", format="nt")


#create list of all triples in lj
ljlist = []

for s,p,o in lj:
    if s not in ljlist:
        ljlist.append(s)

#print (ljlist)

# number of unique lj subject URIs
print ('Number of Linked Jazz People:', len(ljlist))
#prints 2005. 

#convert rdflib URI list into string. Add space between each object to assist compile
ljstring = ' '.join(ljlist)

#print (ljstring)

#compile pattern to find only dbpedia objects
x = re.compile('([\w]{4}[\W]{3}d[a-q]{6}[^\s]+)')

#search method
m = x.findall(ljstring)

#print (m)

print('Number of Linked Jazz People in dbpedia:', len(m))
#prints 1516

#Write out list of dbpedia URIs to json
with open ('LJ-dbpedia-URIs.json', 'w') as f:
    f.write(json.dumps(m, indent=4))



