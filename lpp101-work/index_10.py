# Exercise - Strings-basics / slicing

msg='welcome to Python 101: Strings'

new_msg = msg[18] + ' ' + msg[0:7].title() + ' ' + msg[-5:-1].title() + ' ' + msg[8:10].title() + ' ' + msg[8].title() + msg[12] + msg[2] + msg[1] + msg[-5]

print(new_msg.title())

print(new_msg[::-1])