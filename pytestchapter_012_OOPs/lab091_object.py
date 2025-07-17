
class dog():

#Attributes | Data variables | Instance structures | Data variables
    breed : None
    height : 100
    # name : None
#behaviors
    def __init__(self, name, breed):
        print("New Dog")
        self.name = name
        self.breed = breed

    def sleeper(self):
        print("sleeping", self.name)

husky = dog("kaiser", "husky")
mixed = dog("mixed", "boxer")
print(husky.name, husky.breed)
print(mixed.name, mixed.breed)
print(id(mixed))
print(id(husky))
husky.sleeper()
print
