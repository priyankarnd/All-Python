import random

import math

# value = int(input("PLease enter a number : ") or "42")
#
# print(value)


def generate_dart_throws(path,n):
    with open("data2.txt", "w+") as data:
        n = int(input("PLease enter a number : ") or "10")
        print(f'Number of throws is: {n}')
        while ( n > 0 ):
            posx = random.randrange(-3,3)
            posy = random.randrange(-3,3)
            pos = math.sqrt(posx ** 2 + posy ** 2)
            if (pos <= 1):
                points = 3
            elif (pos > 1 and pos <= 2):
                points = 2
            elif (pos > 2 and pos <= 3):
                points = 1
            else:
                points = 0
            print(f'dart_point_value : {points}')
            data.write(str(posx) + " " + str(posy) + " " + str(points) + "\n")
            n -= 1
        data.close()

path = "/Users/bappamac/TA_Python/Assignment5"

generate_dart_throws(path,1)


