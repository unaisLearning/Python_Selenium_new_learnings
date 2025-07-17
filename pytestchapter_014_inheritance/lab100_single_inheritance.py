#Inheritance

class Father():
    key = "1BHK"

    def car1(self):
        print(self.key)
        print("Innova Crysta")

class Child(Father):
    key2 = "villa"

    def car2(self):
        print(self.key2)
        print("BMW M4")



child_obj = Child()
child_obj.car2()
child_obj.car1() # here as child we can use father attributes and methds