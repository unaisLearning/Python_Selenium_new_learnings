#basically we are using unlimited arguments because there must be
# requirement like unlimited arguments , so if we give any specifc parameters
# it can only take that number of arguments.

def pizza(*toppins):
    for i in toppins:
        print(i)

rahul = pizza("tomato", "chili", "pummin")
sam = pizza("tomato")
khuraishi = pizza(123, "hello")