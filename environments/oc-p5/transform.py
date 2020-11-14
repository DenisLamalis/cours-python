import json

with open('off_products_fr.json', encoding='utf-8') as json_file:
    datas = json.load(json_file)

# for n in range(len(datas['products'])):
#     print("===========================")
#     print(datas['products'][n]['product_name_fr'])
#     print(datas['products'][n]['code'])
#     print(datas['products'][n]['categories'])
#     print(datas['products'][n]['nutriscore_grade'])
#     print(datas['products'][n]['url'])
#     print(datas['products'][n]['brands'])
#     print(datas['products'][n]['purchase_places'])
#     print(datas['products'][n]['stores'])

# print(len(datas['products']))


fields = (
    'product_name_fr', 
    'code', 
    'categories', 
    'nutriscore_grade', 
    'url', 
    'brands', 
    'stores' 
    )

for n in range(len(datas['products'])):
    print("===========================")

    for field in fields:
        print(datas['products'][n][field].lower())




#