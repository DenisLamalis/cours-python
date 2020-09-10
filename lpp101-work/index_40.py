# Dictionaries - exercise part 2



#create stores
freelancers = {'name':'freelancing Shop','brian': 70, 'black knight':20, 'biccus diccus':100, 'grim reaper':500, 'minstrel':-15}
antiques = {'name':'Antique Shop','french castle':400, 'wooden grail':3, 'scythe':150, 'catapult':75, 'german joke':5}
pet_shop = {'name':'Pet Shop','blue parrot':10, 'white rabbit':5, 'newt': 2}

# ###
# # Etape 0
# ###
# #create an dempty shopping cart
# cart = {}
# #loop through stores/dicts
# for shop in (freelancers,antiques,pet_shop) :
#     #inputbox  to show what you can buy...capture textstring of what was bought...make lowercase
#     buy_item = input(f'Welcome to {shop["name"]}! what do you want to buy: {shop}').lower()
#     #update the cart
#     cart.update({buy_item:shop.pop(buy_item)}) # use pop...
#     buy_items = ", ".join(list(cart.keys()))
# print(f'You Purchased {buy_items}. Today it is all free. Have a nice day of mayhem!')


# ###
# # Etape 1
# ###
# #create an dempty shopping cart
# cart = {}
# #create purse with 100Gp
# purse = 1000
# #loop through stores/dicts
# for shop in (freelancers,antiques,pet_shop) :
#     #inputbox  to show what you can buy...capture textstring of what was bought...make lowercase
#     buy_item = input(f'Welcome to {shop["name"]}! (type exit to exit store) what do you want to buy: {shop}').lower()
#     #exit on exit typed or buying nonexistant item
#     if buy_item == 'exit':
#         continue
#     if buy_item not in shop:
#         continue
        
#     #update the cart
#     cart.update({buy_item:shop.pop(buy_item)}) # use pop...
#     buy_items = ", ".join(list(cart.keys()))
# print(f'You Purchased {buy_items}. Your total is {sum(cart.values())} Gp. Your change is {purse - sum(cart.values())} Gp. Have a nice day of mayhem!')


# # ###
# # # Etape 2
# # ###
# #create an dempty shopping cart
# cart = {}
# #create purse with 100Gp
# purse = 1000
# buy_items1 = ''
# #loop through stores/dicts
# for shop in (freelancers,antiques,pet_shop) :
#     #inputbox  to show what you can buy...capture textstring of what was bought...make lowercase
#     buy_item = input(f'Welcome to {shop["name"]}! (type exit to exit store) what do you want to buy: {shop}').lower()
#     #exit on exit typed or buying nonexistant item
#     if buy_item == 'exit':
#         continue
#     if buy_item not in shop:
#         continue
#     #update string
#     buy_items1 = buy_items1 + f'{buy_item}:{shop[buy_item]} Gp, '    
#     #update the cart
#     cart.update({buy_item:shop.pop(buy_item)}) # use pop...
#     buy_items = ", ".join(list(cart.keys()))
#     total_sum = sum(cart.values())
# print(f'You Purchased {buy_items}. Your total is {total_sum} Gp. Your change is {purse - total_sum} Gp. Have a nice day of mayhem!')
# print(f'You Purchased {buy_items1}. Your total is {total_sum} Gp. Your change is {purse - total_sum} Gp. Have a nice day of mayhem!')


# ###
# # Etape 3
# ###
# #morning inventory
# department_store = {}
# for department in (freelancers, antiques, pet_shop) :department_store.update(department)
# print('Morning inventory of stores', sorted(department_store.items()))
# print('-----------------')
# #create an dempty shopping cart
# cart = {}
# #create purse with 100Gp
# purse = 1000
# buy_items1 = ''
# #loop through stores/dicts
# for shop in (freelancers,antiques,pet_shop) :
#     #inputbox  to show what you can buy...capture textstring of what was bought...make lowercase
#     buy_item = input(f'Welcome to {shop["name"]}! (type exit to exit store) what do you want to buy: {shop}').lower()
#     #exit on exit typed or buying nonexistant item
#     if buy_item == 'exit':
#         continue
#     if buy_item not in shop:
#         continue
#     #update string
#     buy_items1 = buy_items1 + f'{buy_item}:{shop[buy_item]} Gp, '    
#     #update the cart
#     cart.update({buy_item:shop.pop(buy_item)}) # use pop...
#     buy_items = ", ".join(list(cart.keys()))
#     total_sum = sum(cart.values())
# print(f'You Purchased {buy_items}. Your total is {total_sum} Gp. Your change is {purse - total_sum} Gp. Have a nice day of mayhem!')
# print(f'You Purchased {buy_items1}. Your total is {total_sum} Gp. Your change is {purse - total_sum} Gp. Have a nice day of mayhem!')
# #evening inventory
# department_store_after = {**freelancers, **antiques, **pet_shop} #pyth 3.5
# print('-----------------')
# print('Morning inventory of stores', sorted(department_store_after.items()))


###
# Etape 4
###
#morning inventory
department_store = {}
for department in (freelancers, antiques, pet_shop) :department_store.update(department)
department_store.pop('name')
print('Morning inventory of stores', sorted(department_store.items()))
print('-----------------')
#create an dempty shopping cart
cart = {}
#create purse with 100Gp
purse = 1000
buy_items1 = ''
#loop through stores/dicts
for shop in (freelancers,antiques,pet_shop) :
    #inputbox  to show what you can buy...capture textstring of what was bought...make lowercase
    buy_item = input(f'Welcome to {shop["name"]}! (type exit to exit store) what do you want to buy: {shop}').lower()
    #exit on exit typed or buying nonexistant item
    if buy_item == 'exit':
        continue
    if buy_item not in shop:
        continue
    #update string
    buy_items1 = buy_items1 + f'{buy_item}:{shop[buy_item]} Gp, '    
    #update the cart
    cart.update({buy_item:shop.pop(buy_item)}) # use pop...
    buy_items = ", ".join(list(cart.keys()))
    total_sum = sum(cart.values())
print(f'You Purchased {buy_items}. Your total is {total_sum} Gp. Your change is {purse - total_sum} Gp. Have a nice day of mayhem!')
print(f'You Purchased {buy_items1}. Your total is {total_sum} Gp. Your change is {purse - total_sum} Gp. Have a nice day of mayhem!')
#evening inventory
department_store_after = {**freelancers, **antiques, **pet_shop} #pyth 3.5
department_store_after.pop('name')
print('-----------------')
print('Evening inventory of stores', sorted(department_store_after.items()))


