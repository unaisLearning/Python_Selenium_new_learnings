#Count how many times each character appears in a given string

dict = {}
string = input("input a string: ")
for char in string:
    dict[char] = dict.get(char, 0)+1

print(dict)