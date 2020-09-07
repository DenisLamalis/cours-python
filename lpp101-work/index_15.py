# Lists

friends = ['John','Michael','Terry','Eric','Graham']
cars = [911,130,328,535,740,308]
# print(friends)

# friends.sort()
# print(friends)

# friends.sort(reverse=True)
# print(friends)

# friends.reverse()
# print(friends)

# print(min(friends))
# print(min(cars))

# print(max(cars))
# print(max(friends))

# print(sum(cars))

# friends.append('TerryG')
# friends.insert(1, 'TerryH')
# friends[2] = 'TerryI'
# friends.extend(cars)

# friends.remove('Terry')
# friends.pop()                 # delete the last one
# friends.pop(2)
# friends.clear()
# del friends
# del friends[2]

# new_friends = friends[:]
# new_friends = friends.copy()
new_friends = list(friends)

print(friends)
print(new_friends)
