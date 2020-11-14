import requests
import json 


URL = "https://fr.openfoodfacts.org/cgi/search.pl"

HEADERS = {"User-Agent": "P5_substitute - GNU/Windows - Version 0.1"}

PARAMS = {
    "search_simple": 1,
    "action": "process",
    "json": 1,
    "tagtype_0": "countries",
    "tag_contains_0": "contains",
    "tag_0": "france",
    "page_size": 20, 
    "page": 1,
    "sort_by": "unique_scans_n",
    "fields": "generic_name_fr",
}

# GET request 
response = requests.get(url = URL, params = PARAMS, headers = HEADERS) 

# extracting data in json format 
products = response.json() 

with open("off_products_fr.json", "w") as f:
    json.dump(products, f)

print(len(products['products']))