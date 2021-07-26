odd = []
even = []

for x in range(1, 101):
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)

print(odd)
print(even)