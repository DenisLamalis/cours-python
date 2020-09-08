# Conditionals: if, else, elif

# is_raining = True
# print('Good morning!')

# if is_raining:
#     print('Bring umbrella')


# is_raining = False
# print('Good morning!')

# if is_raining:
#     print('Bring umbrella')
# else:
#     print('Umbrella is optional')


# is_raining = True
# is_cold = True
# print("Good Morning")
# if is_raining or is_cold:                           # or
#     print("Bring Umbrella or jacket or both")
# else:
#     print("Umbrella is optional")


# is_raining = True
# is_cold = False
# print("Good Morning")
# if is_raining and is_cold:                           # and
#     print("Bring Umbrella and jacket")
# else:
#     print("Umbrella is optional")


# is_raining = False
# is_cold = True
# print("Good Morning")
# if is_raining and is_cold:
#     print("Bring Umbrella and jacket")
# elif is_raining and not(is_cold):                       # and not()
#     print("Bring Umbrella")
# elif not(is_raining) and is_cold:
#     print("Bring Jacket")
# else:
#     print("Shirt is fine!")


amount = 10
if amount <= 50:
    print("Purchase approved")
else:
    print("Please enter your pin!")