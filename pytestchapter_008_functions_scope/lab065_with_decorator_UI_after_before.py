def ui_after_before(func):
    def wrapper():
        print("login")
        func()
        print("logout")
    return wrapper()

@ui_after_before
def ui_test():
    print("Ui actions")

@ui_after_before
def ui_test2():
    print("second ui actions")