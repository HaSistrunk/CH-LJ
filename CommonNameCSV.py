#Replace the non-dbpedia URIs in the master csv with their common names using
#the lj data foaf:name.

#Incomplete

import csv
from rdflib import Graph

links = [ ]
total = []
lined_up = { }


lj = Graph()
lj.parse("lj_data.nt", format="nt")

# #open CSV file to write out URI, commonName
# with open('relates_linksreplaced.csv', 'w', newline='') as f:
#     writer = csv.writer(f)

#parse master list of source-targets
with open('relatesMASTER.csv', 'r') as f:
    reader = csv.reader(f)

    with open('relatesMASTER_fullnames.csv', 'w', newline='') as g:
        writer = csv.writer(g)

    #find all the links
        for a_row in reader:
            if "http" in a_row[0]:
                links.append(a_row[0])

            if "http" in a_row[1]:
                links.append(a_row[1])

    #get the commonName for each link
        for s,p,o in lj:
             if "foaf/0.1/name" in p:
                for a_link in links:
                    if a_link==str(s):
                        lined_up['URI'] = a_link
                        lined_up['Name'] = str (o)
                        total.append(dict(lined_up))

        for someone in total:
            for a_row in reader:
                if a_row[0] == someone['URI']:
                    
                
##                if someone['URI'] in a_row[0]:
                    
   


##
##        for someone in total:
##            for a_row[0] in reader:
##                if someone['URI'] == a_row[0]:
##                    
##                    a_row[0] = someone['Name']
##                    
##                    if someone['URI'] == a_row[1]:
##                        a_row[1] = someone['Name']
##                    writer.write(a_row[0], a_row[1])
                    
                
                
   
##print(total)

                    # writer.writerows([[a_link, str(o)]])


            
           
