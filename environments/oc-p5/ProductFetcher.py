import requests
import json 

# api-endpoint 
URL = "https://fr.openfoodfacts.org/cgi/search.pl"

# defining a params dict for the parameters to be sent to the API 
PARAMS = {
    "action": "process",
    "json": 1,
    "tagtype_0": "countries",
    "tag_contains_0": "contains",
    "tag_0": "france",
    "page_size": 1, # ou 20, 50, 100, 250, 500
    "page": 1, # ou 2, 3, 4...
    "sort_by": "unique_scans_n", # popularité
}


# GET request 
response = requests.get(url = URL, params = PARAMS) 

# extracting data in json format 
products = response.json() 

# 
with open("off_products_fr.json", "w") as f:
    json.dump(products, f)

print(len(products))