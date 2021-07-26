import operator
import random

#Input the string
print("Enter a string: ")
s = input()
print(s)

#Find out the length of the string
length = len(s)
print(f'The length of the string is: {length}')

#less than 5 letters
if (length < 5):
    print(s)
elif (length >= 5 and length < 8):
    r = random.randint(1,10)
    print(f'Random integer is: {r}')
    if (r% 2 == 0):
        print(s.upper())
    else:
        print("Go Irish!")
else:
    if operator.contains(s, "R"):
        print("This long word has the letter R")
    else:
        print("This long word does not have the letter R")



