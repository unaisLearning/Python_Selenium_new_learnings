a = 10 #global

class Abc:
    b = 20 # instance varialbe

    def print_info(self):
        c = 20 # this is local variable
        print(c) #no need of self for local variable
        print(self.b) # need self for instance variable

abcd = Abc()
abcd.print_info()