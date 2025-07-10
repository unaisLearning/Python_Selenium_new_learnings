# Find the first non-repeating character in a string using sets.
# swiss →> 5-x, W-Anwser


def first_non_repeat(string):
    for char in string:
        if string.count(char) == 1:
            return char
    return None

print(first_non_repeat("swiss"))