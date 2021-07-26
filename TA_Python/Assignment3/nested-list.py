import random

mainlist = [] #Masterlist

#Sub-lists
list = []



for x in range(0,5):
    for y in range(0,5):
        a = random.randint(1, 100)
        # print(a)
        list.append(a)
        # print(list)
    mainlist.append(list)
    list = []
#     print(mainlist)
#
print(mainlist)
#
# print(mainlist[2][3])

for x in mainlist:
    for y in range(0,5):
        print(x[y])
        if ( x[y] > 50):
            x[y] = 0



for x in mainlist:
    # print(x)
    print(*x, sep=' ')















