import random

newlist = []

for i in range(0 ,20):
    r = random.randint(1, 50)
    newlist.append(r)

print(newlist)

sum = 0

for i in range(0, 20):
    sum = sum + newlist[i]

print(sum)





