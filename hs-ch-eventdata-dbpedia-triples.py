#Using Carnegie Hall jazz event data from R. Hudson, this script isolates 
#the CH triples with object URIs from dbpedia using regex


from rdflib import Graph
from rdflib import URIRef
import re


#create data graph for Carnegie Hall event triples 
ch = Graph()

#Parse source, adding the resulting triples to the Graph.
#The file source is specified with a parameter added for format
ch.parse("ch_linkedJazz.nt", format="nt")


#create list of all triples in ch
chlist = []

for s,p,o in ch:
    if o not in chlist:
        chlist.append(o)

# number of ch objects
print ('Number of Carnegie Hall People:', len(chlist))
#prints 1291. Only 1291 out of 2878 triples in 'ch_linkedJazz.nt' file
#because the same person can be in multiple events

#convert list into string for regex. Add space between each object to assist compile
chstring = ' '.join(chlist)

#print (chstring)

#compile pattern to find only dbpedia objects
x = re.compile('([\w]{4}[\W]{3}[a-q]{7}[^\s]+)')

#search method
m = x.findall(chstring)

print (m)

print('Number of Carnegie Hall People in dbpedia:', len(m))


#Wrap list items in a URIRef

ch_dbplist = []

for obj in m:
    if obj not in ch_dbplist:
        ch_dbplist.append(URIRef(obj))

#print (ch_dbplist)

#Create new graph and load ch dbpedia triples into it

g= Graph()

for s,p,o in ch:
    for uri in ch_dbplist:
        if o == uri:
            g.add((s,p,o))

print ('Number of Carnegie Hall Events that include people in dbpedia:', len(g))
g.serialize('ch_dbpedia_triples.nt', format='nt')
        


