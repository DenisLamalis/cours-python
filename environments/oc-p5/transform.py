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

    data_clean[data['products'][n]['product_name_fr'].lower()] = {}

    data_clean[data['products'][n]['product_name_fr'].lower()]['code'] = data['products'][n]['code'].lower()
    data_clean[data['products'][n]['product_name_fr'].lower()]['categories'] = data['products'][n]['categories'].lower()
    data_clean[data['products'][n]['product_name_fr'].lower()]['nutriscrore_grade'] = data['products'][n]['nutriscore_grade'].lower()
    data_clean[data['products'][n]['product_name_fr'].lower()]['url'] = data['products'][n]['url'].lower()
    data_clean[data['products'][n]['product_name_fr'].lower()]['brands'] = data['products'][n]['brands'].lower()
    data_clean[data['products'][n]['product_name_fr'].lower()]['stores'] = data['products'][n]['stores'].lower()

    # for field in fields:
    #     # print(field, data['products'][n][field].lower())

    #     if field == 'product_name_fr':
    #         tampon[data['products'][n][field].lower()] = {}
    #     else:
    #         pass


print(data_clean)