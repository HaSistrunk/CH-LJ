import json


with open('CH_allNames.json') as json_data:
    ch = json.load(json_data)
    json_data.close()

with open('LJ_allNames.json') as json_data_2:
    lj = json.load(json_data_2)
    json_data_2.close()

sames = [ ]

for a_performer in lj:
    for another_one in ch:
        if a_performer[0] == another_one[0]:
            if a_performer not in sames:
                sames.append(a_performer)

with open ('Matches.json', 'w') as f:
    f.write(json.dumps(sames, indent=4))
