#This script compares the lj people to the full list of ch people and creates
#two dictionaries of the LJ URIs and CH URIs, respectivally, and the corresponding
#names of the people in both datasets
#This doesn't use the name parser or any other fancy string matching,
#only exact string matches

import json


lj_match = {}
ch_match = {}

#open LJ json files
with open ('LJ_allNames.json', 'r') as LJ_data:
    ljdata = json.load(LJ_data)

with open ('CH_allNames.json', 'r') as CH_data:
    chdata = json.load(CH_data)

#loop through the people in both the lj and ch dictionaries and make a dict of
#the people in both datasets:

#loop through lj names    
    for URIa in ljdata:
        ljperson =(ljdata[URIa])
        
#loop through ch names
        for URIb in chdata:
            chperson = (chdata[URIb])
            
#create a dict of lj names that match ch names
            if ljperson == chperson:
                
                if ljperson not in lj_match:
                    
                    lj_match[URIa] = ljperson

#create a dict of ch names that match lj names

                if chperson not in ch_match:

                    ch_match[URIb] = chperson
                    
    #print (len(lj_ch_match)) #228 people

#create json file of LJ dictionary of name matches

    with open('lj_match.json', 'w') as f:
        f.write(json.dumps(lj_match, indent=4))

#create json file of CH dictionary of name matches

    with open('ch_match.json', 'w') as g:
        g.write(json.dumps(ch_match, indent=4))



                


