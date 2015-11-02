import re
import json

#open json file and load
with open('CH_mints.json') as json_data:
    d = json.load(json_data)
    json_data.close()

    # print(d)
mintstring = ' '.join(d)

p = re.compile('.{36}(\w+\_\w+)')

m = p.findall(mintstring)

# print(m)
with open('CH_namesOnly.json','w') as f:
    f.write(json.dumps(m,indent=4))
