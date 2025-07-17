class Home:
    def __init__(self):
        self.public_var = "father"
        self.__private_var = "child"

    def mom(self):
        print(self.__private_var)
        print(self.public_var)
        self.__wife()


    def __wife(self):
        print("iam wife")

outsider = Home()

print(outsider.public_var)
#print(outsider.__private_var)#unable to access
outsider.mom()
#outsider.__wife() #unable to access from outer class