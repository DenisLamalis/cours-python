# functions - named notation

#1. Comment your code...and explain what it does

# def greeting(name, age=28, color="red"):
#  #Greets user with “name” from “input box” and “age”, if unavailable, default age is used   
   
#    print(f"Hello {name.capitalize()}, you will be {age+1} next birthday!")
#    print(f"We hear you like the color {color.lower()}!")

# greeting("brian", 27,"Blue")


def greeting(name, age=28, color="red"):
 #Greets user with “name” from “input box” and “age”, if unavailable, default age is used   
   
   print(f"Hello {name.capitalize()}, you will be {age+1} next birthday!")
   print(f"We hear you like the color {color.lower()}!")

greeting(age=27, name="brian",color="Blue")
