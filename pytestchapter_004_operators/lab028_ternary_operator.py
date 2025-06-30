#Ternary operator is a way to write if else condition in single line
# also called a condition operator
#it is not recommended because of the readbility issues. if else method is good

a , b = 10, 20

print("a is greater than b" if a>b else "B is greater")

x = int(input("Enter your age :"))
print("you are not eligible for vote" if x < 18 else "you are eligible for vote" )