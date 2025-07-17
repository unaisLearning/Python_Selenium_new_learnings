#remove duplicate value from dictionary

my_dict = {"a" : 1, "b":2, "c":3, "d":1}


unique_values = set()
result = {}
for key,value in my_dict.items():
    if value not in unique_values:
        result[key] = value
        unique_values.add(value)
print(result)


