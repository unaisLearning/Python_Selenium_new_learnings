#2 types of variables
# 1- Global
# 2 - Local

a = 13 #this is global can access from anywhere
c=15
def scope():
    b=23 # local variable , only can access inside the function
    a=12 # inside now a will be 12 outside will be 13 by taking from global
    print(c) #here we can access global variable aswell
    print(a)
scope()
print(a)

