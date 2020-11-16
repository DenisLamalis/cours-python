import json

with open('off_products_fr.json', encoding='utf-8') as json_file:
    data = json.load(json_file)

fields = (
    'product_name_fr', 
    'code', 
    'categories', 
    'nutriscore_grade', 
    'url', 
    'brands', 
    'stores' 
    )

data_clean = {}
tampon = {}

for n in range(len(data['products'])):
    print("===========================")

    for field in fields:
        print(field, data['products'][n][field].lower())

        tampon[field] = data['products'][n][field].lower()


print(tampon)