import json

with open('off_products_fr.json', encoding='utf-8') as json_file:
    datas = json.load(json_file)

fields = (
    'product_name_fr', 
    'code', 
    'categories', 
    'nutriscore_grade', 
    'url', 
    'brands', 
    'stores' 
    )

datas_clean = {}

for n in range(len(datas['products'])):
    print("===========================")

    for field in fields:
        print(datas['products'][n][field].lower())
        datas_clean(field) = datas['products'][n][field].lower()


print(datas_clean)