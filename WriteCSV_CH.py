#Creates a csv file of source and target from the CH relationships dictionary
#to be used for Gephi visualization

import json
import csv

#include newline='' parameter to prevent the csv from including a blank line
#between each row
with open('relatesCH.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    with open ('relationshipsCH.json', 'r') as matches:
          relationships = json.load(matches)

    for someone in relationships:
          for a_relationship in relationships[someone]:
              target = a_relationship

              writer.writerows([[someone,target]])
              






