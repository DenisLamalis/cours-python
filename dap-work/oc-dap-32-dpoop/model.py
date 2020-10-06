
class Agent:
    """ """

    def __init__(self, agreeableness):
        self.agreeableness = agreeableness
    
    def say_hello(self, first_name):
        return "Bien le bonjour " + first_name + " !"


# # valider que c'est un objet de Agent
# first_agent = Agent()
# print(first_agent)

# Ajouter une méthode
agent = Agent(10)
print(agent.say_hello("Céline"))

# Ajouter un attribut
print(agent.agreeableness)

