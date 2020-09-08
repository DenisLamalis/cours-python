# Functions - calling, parameters, arguments, defaults

# def greeting():                   # declaration
#     print('Hello friend !')

# greeting()                        # call


# def greeting(name):                 # with argument
#     print(f'Hello {name} !')

# greeting('toto')


# def greeting(name, age):                 # with several argument
#     print(f'Hello {name}, you are {age} !')

# greeting('toto', 46)


# def greeting(name, age="28"):                 # with default value
#     print(f'Hello {name}, you are {age} !')

# greeting('toto')


# def greeting(name,age="28"):
#     print("Hello " + name + ", you are " + age + "!")
#     print(f"Hello {name}, you are {age}!")

# name = input('Enter your name: ')
# greeting(name,"32")
# greeting("Judith")


def greeting(name,age=28):
    print("Hello " + name + ", you are " + str(age) + "!")
    print(f"Hello {name}, you are {age}!")

name = input("Enter your name: ")    
greeting(name,32)
greeting("Judith")
