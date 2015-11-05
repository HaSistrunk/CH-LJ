#Isolates only the LJ mint names using regex

import re
import json

#open json file and load
with open('LJ-mints.json') as json_data:
    d = json.load(json_data)
    json_data.close()

    # print(d)
#convert to string
mintstring = ' '.join(d)

#compile regex to isolate just FirstName_LastName
p = re.compile('.{32}(\w+\_\w+)')

#find in string
m = p.findall(mintstring)

print (len(m))

###write out to json file
##with open('LJ_namesOnly.json','w') as f:
##    f.write(json.dumps(m,indent=4))



