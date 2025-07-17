"""
Dictionary:
collection of key and value
its unordered, mutable, and indexed, collection of key and value
syntax:
dict = {"set":"value"}
"""
person = {"name" : "alex",
          "place" : "newyork",
          "age" : 44}

#accessing data
print(person["name"])
print(person)

#editing data
person["name"] = "sam"
print(person)

#delete data
del person["age"]
print(person)

#Iterate data
for key, value in person.items():
    print(key, ":::", value)

#Existance check
print("age" in person)
print("name" in person)
