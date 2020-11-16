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

    data_clean[off_data['products'][n][fields[1]].lower()] = {}

    for field in fields:
        if field != fields[1]:
            data_clean[off_data['products'][n][fields[1]].lower()][field] = off_data['products'][n][field].lower()

# Check input vs output
if len(off_data['products']) == len(data_clean):
    print("Nettoyage OK. Il y a", len(off_data['products']), "input pour", len(data_clean), "output.")
    with open('my_products_fr.json', 'w') as fp:
        json.dump(data_clean, fp)
    print("Création du fichier : OK")
else:
    print("Nettoyage KO. Il y a", len(off_data['products']), "input pour", len(data_clean), "output.")
    print("Création du fichier : KO")


###########

# # Save the data in en json file
# with open('my_products_fr.json', 'w') as fp:
#     json.dump(data_clean, fp)


# Open the clean json file
# with open('my_products_fr.json', encoding='utf-8') as json_file:
#     my_products = json.load(json_file)


# for n in range(len(my_products)):
#     pass