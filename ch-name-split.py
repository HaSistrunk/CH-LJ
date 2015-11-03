
import json

#open json file and load
with open('CH_namesOnly.json') as json_data:
    d = json.load(json_data)
    json_data.close()

for a_name in d:
    names = a_name.split("_")

    print(names)
