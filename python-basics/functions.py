#Functions

#Defining a function

def helloWorld():
    print ("Hello from a function")

#Calling a function
helloWorld()

#Parameters
def greeting (firstName):
    print ("Hello " + firstName)

greeting("Justin")

# Random parameters

def fullGreeting (firstName, lastName):
    print("Hello " + firstName + " " + lastName)
    print("Hello {} {}".format(firstName,lastName))
    print("Hello {first} {last}".format(first=firstName, last=lastName))
    print("Hello {first} {last}".format(last=lastName, first=firstName))

fullGreeting("Priyankar", "Roychowdhury")

# Pass multiple values and access values by their index
def my_func2(*arg):
    print(arg[2])

my_func2("ABC", "PQR", "XYZ")


#Default parameter values
def default_greeting(firstName = "John"):
    print("Hi {}".format(firstName))

default_greeting()

default_greeting("Ross")

#passing a list as a parameter

def myFoodList (food):
    print(food)
    for item in food:
        print(item)

food = ["bread", "chicken", "fish"]

myFoodList(food)

#Returning values
def addition(num1, num2) :
    return num1 + num2

print(addition(10,20))

#Unknown number of parameters
def sum(*numbers) :
    result = 0
    for x in numbers:
        result += x
    return result

print(sum(10,25,35,67,100))

print(sum(30,20,25))

#Pass statement
def func():
    pass

func()

#Passing by Reference vs Passing value

'''
All parameters (arguments) are passed by reference in Python.
Changing what a parameter refers to within a function, will also change 
the original value passed in
'''

def changedVar (inputList) :
    inputList.append([1,2,3,4])
    print("Values changed inside the function : ", inputList)
    return

list = [10,20,30]
changedVar(list)

print("Values outside the function: ", list)

#Reference is overwritten
def overwrite (inputList):
    inputList = [1,2,3,4]  #this would assign a new reference to inputlist
    print("values inside the function: ", inputList)
    return

list = [10,20,30]
overwrite(list)

print("values outside the function: ", list)

#Recursion

#Factorial

'''
5! = 5 X 4 X 3 X 2 X 1
'''

def fact(num):
    result = 1
    while(num > 0):
        result *= num
        num -= 1
    return result

print(fact(5))

#defining a recursive function
def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n * recur_factorial(n-1)

print(recur_factorial(5))



