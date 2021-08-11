#Exceptions

try :
    print (x)
    print ("After the print statement")

except :
    print ("An exception occurred")


try :
    print (x)
except NameError :
    print ("Variable x is not defined")
except :
    print ("Something else went wrong")

#Else
#Execute a block of code if no errors were raised

try:
    print("hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

try :
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print ("Value of x is {}".format(x))

#Finally
#Execute a block regardless of if try block raises an error or not

try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The try except is finished")

try:
    print("Hi there")
except:
    print("Something went wrong")
finally:
    print("The try except is finished")


try :
    # x = 10 * 50
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
else :
    print("Value of x is {}".format(x))
finally :
    print("This code will always run")

# Default exception

try:
    f = open("test.txt")
    f.write("Hello, how are you")
    f.close()
except Exception as e:
    print(e)
finally:
    print("Finished")

try:
    x = input("Enter username: ")
    print("Username is: " + int(x))
except Exception as e:
    print("Something went wrong: ", e)
else:
    print("Default statement")
finally:
    print("Code execution finished")


try:
    x = input("Enter username: ")
    print("Username is: " + x)
except Exception as e:
    print("Something went wrong: ", e)
else:
    print("Default statement")
finally:
    print("Code execution finished")

# Exception within logic passed to except block

try:
    i = 0
    while(i<10):
        print(i)
        if i == 5:
            break
            raise Exception("Value is equal to 5")
        i = i + 1
except Exception as e:
    print("Something went wrong : ", e)
else:
    print("No exception, no error")
finally:
    print("Code execution complete")





# #Raising your own custom exception

y = -1
if y < 0 :
    #raise Exception ("Your number is less than zero")
    #raise ValueError ("Your number is less than zero")
    pass

x = "Hello"
if not(type(x)) is int:
    # raise TypeError("Only integers are allowed:")
    pass


#Getting the details of an exception
try :
    with open ("file.log") as file:
        read_data = file.read()

except FileNotFoundError as fnf_error :
    print(fnf_error)

#Assertions
y = -1
#y = 2
assert (y > 0) , "y cannot be less than zero"







