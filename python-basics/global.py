a = 1 # global variable

def inc():
    # Throw error since a is out of scope inside this function; need to declare global a
    global a
    a = a + 1
    print("Incremented value inside function", a)

inc()

print("The value of a: ",a)

# Access the function from outside

def mult():
    # global b
    b = 5
    b = b * 2
    print(b)

mult()

# print(b)



