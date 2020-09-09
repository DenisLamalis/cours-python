# while loops - exercise

# Guess the correct number in 3 guesses. If you don’t get it right after 3 guesses you lose the game. 
# Give user input box: 1. To capture guesses, 
# print(and input boxes) 1. If user wins 2. If user loses
# Tip:( remember you won’t see  print statements durng execution, so If you want to see prints during whle loop, then print to the input box

#Modification 1: number 1-100, tell user if guess is too high/low ,and let them have 5-10 guesses.
# Tip:( remember you won’t see  print statements during execution, so If you want to see prints during whle loop, print to the input box (This is specific to this platform)

# Three Loop Questions:
#1. What do I want to repeat?
#  -> 
#2. What do I want to change each time?
#  -> 
#3. How long should we repeat?
#  -> 

# input a number
# afficher si la réponse est bonne
# afficher si la répopnse est fausse

answer = ''
number = 90
nb_guesses = 10
i = 0

while i < nb_guesses:
    answer = input(f'Try {i+1} ({nb_guesses-(i+1)}) tries left, give a number: ')
    
    i = i + 1

    if answer != str(number):
        if int(answer) > number:
            print("\nIncorrect, it's to high\n")
        elif int(answer) < number:
            print("\nIncorrect, it's to low\n")

    elif answer == str(number):
        print('\nYou win!\n')
        break

print('End of the game')


# Solution

# num = 12
# guess = 0
# guess_limit = 3
# guess_number = 0

# while guess_number < guess_limit:
#     guess = int(input(f'Guess # {guess_number+1} a number 1-20: last guess:{guess} '))
#     if guess == num:
#         print(f'You Win! You Guessed it: {guess}')
#         break
#     else:
#         print(f'No, not {guess}!')
#         guess_number += 1
# if guess != num:
#     print(f'Sorry you lose! It was {num}')


# num = 76
# guess = 0
# guess_limit=5
# guess_number = 0

# guess = int(input(f'Guess a number 1-100: '))
# guess_number +=1

# while guess_number < guess_limit:
    
#     if guess != num:
#         guess_number +=1
#         if guess > num:
#             guess = int(input(f'{guess} Too high - Guess again 1-100: '))
#         else:
#             guess = int(input(f'{guess} too low - Guess again 1-100: '))
#     if guess == num:
#         print(f'You Win! You Guessed it: {guess}')
#         break
    
# if guess != num:
#     print(f'Sorry you lose! It was {num}')