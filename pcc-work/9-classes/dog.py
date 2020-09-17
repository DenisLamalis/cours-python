class Dog:
    """ a simple attempt to model a dog """

    def __init__(self, name, age):
        """ initialize name and age attributes """

        self.name = name
        self.age = age

    def sit(self):
        """ simulate a dog stting in response to a command """

        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """ simulate rolling over in response to a command """

        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog's is {my_dog.age} years old.")
