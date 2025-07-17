#missing

dict1 = {"a" : 1, "b" : 2}
dict2 = {"a" : 1, "b" : 2, "c":3}

missing_keys = set(dict2.keys()) - set(dict1.keys())
print(missing_keys)