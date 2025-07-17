"""
Encapsulation basicily means we can prevent a variable or fuction access by someone from outside of the class
we can activate encapsulation/private by giving "--"(Double undrescore) before the variable name or function nanme
private variable or function can access inside from a class
outside of class need any access to private variable or function we need to call or print or use inside any of the public function

"""

class Bank:
    def __init__(self, debit_value, account_number):
        self.balance = 100 #public instance variable ,can access from outer class aswell
        self.__account_no = account_number # private instance variable, only can access inside class
        self.debit = debit_value
        self.name = "sss"


    def deposit(self):
        self.balance += self.debit

    def check_balance(self):
        print(self.balance)

    def check_account_number(self, auth):
        if auth:
            print(self.__account_no)
        else:
            print("not authorised for account number")

    def __private_function(self):  #this is a priate function , cant access from outside class
        print("Hello")

    def publi_function(self):
        self.publi_function()

sam = Bank(1000, 2323232323)
sam.deposit()
sam.check_balance()
print(sam.name)
#print(sam.__account_no) # we cant access the account no because its set as private
#we can access with the help of a private function
sam.check_account_number(True)



