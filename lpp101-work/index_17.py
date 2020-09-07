# Split and join

# msg ='Welcome to Python 101: Split and Join'
msg ='Welcome  to  Python  101: Split  and Join'
csv = 'Eric,John,Michael,Terry,Graham'
friends_list = ['Eric','John','Michael','Terry','Graham']

# print(list(msg))
# print(msg.split())
# print(msg.split(' '))
# print(msg.split(' '), type(msg.split(' ')))

# print(csv.split(','))

# print(str(friends_list))

# print('-'.join(friends_list))
# print('-'.join(friends_list + friends_list))
# print(''.join(friends_list))

print(''.join(msg.split()))
print(msg.replace(' ', ''))


