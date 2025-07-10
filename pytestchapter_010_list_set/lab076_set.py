"""
most commenlt using
set in {}
No duplicates

"""
new_set = {3,4,5,6,5}
print(new_set)

lister = [3,3,4,4,5,10,20,30]
set_changer = set(lister)
print(set_changer)

united = new_set.union(set_changer)
print(united)

inter = new_set.intersection(set_changer) # print common values
print(inter)

differ = new_set.difference(set_changer) #items in new_Set but not in set_changer
print(differ)

differ = set_changer.difference(new_set) #set_changer but not in new_set
print(differ)