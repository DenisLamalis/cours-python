# Return Statements

# def value_added_tax(amount):
#     tax = amount * 0.25
#     total_amount = amount * 1.25
#     return amount, tax, total_amount            # return a tuple
    
# price = value_added_tax(100)    
# print(price, type(price))


# def value_added_tax(amount):
#     tax = amount * 0.25
#     total_amount = amount * 1.25
#     return [amount, tax, total_amount]             # return a list
    
# price = value_added_tax(100)    
# print(price, type(price))


# def value_added_tax(amount):
#     tax = amount * 0.25
#     total_amount = amount * 1.25
#     return {amount, tax, total_amount}                # return a set
    
# price = value_added_tax(100)    
# print(price, type(price))


def value_added_tax(amount):
    tax = amount * 0.25
    total_amount = amount * 1.25
    return f'{amount}, {tax}, {total_amount}'           # return a string
    
price = value_added_tax(100)    
print(price, type(price))