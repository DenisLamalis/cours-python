# User Input - Exercise

fname = input('What is your first name ? ')
distance_km = input(f'{fname.title()}, what is the distance (in km)? ')

distance_miles = float(distance_km) / 1.609

print(f'Greeting {fname.title()} ! distance in km : {distance_km} and in miles : {distance_miles}')