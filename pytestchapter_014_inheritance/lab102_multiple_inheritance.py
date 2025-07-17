"""
Mutiple inheritance - one class inherit from two different classes
this feature npt available in JAVA but in python
"""
from functools import total_ordering


class Father:
    def father_money(self):
        return 50

class Mother:
    def mom_money(self):
        return 50

class Son(Father, Mother):
    def son_money(self):
        return 1050

s = Son()
money1 = s.mom_money()
money2 = s.father_money()
money3 = s.son_money()
total_money = money1 + money2 + money3
print("Total son net worth", total_money)