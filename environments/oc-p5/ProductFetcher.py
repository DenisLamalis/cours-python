import requests
import json 


URL = "https://fr.openfoodfacts.org/cgi/search.pl"

PARAMS = {
    "action": "process",
    "json": 1,
    "tagtype_0": "countries",
    "tag_contains_0": "contains",
    "tag_0": "france",
    "page_size": 20, 
    "page": 1,
    "sort_by": "unique_scans_n",

}

# GET request 
response = requests.get(url = URL, params = PARAMS) 

# extracting data in json format 
products = response.json() 

with open("off_products_fr.json", "w") as f:
    json.dump(products, f)

print(len(products['products']))