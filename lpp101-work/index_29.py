# if elif else - exercise

# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs 
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f


# def calculation(num1, num2, operator):
#     if operator == '+':
#         result = num1 + num2
#     elif operator == '-':
#         result = num1 - num2
#     elif operator == '*':
#         result = num1 * num2
#     else:
#         result = num1 / num2
#     return result

# def asking():
#     num1 = input('Your first number: ')
#     num2 = input('Your second number: ')
#     operator = input('The operator (+, -, * or /): ')
#     # if operator != '+' or '-' or '*' or '/':
#     #     return
#     return num1, num2, operator

# informations = asking()

# num1 = int(informations[0])
# num2 = int(informations[1])
# operator = informations[2]
# result = calculation(num1, num2, operator)

# print('The result is : ' + str(result))

# Solution

mode = input('Enter math operation(+,-,*,/) or f for Celsius to Fahrenheit conversion: ')
num1 = float(input('Enter first number: '))
if mode.lower() == 'f':
    print(f'{num1} Celsius is equivalent to {(num1*9/5)+32 } fahrenheit')
else:
    num2 = float(input('Enter second number: '))

    if mode == '+':
        print(f'Answer is: {num1 + num2}')
    elif mode == '-':
        print(f'Answer is: {num1 - num2}')
    elif mode == '*':
        print(f'Answer is: {num1 * num2}')
    elif mode == '/':
        print(f'Answer is: {num1 / num2}')
    else:
        print('Input error!')