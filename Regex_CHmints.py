import re
import json

#open json file and load
with open('CH_mints.json') as json_data:
    d = json.load(json_data)
    json_data.close()

    # print(d)
#convert to string
mintstring = ' '.join(d)

#compile regex to isolate just FirstName_LastName
p = re.compile('.{36}(\w+\_\w+)')

#find in string
m = p.findall(mintstring)

# print(m)

# write out to json file
with open('CH_namesOnly.json','w') as f:
    f.write(json.dumps(m,indent=4))
