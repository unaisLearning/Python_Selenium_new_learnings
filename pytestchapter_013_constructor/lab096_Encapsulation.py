"""
Encapsulation
we take all the needed variables and functions in a single class and call only needed items
Bind the data variables inside methods
Wrapping or binding the data variables with the methods
"""

class Abstract:
    def __init__(self, username, password_arg):
        self.name = username
        self.password = password_arg

    def confirm_cred(self):
        if self.name == "Hello" and self.password == "12345":
            print("you are succesfully log in")
        else:
            print("login failed")

name = input("Enter username : ")
password = input("Enter password : ")

cred1 = Abstract(name, password)
cred1.confirm_cred()
