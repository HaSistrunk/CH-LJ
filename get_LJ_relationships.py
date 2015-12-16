#Using the master list of matches between the LJ and CH datasets and the LJ
#relationship triples, this script creates a dictionary where each key is a
#LJ person, and each person key contains a list of dictionaries for each
#person they are related to. This json output will be used to create a csv of
#source and target for use in Gephi.

from rdflib import Graph
import json


#create data graph for LJ triples
lj = Graph()

#Parse source, adding the resulting triples to the Graph.
lj.parse("relationships.nt", format="nt")

# for s,p,o in lj:
#     print(s)

match_relationships = {}

with open ('master_matches.json', 'r') as matches:
    master_matches = json.load(matches)


for a_match in master_matches:
    for s,p,o in lj:
        if str(p)=="http://purl.org/vocab/relationship/knowsOf":
            if a_match==str(s) or a_match==str(o):
                if a_match not in match_relationships:
                    match_relationships[a_match] = []
                if a_match==str(s):
                    one_matchRELs = {}
                    one_matchRELs["relationship"] = p
                    one_matchRELs["target"] = o
                else:
                    one_matchRELs = {}
                    one_matchRELs["relationship"] = p
                    one_matchRELs["target"] = s
                match_relationships[a_match].append(one_matchRELs)

##print(len(match_relationships))

with open ('relationships_of_matches.json', 'w') as f:
    f.write(json.dumps(match_relationships, indent=4))



