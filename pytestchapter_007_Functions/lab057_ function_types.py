#4 types of function
# 1 - Function without argument/parameter no return
# 2- Function No return  with argument/parameter
#3 - Function with return
#4 Function not return anything

#1 Function without argument/parameter no return

def greet():
    print("hello")

greet()

#Function No return  with argument/parameter
def greetings(name1 , name2):
    print("Hello", name1, name2)

greetings("sam","alex")

#3 - Function with  default argument and no return

def names(name = "sam"):
    print("Hello,", name)

names("alex")
names()

#4 Function with argument and return
def addition(num1 = 12, num2 = 13):
    return num1 + num2

result = addition()
print(result)
result =addition(10,20)
print(result)
result =addition(10)
print(result)
result =addition(num2=20)
print(result)
result =addition(num1=1)
print(result)
