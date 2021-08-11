x = (1,2,3,4,5)  # Tuple

y = list(x)  # Convert to list

print(y)

# y[2] = "modified"

# print(y)

# x = tuple(y)

# print(x)

n = int(input("Enter the position you want to modify: "))
data = int(input("Enter your modified value: "))

y[n] = data

print(y)

x = tuple(y)

print(x)



