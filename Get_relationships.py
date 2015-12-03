from rdflib import Graph
import json


#create data graph for LJ triples
lj = Graph()

#Parse source, adding the resulting triples to the Graph.
#The file source is specified with a parameter added for format
lj.parse("relationships.nt", format="nt")


# for s,p,o in lj:
#     print(s)

match_relationships = {}

with open ('master_matches.json', 'r') as matches:
    master_matches = json.load(matches)

# print(master_matches)
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



# for s in lj:
#     try:
#         if s not in match_relationships:
#             match_relationships[s] = one_matchRELs[s]
#     except:
#         continue

# for a_match in master_matches:
#     for s,p,o in lj:
#         if a_match in s:
#             one_matchRELs[s] = [p,o]

#
#       if a_match in o:
#             match_relationships[a_match] = one_matchRELs[s] = [p,o]

#
print(len(match_relationships))

with open ('relationships_of_matches.json', 'w') as f:
    f.write(json.dumps(match_relationships, indent=4))
