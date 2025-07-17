vowels ="aeiou"

inp = input(("enter a word to find vowels :"))
vowels_count = 0
for char in inp:
    if char in vowels:
        vowels_count = vowels_count + 1
print(vowels_count)