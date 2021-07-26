import random

num = 0    #Total number of integers

div3 = 0   #Total number of integers divisible by 3

newlist = []  # A blank list

while ( div3 < 10 ):
    r = random.randint(1, 100)  #generate random integer
    num += 1

    if (r % 3 == 0):
        div3 += 1
        newlist.append(r)

else:
    print(f'The total number of integers generated is: {num}')
    print("The list of integers divisible by 3:")
    print(newlist)



