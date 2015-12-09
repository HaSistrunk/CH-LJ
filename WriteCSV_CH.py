#Creates a csv file of source and target from the CH relationships dictionary
#to be used for Gephi visualization

import json
import csv
from rdflib import Graph

#include newline='' parameter to prevent the csv from including a blank line
#between each row

lj = Graph()
lj.parse("lj_data.nt", format="nt")

with open('relatesCH.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    with open ('relationshipsCH.json', 'r') as matches:
        relationships = json.load(matches)
          

        for someone in relationships:
            for a_relationship in relationships[someone]:
                target = a_relationship

#Change the URI to the foafName for output to csv
                for s,p,o in lj:
                    if "foaf/0.1/name" in p:
                        if someone == str(s): 
                            someone = str(o)
                        if target == str(s):
                            target = str(o)

                  
                            writer.writerows([[someone,target]])
              






