from rdflib import Graph
import json

lj = Graph()

lj.parse("relationships.nt", format="nt")

match_relationships = {}

with open ('master_matches.json', 'r') as all_matches:
    master_matches = json.load(all_matches)

for a_match in master_matches:
    for s,p,o in lj:

        try:
            s = person1
            p = relationship
            o = person2
        except:
            continue

            if person1 in master_matches:
                if person1 not in match_relationships:
                    match_relationships[a_match] = [s,p,o]


print(match_relationships)
