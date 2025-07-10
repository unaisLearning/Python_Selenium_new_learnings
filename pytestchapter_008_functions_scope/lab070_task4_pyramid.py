rows = 5
for i in range(1,rows + 1):
    spaces = " " * (rows - i)
    star = "*" * (2 * i - 1)
    print(spaces + star)