"""
Heirarchical Inheritance
One father and multiple child
"""

class Father:
    def car(self):
        print("Innova crysta")

class Son1(Father):
    pass

class Son2(Father):
    pass

class Son3(Father):
    pass

s1 = Son1()
s2 = Son2()
s3 = Son3()
s1.car()
s2.car()
s2.car()