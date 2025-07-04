#we can call a function inside a function

def function1():
    print("function hello")

def function2():
    function1()

function2()