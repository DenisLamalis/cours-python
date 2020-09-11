# Lambda functions (anonymous function)

# def square(x):
#     return x*x

# print(square(3))

# #name = lambda parameter(s): expression
# square1 = lambda x: x*x
# print(square1(3))

# def square2(x):return x*x
# print(square2(3))

# double_mult = lambda x,y: 2*x*y
# print(double_mult(2,3))


# def name_and_alias(name,alias):
#     return name.strip().title() + ':' + alias.strip().title()
# name_and_alias1 = lambda name,alias:name.strip().title() + ':' + alias.strip().title()
# def name_and_alias2(name,alias):return name.strip().title() + ':' + alias.strip().title()

# print(name_and_alias(' john  ClEEse  ','HECKLER'))
# print(name_and_alias1(' john  ClEEse  ','HECKLER'))
# print(name_and_alias2(' john  ClEEse  ','HECKLER'))


monty_python = ['John Marwood Cleese','Eric Idle','Michael Edward Palin','Terrence Vance Gilliam','Terry Graham Perry Jones', 'Graham Arthur Chapman']

def sort_names(name):
    return name.split(' ')
monty_python.sort(key = lambda name:name.split(' ')[-1])
print(monty_python)
monty_python.sort(key= sort_names)
print(monty_python)
