#similar to the isolateNames_CH+LJ script, this creates a list of dictionaries
#of the URI and foaf:name of each person for each dataset

from rdflib import Graph
import json
from nameparser import HumanName


#create data graphs for LJ and CH triples and add the resulting triples to the Graphs 
lj = Graph()
lj.parse("lj_data.nt", format="nt")

ch =Graph()
ch.parse("chAddressBook.nt", format="nt")


ljNames = []
chNames = []
LJdict ={}
CHdict = {}


#create list of dictionaries for each person in LJ dataset with name (first, last, full) and URI

for s,p,o in lj:
    if 'foaf/0.1/name' in p:
        LJdict['full name']=o
        ljname = HumanName(LJdict['full name'])
        LJdict['first name'] = ljname.first
        LJdict['last name'] = ljname.last
        LJdict['URI']=s
        ljNames.append(dict(LJdict))
        
    

with open ('LJ_dict.json', 'w') as f:
    f.write(json.dumps(ljNames, indent=4))


#create list of dictionaries for each person in CH dataset with name (first, last, full) and CH URI

for x,y,z in ch:
    
    if 'foaf/0.1/name' in y:
        CHdict['full name']=z
        chname = HumanName(CHdict['full name'])
        CHdict['first name'] = chname.first
        CHdict['last name'] = chname.last
        CHdict['CH_URI']=x
        chNames.append(dict(CHdict))
        
##    for CHdict in chNames:
##        if (CHdict['CH_URI']) == x and "owl#sameAs" in y and "http://dbpedia.org/resource" in z:
##            CHdict['dbpedia_URI']=z
##            chNames.append(dict(CHdict))

                

with open ('CH_dict.json', 'w') as f:
    f.write(json.dumps(chNames, indent=4))
        












