import random

l = [1,3,5,7,11,23,56]

length = len(l)
print(length)

r = random.randint(0,length-1)
print(r)

print("A randomly picked number from the list is:",l[r])



