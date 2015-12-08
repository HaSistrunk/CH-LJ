#Creates csv file of source and target of LJ KnowsOf relationships for use in
#Gephi visualization

import json
import csv

alls = [ ]

with open('relatesLJ.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    with open ('relationships_of_matches.json', 'r') as matches:
        relationships = json.load(matches)

    for someone in relationships:
        for a_relationship in relationships[someone]:
            target = a_relationship['target']

        # print(target)

            writer.writerows([[someone,target]])

with open('relatesLJ.csv','r') as f:

    reader = csv.reader(f)

    for a_row in reader:
        alls.append(a_row)

    print(len(alls))
