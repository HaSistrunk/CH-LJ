#This script loops through the dictionary of events (keys) and performers (values)
#and creates a new dictionary of each performer (key) and a list of other
#performers that they played in events with (values). This puts the data in a
#format where we can work with the relationships between performers  

import json

with open ('event_performer_dict.json') as f:
    event_dict = json.load(f)

dictionary = {}

for an_event in event_dict:
    list_of_players = event_dict[an_event]
    
    for a_player in list_of_players:
        for other_player in list_of_players:
            if a_player != other_player:
                
                if a_player not in dictionary:
                    dictionary[a_player] = []
                if other_player not in dictionary[a_player]:
                    dictionary[a_player].append(other_player)

##print (len(dictionary))
            
with open ('relationshipsCH.json', 'w') as f:
    f.write (json.dumps(dictionary, indent=4))
    
    





