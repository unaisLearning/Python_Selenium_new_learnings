#outer function variable can accessible from inner function

def outer_function():
    a=45
    def inner_function():
        print(a)
        b=15
    def inner_function2():
        print(a)
    inner_function()
    inner_function2()
outer_function()
