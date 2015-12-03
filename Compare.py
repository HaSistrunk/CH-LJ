#This script compares both the first and last names of the LJ and CH ppl
#to find string matches between them and writes out a list of the LJ URIs
#associated with the person match AND a seperate dictionary of the CH URIs
#and their corresponding LJ URIs that match to be used later in working
#with the event data, which uses some CH mints)

import json

matches = [ ]
matches_CH = [ ]
CH_matches_dict ={}

with open('LJ_dict.json') as json_data_LJ:
    lj = json.load(json_data_LJ)
    json_data_LJ.close()

with open('CH_dict.json') as json_data_CH:
    ch = json.load(json_data_CH)
    json_data_CH.close()


#loop through both datasets and find matches of both first and last name
#pulled from the human name parser in the 'isolate_as_dict_CH+LJ.py' script
    
for a_person in lj:

    for someone in ch:

        if a_person['first name'] == someone['first name']:
            if a_person['last name'] == someone['last name']:
                if a_person not in matches:
                    matches.append(a_person['URI'])
                    CH_matches_dict['LJ URI'] = (a_person['URI'])
                    CH_matches_dict['CH URI'] = (someone['CH_URI'])
                    matches_CH.append(dict(CH_matches_dict))
                    

matches.sort()

#print (len(matches))



with open ('name-string-matches.json', 'w') as f:
    f.write(json.dumps(matches, indent=4))

with open ('name-string-matches_CH-URI.json', 'w') as g:
    g.write(json.dumps(matches_CH, indent=4))
