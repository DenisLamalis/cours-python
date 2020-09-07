# Split and Join exercice


csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
friends_list = ['Exercise: fill me with names']
print(friends_list)

# From the list above fill a list(friends_list) properly
# with the names of all the friends. One per "slot"
# you may need to run same command several times
# use print() statements to work your way through the exercise

csv = csv.replace(':', ',')
csv = csv.replace(';', ',')

friends_list = csv.split(',')
print(friends_list)


# Solution

# csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
# print(','.join(csv.split(';')))
# print(','.join(csv.split(';')).split(':'))
# print(','.join(','.join(csv.split(';')).split(':')))
# print((','.join(','.join(csv.split(';')).split(':'))).split(','))
# friends_list = ['Exercise: fill me with names']
# print(friends_list)

# friends_list = (','.join(','.join(csv.split(';')).split(':'))).split(',')

# print('replace', csv.replace(';',',').replace(':',',').split(','))
friends_list = csv.replace(';',',').replace(':',',').split(',')
print(friends_list)