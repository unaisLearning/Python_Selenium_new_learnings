
class person:
    def __init__(self):
        self.name = input("Enter your name")
        self.age = input("Enter your age")
        self.place = input("Enter your place")

    def person_details(self):
        print(self.name, self.age, self.place)

person1 = person() #object
person1.person_details() #object
