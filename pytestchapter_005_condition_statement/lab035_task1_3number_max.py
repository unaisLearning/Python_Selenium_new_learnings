# find max of 3 numbers

#Logic building formule
#step 1 -> input and output
# input 3 numbers -> float
# output - string

#step 2 -> rough logic
# num 1 > num2 and num3 -> num1 is max
# num2 > num 1 and num3 -> num2 is max
# num3 > num1 and num 2 -> num3 is max


#step 3 -> start code
num1 = int(input("Enter number 1 :"))
num2 = int(input("Enter number 2 :"))
num3 = int(input("Enter number 3 :"))

if num1 > num2 and num1 > num3:
    print(f"{num1} is greater")
elif num2 > num3:
    print(f"{num2} is greater")
else:
    print(f"{num3} is greater")

#step 4 ->Edge cases

#step 5 -> optimise code
