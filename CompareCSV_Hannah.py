#Loops through the rows in the CH relationships csv and checks for matches in
#the LJ relationships csv.

import json
import csv


with open('Matching_relationships_CSV.csv', 'w') as overlap:
    writer = csv.writer(overlap)

    with open ('relatesLJ.csv', 'r') as f:
        LJrelates = csv.reader(f)
        
        with open ('relatesCH.csv', 'r') as g:
            CHrelates = csv.reader(g)
            
            for CH_row in CHrelates:
                #print (CH_row)
                if CH_row in LJrelates:
                    
                    print (LJ_row)
                else:
                    print (0)

#I also switched the columns in the relatesCH.csv and ran this script to be sure
#that the order of performers was not effecting matches (since the CH
#are not directional).
