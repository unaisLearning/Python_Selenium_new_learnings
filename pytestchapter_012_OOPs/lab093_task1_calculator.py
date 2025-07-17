class calculator:
    def sum(self, a , b):
        return a + b
    def min(self, a, b):
        return a - b
    def mult(self, a, b):
        return a * b
    def div(self,  a, b):
        return a / b

object = calculator()
a = (float(input("first number")))
b = (float(input("second number")))

osum = object.sum(a, b)
omin = object.min(a, b)
omult = object.mult(a, b)
odiv = object.div(a ,b)

print(osum, omin, omult, odiv)

