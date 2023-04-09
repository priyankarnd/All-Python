def generator1():
    yield 1
    yield 2
    yield 3

for value in generator1():
    print(value)

def generator2():
    yield 1
    yield 2
    yield 3

x = generator2()

print(x.__next__())
print(x.__next__())
print(x.__next__())