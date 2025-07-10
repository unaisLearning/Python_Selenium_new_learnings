"""
Tuple
unable to mutate or edit
use () to store
can append to tuple

"""
tuple_new = ("Hello", 1 , 2, 1)
print(tuple_new)

join_tuple = ((1,2,3),tuple_new)
print(join_tuple)

print(join_tuple[1])
print(join_tuple[0][1])
# Tuple can convert to other format easily

new_list = list(join_tuple)
print(new_list)
