def division(x,y):
    z = x/y
    return print(z)

# try:
#     x = 6
#     y = 0
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# else:
#     division(x,y)
# finally:
#     print("The execution is complete")


# try:
#     x = 6
#     y = 2
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# else:
#     division(x,y)
# finally:
#     print("The execution is complete")


# try:
#     x = 5
#     print("The number is: " + x)
# except Exception as e:
#     print("Something is not correct ",e)
# else:
#     print("The program runs")
# finally:
#     print("The execution is complete")


# try:
#     i = 5
#     if i is str:
#         raise Exception("Value is int")
# except Exception as e:
#     print("Something went wrong : ", e)
# else:
#     print("No exception, no error")
# finally:
#     print("Code execution complete")



try:
    j = 6
    if j != 5:
        raise Exception("Value not matching")
except Exception as e:
    print("Something went wrong : ", e)
else:
    print("No exception, no error")
finally:
    print("Code execution complete")