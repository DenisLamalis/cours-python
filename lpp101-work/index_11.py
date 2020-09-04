# find/replace, String formating

# msg="""Dear Terry,,
# You must cut down the mightiest 
# tree in the forest with…
# a herring! <3"""
# print(msg)

msg = 'Welcome to Python 101: Strings'

print(msg.find('h'))

print(msg.replace('Python', 'Java'))

msg1 = msg.replace('Python', 'Java')
print(msg1)

print('Python' in msg)
print('Python' not in msg)


#
# String Formating
#

name='TERRY'
color = 'RED'
msg = '[' + name + '] loves the color ' + color + '!'
msg1 = f'[{name.capitalize()}] loves the color {color.lower()}!'

print(msg)
print(msg1)
