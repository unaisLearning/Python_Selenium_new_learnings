
class GrandFather:
    hello = "Helloo"
    def money(self):
        print("40")

class Father(GrandFather):
    def moneyy(self):
        print("50")

class Son(Father):
    def moneyyy(self):
        print(1000)

s = Son()
s.moneyy()
s.money()
s.moneyyy()
print(s.hello)

