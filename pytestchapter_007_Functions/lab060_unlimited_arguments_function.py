# *args -> act as we can give unlimited argument
# *args store in a list , we should take it by one by one.

def unlimited_args(*args):
    print(*args)
    for i in args:
        print(i)


unlimited_args("Hello","sam", "first")
