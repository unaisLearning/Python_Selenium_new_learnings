class calc:
    def __init__(self, a ,b):
            self.a = a
            self.b = b

    def add(self):
        return self.a + self.b

    def min(self):
        return self.a - self.b

    def mult(self):
        return self.a * self.b

obj1 = calc(10, 20)

sum_output = obj1.add()
print(sum_output)

mult_output = obj1.mult()
print(mult_output)

min_output = obj1.min()
print(min_output)

