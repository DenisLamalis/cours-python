import json

with open('off_products_fr.json', encoding='utf-8') as json_file:
    off_data = json.load(json_file)

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

for n in range(len(off_data['products'])):

    data_clean[off_data['products'][n][fields[0]].lower()] = {}
    print('clé pour ', data_clean[off_data['products'][n][fields[0]].lower()], 'crée.')

    for field in fields:
        if field != fields[0]:
            data_clean[off_data['products'][n][fields[0]].lower()][field] = off_data['products'][n][field].lower()
        
print("Nombre de produits en entrée :", len(off_data['products']))
print("Nombre de produits en sortie :", len(data_clean))

# Save the data in en json file
with open('my_products_fr.json', 'w') as fp:
    json.dump(data_clean, fp)


# Open the clean json file
with open('my_products_fr.json', encoding='utf-8') as json_file:
    my_products = json.load(json_file)



print(my_products.keys())
print('Nombre de produits : ', len(my_products))

for n in range(len(my_products)):

    pass