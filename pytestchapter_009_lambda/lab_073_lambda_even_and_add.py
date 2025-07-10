
n = int(input("Enter the number :"))
result = lambda n: "Even" if  n%2 == 0 else "Odd"
print(result(n))

# here actually we are doing:

def even_odd(n):
    if n % 2 ==0 :
        print("Even")
    else:
        print("Odd")
even_odd(n)