#This script creates a dictionary of all the CH events as keys and a list of the
#performers in that event as values. It selects for only the performers who are
#in both the LJ and CH datasets.

from rdflib import Graph
import json


events = Graph()
events.parse("ch_linkedJazz.nt", format="nt")

with open ('master_matches.json') as master_match:
    LJ_URI_matches = json.load(master_match)

with open ('name-string-matches_CH-URI.json') as CH_URI_string_match:
    CH_URI_matches = json.load(CH_URI_string_match)

event_info = {}

        
#Loop through the event data and find events and their associated performers
#from the master list of matches (CH and LJ) using the LJ dataset URIs.        

for s,p,o in events:
    for person in LJ_URI_matches:
        if person == str(o):
            if str(s) not in event_info:
                event_info[str(s)] = []
            event_info[str(s)].append(person)

#identify ch_mints in the event data that are matches for URIs in LJ (identified
#using the name parser string matching)and add them to the event dictionary

    for ch_mint in CH_URI_matches:
        if ch_mint['CH URI'] ==str(o):
            ch_mint['CH URI'] = ch_mint['LJ URI']
            if str(s) not in event_info:
                event_info[str(s)] = []
            event_info[str(s)].append(ch_mint['CH URI'])
            
#write the dictionary to json
            
with open ('event_performer_dict.json', 'w') as f:
    f.write (json.dumps(event_info, indent=4))
    
    
    




