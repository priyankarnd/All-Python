from os import close, read

# Read line by line
f = open("data.txt", "r")
print(f.readline())
print(f.readline())
print(f.readline())
f.close()

# Read first 5 characters
f = open("data.txt", "r")
print(f.readline(5))
f.close()

# # Write
# f = open("data2.txt", "w")
# f.write("Hello \n")
# f.write("Whassup? \t")
# f.write("How it's going \n \n")
# f.write("All good?")
# f.close()

# # Append
# f = open("data2.txt", "a")
# f.write("Yeah. It's going")
# f.close()

#Deleting a File

import os

if os.path.exists("data2.txt"):
    os.remove("data2.txt")
else:
    print("The file does not exist")
