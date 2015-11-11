#Testing human name parser

from nameparser import HumanName
import json

#open LJ json file
with open ('LJ_allNames.json', 'r') as LJ_data:
    data = json.load(LJ_data)

#loop through dictionary value (person's name)
    for URI in data:
        person =(data[URI])

#parse name into parts
        name = HumanName(person)
#name is parsed. Print only first name
        print (name.first)
        #print (name.middle)
        
#See http://nameparser.readthedocs.org/en/latest/usage.html            
            
#nicknames are indicated as &quot;Moms&quot;
#The human name parser is pulling these out as middle names
        
            
        

