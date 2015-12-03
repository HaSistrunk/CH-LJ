
from rdflib import Graph


lj = Graph()

lj.parse("lj_ppl.nt", format="nt")

ljNames = {}

for s,p,o in lj:

    if 'foaf/0.1/name' in p:
        if s not in ljNames:
            ljNames[s] = o

print (len(ljNames))
