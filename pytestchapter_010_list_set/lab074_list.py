"""
List:
its a set of data
duplicated data is allowedits mutable/editable 
multiple data types are included
space allocation start from 0

"""
List = ["abc", 1, 3, 1.43, True]

print(List)
print(List[3])
print(len(List))
List[4] = "Hello"
print(List)

print("-----")

for i in List:
    print(i, end=" ")
print("Length", len(List))

#append - Add a value at end

List.append("new append")
print(List)
print("Length", len(List))

#extend - add a list with current list
new_list = [1, 2, 3]
List.extend(new_list)
print("Length", len(List))

#insert - insert  a value by saying index
List.insert(1 , "inserted")
print(List)
print("Length", len(List))
#remove

List.remove("Hello")
print(List)

#copy
copy = List.copy()
print("Copy = ",copy)

#sort
new_list = [31 ,52,23,34,5]
new_list.sort()
print(new_list)