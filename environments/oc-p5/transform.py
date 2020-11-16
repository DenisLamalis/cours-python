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

    data_clean[data['products'][n][fields[0]].lower()] = {}

    # data_clean[data['products'][n]['product_name_fr'].lower()]['code'] = data['products'][n]['code'].lower()
    # data_clean[data['products'][n]['product_name_fr'].lower()]['categories'] = data['products'][n]['categories'].lower()
    # data_clean[data['products'][n]['product_name_fr'].lower()]['nutriscrore_grade'] = data['products'][n]['nutriscore_grade'].lower()
    # data_clean[data['products'][n]['product_name_fr'].lower()]['url'] = data['products'][n]['url'].lower()
    # data_clean[data['products'][n]['product_name_fr'].lower()]['brands'] = data['products'][n]['brands'].lower()
    # data_clean[data['products'][n]['product_name_fr'].lower()]['stores'] = data['products'][n]['stores'].lower()

    for field in fields:
        if field != fields[0]:
            data_clean[data['products'][n][fields[0]].lower()][field] = data['products'][n][field].lower()
        
 
with open('products_fr', 'w') as fp:
    json.dump(data_clean, fp)
