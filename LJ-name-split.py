#splits names pulled out with the Regex_LJmints

import json

#open json file and load
with open('LJ_namesOnly.json') as json_data:
    d = json.load(json_data)
    json_data.close()

for a_name in d:
    names = a_name.split("_")

    print (len(d))


    

