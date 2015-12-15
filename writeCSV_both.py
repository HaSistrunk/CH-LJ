#This script finds the duplicates in the relatesMASTER.csv files and writes
#them out to a new csv. These are the relationships that exist in both the LJ
#and CH datasets

#note: to run script, remove the "CH" or "LJ" designations from relatesMaster.csv


import csv

duplicate_rows = []
unique_rows = []

with open ('relatesMaster.csv', 'r') as f:
    reader = csv.reader(f)

    with open ('relatesBOTH.csv', 'w', newline='') as g:
        writer = csv.writer(g)

        for row in reader:

            if row not in unique_rows:
                unique_rows.append(row)
            else:
                duplicate_rows.append(row)
            
        for a_row in duplicate_rows:
            source = a_row[0]
            target = a_row[1] 
            
            writer.writerows([[source, target]])
            
print (len(duplicate_rows))

                
#this script (below) was used to assure that there were no duplicates in the
#relatesLJ.csv and relatesCH.csv because there were combined manually to
#make the relatesMASTER.csv. This assures that the script above is only finding
#relationships that overlap BETWEEN the LJ and CH datasets.
                       
##import csv
##
##duplicate_rows = []
##unique_rows = []
##
##with open ('relatesLJ.csv', 'r') as f:
##    reader = csv.reader(f)
##
##
##    for row in reader:
##
##        if row not in unique_rows:
##            unique_rows.append(row)
##        else:
##            duplicate_rows.append(row)
##            
##    
##print (duplicate_rows)
