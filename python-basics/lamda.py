x = lambda a : a + 100

print(x(50))
print(x(150))

x = lambda a, b : a * b
print(x(10,2))

x = lambda a, b, c : a + b + c
print(x(10,20,30))

def func(a):
    return lambda a: a + 10

y = func(20)

print(y(20))

