#Test d'ouverture de fichier .json

import json

with open('response.json', encoding='utf-8') as json_file:
    data = json.load(json_file)

print(data)