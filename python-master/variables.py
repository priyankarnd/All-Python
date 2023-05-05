#Variables in Python

x = 10

y = 5.5

name = "Bappa"

print(x)

print(y)

print(name)

x = 6.5

name = "Sonia"

print(x)
print(name)


#Assigning a value to multiple variables

fruit1, fruit2, fruit3 = "apple", "orange", "banana"

print(fruit1)
print(fruit2)
print(fruit3)


#Output variables

name = "PR"

print("Hello " + name)


#Global variables

x = 20

def addition():
    #Local variables
    x = 10 + 30
    print(x)

addition() #Local

print(x)  #Global

y = 10

def substraction():
    #Global variables
    global y
    y = 40 - 20
    print(y)

substraction()

print(y)







