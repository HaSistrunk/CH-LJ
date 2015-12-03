import json
import csv

with open ('relationships_of_matches.json', 'r') as matches:
    relationships = json.load(matches)

for someone in relationships:
    for a_relationship in relationships[someone]:
        target = relationships[someone][0]['target']

    # print(target)

print(someone)
