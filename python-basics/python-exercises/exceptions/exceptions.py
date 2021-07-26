def division (x,y):
    z = x/y
    return print(z)

try:
    x = 6
    y = 2
except ZeroDivisionError:
    print("Cannot divide by zero")
if x < 0 or y <0:
    raise ValueError("Input is less than zero")
else:
    division(x,y)




