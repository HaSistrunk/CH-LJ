#this script combines the two lists of LJ-CH matches from string matches of names
#from the full set of CH people, and DBpedia matches from the CH event data. It
#creates a new list of LJ's URIs for all matches

import json

combined_matches = []

with open('name-string-matches.json') as string_match:
    match_a = json.load(string_match)

with open('LJ_DB_matches_from_events.json') as DBpedia_match:
    match_b = json.load(DBpedia_match)


for URIa in match_a:
    combined_matches.append(URIa)
for URIb in match_b:
    if URIb not in combined_matches:
        combined_matches.append(URIb)

#gets rid of any duplicates
master_matches = list(set(combined_matches))

#sort the list alphabetically
master_matches.sort()

#print (len(master_matches))


with open ('master_matches.json', 'w') as f:
    f.write(json.dumps(master_matches, indent=4))
