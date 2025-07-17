"""
Data with env
install pip package
pip install python-dotenv
import os and env
create .env folder and add credential
dont push env to git as its our secret password

"""
import os
import dotenv
from dotenv import load_dotenv

load_dotenv()
class Abstract:
    def __init__(self, username, password_arg):
        self.name = username
        self.password = password_arg

    def confirm_cred(self):
        if self.name == os.getenv("Email") and self.password == os.getenv("password"):
            print("you are succesfully log in")
        else:
            print("login failed")
        print(self.name, self.password)

name = input("Enter username : ")
password = input("Enter password : ")

cred1 = Abstract(name, password)
cred1.confirm_cred()
