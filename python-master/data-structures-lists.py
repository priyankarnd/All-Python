#Lists

#define a list

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

# length
print(len(fruits))


#access element from the list
print(fruits[1])

#negative indexing
#get last element from list
print(fruits[-1])

#get the second to last element from the list
print(fruits[-2])

#count of number of items in a list
print(fruits.count('apple'))

print(fruits.count('tangerine'))

#index of where an item appears
print(fruits.index('banana'))

print(fruits.index('banana',4)) # Find index of next banana starting at position 4

#reverse the order of the elements in the list
fruits.reverse()

print(fruits)

print(fruits[::-1])

# print(fruits)

#add an item to the end of the list
fruits.append('grape')

print(fruits)

#insert an item at a specific index
fruits.insert(3, 'mango')

print(fruits)

#sort alphabetically
fruits.sort()

print(fruits)

#remove the last list list item
fruits.pop()

print(fruits)

#loop over list
for x in fruits:
    print(x)


#check if an item is in the list
if "apple" in fruits:
    print("Yes, apple is in fruit list")


#slicing a list
print(fruits)

print(fruits[3:6]) #start at index 3 and include up to index 5, excluding 6

#print from index 4 till the end
print(fruits[4:])

#negative indexing
#start from the 4th element from the right and go the 3rd element from the right
print(fruits[-4:-2])

#remove items

print(fruits)

fruits.remove("kiwi")
fruits.remove("banana") #removes first banana

print(fruits)

# replace multiple
fruits[1:3] = ["strawberry", "pear"]
print(fruits)

# extend
veg = ["tomatoes", "cabbage", "cauliflower"]
fruits.extend(veg)
print(fruits)

meat = ("chicken", "lamb")
fruits.extend(meat)
print(fruits)

# Pop by position
fruits.pop(3)
print(fruits)

# lambda function

[print(x) for x in fruits]

x = [item for item in fruits]
print(x)

# copy the list
combo = fruits.copy()
print(combo)

# clear elements of list
fruits.clear()
print(fruits)

# delete list
del(fruits)
print(fruits)










