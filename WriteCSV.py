import json
import csv

with open('relatesLJ.csv', 'w') as f:
    writer = csv.writer(f)

    with open ('relationships_of_matches.json', 'r') as matches:
        relationships = json.load(matches)

    for someone in relationships:
        for a_relationship in relationships[someone]:
            target = a_relationship['target']

        # print(target)

            writer.writerows([[someone,target]])
