#This script creates a dictionary of all the CH events as keys and a list of the
#performers in that event as values. It selects for only the performers who are
#in both the LJ and CH datasets.

from rdflib import Graph
from rdflib import URIRef
import json
import csv


events = Graph()
events.parse("ch_linkedJazz.nt", format="nt")

with open ('master_matches.json') as master_match:
    LJ_URI_matches = json.load(master_match)

with open ('name-string-matches_CH-URI.json') as CH_URI_string_match:
    CH_URI_matches = json.load(CH_URI_string_match)

event_info = {}

URI_ref_LJ = []
URI_ref_CH = []

#Lists of people matched in both datasets need to be converted to URIRefs
#so that they can be matched to the object (performer) URIRefs in the
#event data. Lists are converted to new lists of the data as URIRefs

for person in LJ_URI_matches:
    if person not in URI_ref_LJ:
        URI_ref_LJ.append(URIRef(person))

for ch_mint in CH_URI_matches:
    if ch_mint not in URI_ref_CH:
        URI_ref_CH.append(URIRef(ch_mint['CH URI']))

        
#Loop through the event data and find events and their associated performers from
#from the master list of matches (CH and LJ) using the LJ dataset URIs.        

for s,p,o in events:
    for person in URI_ref_LJ:
        if person == o:
            if s not in event_info:
                event_info[s] = []
            event_info[s].append(person)

#identify ch_mints in the event data that are matches for URIs in LJ (identified
#using the name parser string matching)and add them to the event dictionary

    for ch_mint in URI_ref_CH:
        if ch_mint ==o:       
            if s not in event_info:
                event_info[s] = []
            event_info[s].append(ch_mint)
            
#writing data to json gets rid of the RDFRef. I can then reopen it to replace the
#CH mint URIs with their corresponding LJ URIs from the CH_URI_matches dictionary
            
with open ('event_performer_dict.json', 'w') as f:
    f.write (json.dumps(event_info, indent=4))
    
    
    




