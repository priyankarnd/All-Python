#from os import close, read
import os

if os.path.exists("fibonacci.txt"):
    os.remove("fibonacci.txt")
else:
    print("No such file exits")

# Length of the series user input
n = int(input("Enter the length of the series: "))

#print(n)

a = 0 # The starting numbers
b = 1

#Check if n is negative or zero
if n<0:
    print("Length should be positive")
elif n == 0:
    print("No numbers in series")
else:
    f = open("fibonacci.txt","a")
    print("The series is : \n")
    print(a)
    f.write(str(a))
    f.write("\n")
    print(b)
    f.write(str(b))
    f.write("\n")
    for i in range(0,n-2):
        c = a + b
        a = b
        b = c
        print(b)
        f.write(str(b))
        f.write("\n")
    f.close()




    