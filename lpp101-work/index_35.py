# Enumerate this!

# print('python101 - Enumerate')
# friends = ['Brian', 'Judith', 'Reg', 'Loretta', 'Colin']

# i = 0
# for friend in friends:
#     print(i, friend)
#     i = i +1 # += 1


# for num, friend in enumerate(friends,1):
#     print(num, friend)


# friends = ['Brian', 'Judith', 'Reg', 'Loretta', 'Colin']
# efriends = [(51,'Brian'), (52,'Judith'), (53,'Reg'), (54,'Loretta'), (55,'Colin')]

#i = 51
#for friend in friends:
#    print(i, friend)
#    i = i +1 # += 1
# for num, friend in enumerate(friends,51):
#     print(num, friend)
    
# print(type(enumerate(friends)))
# print(list(enumerate(friends)))


# for num, friend in enumerate(friends,51):
#     print(num, friend)

# for friend in enumerate(friends,51):
#     print(friend)

# for friend in enumerate(enumerate(friends,51),-100):
#     print(friend)

# print(type(enumerate(friends)))
# print(list(enumerate(friends)))

for num, letter in enumerate('python',start = 5):
    print(num, letter)

for letter in enumerate('python'):
    print(letter)


