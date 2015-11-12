#This script compares the lj people to the full list of ch people and creates
#a dictionary of the LJ URIs and names of the people in both datasets
#(should it be a dictionary of the CH URIs instead?)
#This doesn't use the name parser, only exact string matches are matched

#from nameparser import HumanName
import json


lj_ch_match = {}

#open LJ json files
with open ('LJ_allNames.json', 'r') as LJ_data:
    ljdata = json.load(LJ_data)

with open ('CH_allNames.json', 'r') as CH_data:
    chdata = json.load(CH_data)

#loop through the people in both the lj and ch dictionaries and make a list of
#the people in both datasets:

#loop through lj names    
    for URIa in ljdata:
        ljperson =(ljdata[URIa])
        
#loop through ch names
        for URIb in chdata:
            chperson = (chdata[URIb])
            
#create a list of lj names that match ch names
            if ljperson == chperson:
                
                if ljperson not in lj_ch_match:
                    
                    lj_ch_match[URIa] = ljperson
                    
    #print (len(lj_ch_match)) #228 people

    with open('lj_ch_match.nt', 'w') as f:
        f.write(json.dumps(lj_ch_match, indent=4))

       


#Thinking about using human name parser to further compare names beyond match of both first and last
#parse name into parts
        #ljname = HumanName(ljperson)
        
#name is parsed. Can print specific parts of name like first, last, middle
        #print (ljname)
        #print (name.first)
        #print (name.middle)
                   
#nicknames are indicated as &quot;Moms&quot;
#The human name parser is pulling these out as middle names
        
            
    
##
##        for URI in chdata:
##            chperson = (chdata[URI])
##            chname = HumanName(chperson)
##            #print (chname)
##        
##            
##            if ljname == chname:
##                if ljname not in lj_ch_match:
##                    lj_ch_match.append(ljname)
##            print (lj_ch_match)
                


