
import json

#make a list
split_names = []

#open json file and load
with open('CH_namesOnly.json') as json_data:
    d = json.load(json_data)
    json_data.close()

for a_name in d:
    name = a_name.split("_")

    if name not in split_names:
        split_names.append(name)

    # print(names)

with open('CH_splitNames.json','w') as f:
    f.write(json.dumps(split_names,indent=4))
