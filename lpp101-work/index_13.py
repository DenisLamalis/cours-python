# User Input - Exercise

# - Create a distance converter converting Km to miles
# - Take two inputs from user: Their first name and the distance in km
# - Print: Greet user by name and show km, and mile values
# - 1 mile is 1.609 kilometers
# - hint: use correct types for calculating and print
# - Did you capitalize the name

fname = input('What is your first name ? ')
distance_km = input(f'{fname.title()}, what is the distance (in km)? ')

distance_miles = float(distance_km)/1.609

print(f'Greeting {fname.title()} ! distance in km : {distance_km} and in miles : {distance_miles}')

# Solution

# name = input('Enter your name: ')
# distance_km = input('Enter distance in km: ')
# distance_mi = float(distance_km)/1.609
# print(f'Hi {name.title()}! {distance_km}km is equivalent to {round(distance_mi, 1)} miles.')