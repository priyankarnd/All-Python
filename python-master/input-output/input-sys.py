import sys

#Send output
print ("Hello {} {}".format(sys.argv[1], sys.argv[2]))

print(sys.argv[0])

print(len(sys.argv)) #Print number of arguments

for arg in sys.argv:  #Print each argument
    print(arg)

