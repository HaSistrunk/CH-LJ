#splits names pulled out with the Regex_LJmints

import json

split_names_lj = []

#open json file and load
with open('LJ_namesOnly.json') as json_data:
    d = json.load(json_data)
    json_data.close()

for a_name in d:
    names = a_name.split("_")

    if names not in split_names_lj:
        split_names_lj.append(names)

#write out to json file
with open('LJ_splitNames.json','w') as f:
    f.write(json.dumps(split_names_lj,indent=4))

