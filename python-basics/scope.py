def myf():
    x = 100
    print(x)

myf()

def myf1():
    x = 200
    def myinner():
        print(x)
    myinner()

myf1()

x = 500   # global scope
def myf2():
    print(x)

myf2()

print(x)

def myf4():
    x = 600     # local scope
    print(x)

myf4()
print(x)

def myf5():
    global y
    y = 10
    print(y)

myf5()
print(y)






