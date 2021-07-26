print("Enter your first name:")
f = input()
print(f[0].lower())

print("Enter your last name:")
l = input()
print(l.lower())

print("Enter your birth year:")
y = input()
y=str(y)
print(y[-2:])

username = f[0].lower() + l.lower() + y[-2:]
print("Username: ", username)