# while loops

print("1.*Loops are great*")
print("2.**Loops are great**")
print("3.***Loops are great***")
print("4.****Loops are great****")
print("5.*****Loops are great*****")


# while condition:
#     code
#     iterator

# Three Loop Questions:
#1. What do I want to repeat?
#  -> message
#2. What do I want to change each time?
#  -> stars
#3. How long should we repeat?
#  -> 5 times


# i=0
# while i < 5:
#     # print("Loops are awesome")
#     # print(f"{i}.*Loops are awesome*")
#     print(f"{i}." + "*"*i + "Loops are awesome" + "*"*i)
#     i=i+1

# i=1
# while i < 6:
#     # print("Loops are awesome")
#     # print(f"{i}.*Loops are awesome*")
#     print(f"{i}." + "*"*i + "Loops are awesome" + "*"*i)
#     i=i+1


i=0
while i < 5:
    i+=1
    print(f"{i}." + "*"*i + "Loops are awesome" + "*"*i)
