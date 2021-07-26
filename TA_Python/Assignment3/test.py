numList = [1,2,4,3,1,3,2,4]

mySet = set()

for item in numList:
    mySet.add(item)

mySet.remove(2)
mySet.add(0)

print(mySet)