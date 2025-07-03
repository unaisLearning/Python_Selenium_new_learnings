#pass just simply skip and do nothing
#continue saying skip from this line and do it again untill condition meets

for i in range(10):
    if i == 7:
        pass
        print(i) #this will print because pass only skips



for i in range(10):
    if i == 6:
        continue
        print(i) #this will not print because its skip and continue  from the top of the loop.