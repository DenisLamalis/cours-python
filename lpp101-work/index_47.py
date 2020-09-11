# Lambda functions part II


# def func(n):
#     return n                                # return a integer   
# print(type(func(3)))

# def func(n):
#     return lambda a: a*n                    # return a function  
# print(type(func(3)))

# def func(n):
#     return lambda a: a*n
# # a*2
# doubler = func(2)
# print(doubler(3))
# quintipler = func(5)
# print(quintipler(3))
# print(type(func(3)))

def price_calc(start,hourly_rate):
    return lambda hours: start + hourly_rate * hours
    
walkin_cost = price_calc(10,30)
premium_cost = price_calc(1,25)
print(walkin_cost(2))
print(premium_cost(2))

print(price_calc(1,25)(2))

print((lambda a,b,c: a+b+c)(2,3,4))
print((lambda a,b,c=2: a+b+c)(2,3,4))
print((lambda a,b,c=2: a+b+c)(2,c=3,b=4))
print((lambda *args: sum(args))(2,3,4))