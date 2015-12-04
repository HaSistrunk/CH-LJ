import json
import csv

with open('relatesCH.csv', 'w') as f:
    writer = csv.writer(f)

    with open ('relationshipsCH.json', 'r') as matches:
          relationships = json.load(matches)

    for someone in relationships:
          for a_relationship in relationships[someone]:
              target = a_relationship[0]

              writer.writerows([[someone,target]])
              






