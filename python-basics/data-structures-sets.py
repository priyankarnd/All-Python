#Sets

fruits = { "apple", "banana", "cherry"}

print(fruits)

#Access items
for x in fruits:
    print(x)

#Add one item
fruits.add("orange")

print(fruits)

#Adding multiple ietms
fruits.update(["mango","kiwi","strawberry"])

print(fruits)

#Number of elements in a set
print(len(fruits))

#remove an item
fruits.remove("kiwi")

print(fruits)

#use discard() to remove items. If the item does not exist, no wrror will be raised
fruits.discard("guava")

#empty the set
#fruits.clear()

print(fruits)

#join two sets-union
vegetables = {"carrots", "squash"}

produce = fruits.union(vegetables)

print(produce)

#produce2 = fruits.intersection(vegetables)

#update
#insert the items in set 2 into set 1

set1 = {"a", "b", "c", "d"}
set2 = {1, 2, 3}

set1.update(set2)

print(set1)

set1.pop()
print(set1)

set1.clear()
print(set1)

del set1

#both update and union will exclude duplicate items

#Frozen set - immutable

names = frozenset(["Jim", "John", "Mike"])

print(names)

#names.remove("Jim") #remove will throw error

#names.update({"Mary", "jane"}) #Cannot be updated





