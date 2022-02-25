#File handling in Python

'''
Modes:

Opening a file using open() function

There are four different methods (Modes) for opening a file:

"r": Read   - Default value. Opens a file for reading, error if the file does not exist
"a": Append - Opens a file for appending, creates the file if it does not exist
"w": Write  - Opens a file for writing, creates the file it does not exist 
"x": Create - Creates the spcific file , returns an error if the file exists

"t" : Text - Default value. Text mode.
"b" : Binary - Binary mode (e.g. images)
'''

from os import close, read


f = open("data2.txt")
f.close()
print(f)

f = open("data2.txt", "rt")
print(f)
f.close()

# Reading and writing a file
f = open("data2.txt","r")
print(f.read())
f.close()

f = open("data2.txt", "r")
print(f.read(3))
f.close()

f = open("data2.txt", "r")
print(f.readline())
print(f.readline())
print(f.readline())
f.close()

f = open("data2.txt", "r")
for x in f:
    print(x)
f.close()


# Writing a file
f = open("data2.txt", "a")
f.write("hello, this is the id")
f.write("hello, this is the id1")
f.write("hello, this is the id2 \n")
f.write("hello, this is the id3 \n\n")
f.write("hello, this is the id4 \t")
f.write("hello, this is the id1 \t\t")

f.close()

f = open("data3.txt", "w")
f.write("This is Chicago")
f.close()

f = open("data5.txt", "x")
f.write("This is LA")
f.close()


# f = open("data6.txt", "r")
# print(f.read())
# f.close()

# Deleting a File

import os

if os.path.exists("data4.txt"):
    os.remove("data4.txt")
else:
    print("The file does not exist")




