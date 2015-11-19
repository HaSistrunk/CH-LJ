from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import difflib
import json

maybes = { }

with open('LJ_dict.json') as json_data_LJ:
    lj = json.load(json_data_LJ)
    json_data_LJ.close()

with open('CH_dict.json') as json_data_CH:
    ch = json.load(json_data_CH)
    json_data_CH.close()

for a_person in lj:
    lj_name = a_person['full name']

for someone in ch:
    ch_name = someone['full name']

    for a_person in lj:
        for someone in ch:
            d = fuzz.ratio('lj_name', 'ch_name')

            if ch_name not in maybes:
                maybes[d] = [ch_name, lj_name]

# if d >= 50:
#     print(ch_name, lj_name, d)

print(maybes)
