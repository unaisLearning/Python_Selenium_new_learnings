#can  add a annotation to function for perform an additional action/task
#before and after of a particular function i need to do some task
#without changing actual code of function ,we can modify
#VERY IMPORTANT FOR API and REPORT generation

def login_wrap(func):
    def wrapper():
        print("start")
        func()
        print("end")
    return wrapper()

@login_wrap
def work():
    print("work")

@login_wrap
def breaking():
    print("break")