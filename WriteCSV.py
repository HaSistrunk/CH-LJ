#Creates csv file of source and target of LJ KnowsOf relationships for use in
#Gephi visualization

import json
import csv
from rdflib import Graph

alls = [ ]

lj = Graph()
lj.parse("lj_data.nt", format="nt")

with open('relatesLJ.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    with open ('relationships_of_matches.json', 'r') as matches:
        relationships = json.load(matches)

    for someone in relationships:
        for a_relationship in relationships[someone]:
            target = a_relationship['target']

#Change the URI to the foafName for output to csv
            for s,p,o in lj:
                if "foaf/0.1/name" in p:
                    if someone == str(s): 
                        someone = str(o)
                    if target == str(s):
                        target = str(o)
                        
##                        print(someone, target)

                        writer.writerows([[someone,target]])

            

##with open('relatesLJ.csv','r') as f:
##
##    reader = csv.reader(f)
##
##    for a_row in reader:
##        alls.append(a_row)
##
##    print(len(alls))
