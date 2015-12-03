#This script attempts to replace the CH minted URIs in the event dictionary
#(created by event_performer_dict.py) with their corresponding LJ URIs using
#the 'name-string-matches_CH-URI.json dictionary

#Incomplete

import json


event_dict_final = {}

with open ('name-string-matches_CH-URI.json') as CH_URI_string_match:
    CH_URI_matches = json.load(CH_URI_string_match)
    
     
with open ('event_performer_dict.json') as g:
    event_dict = json.load(g)
    
    
    for an_event in event_dict:
        for performer in event_dict[an_event]:
                 
            for ch_mint in CH_URI_matches:
                    
                if performer == ch_mint['CH URI']:
                    performer = ch_mint['LJ URI']
                        #print (performer) # ->This prints the correct URI,
                                            # but I can't get it to stick in
                                            # the dictionary when I write to 
                                            #a file.

    
                    
with open ('event_dict_final.json', 'w') as h:
    h.write (json.dumps(event_dict, indent=4))
              






