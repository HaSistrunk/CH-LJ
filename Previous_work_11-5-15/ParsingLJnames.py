import json
from nameparser import HumanName

with open('LJ_allNames.json') as json_data_2:
    lj = json.load(json_data_2)
    json_data_2.close()

for a_performer in lj:
    name = a_performer

# structuredName = HumanName(name)

    print(name)
