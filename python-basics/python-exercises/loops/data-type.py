myList = [1,2,"one","two","three", 1.5, 3.5]

Ints = []
Strings = []
Floats = []

# i = 5
# print(type(i))
#
# if (type(i) == int):
#     print("T")
#
# x = 5.5
# if (type(x) == float):
#     print("T")
#
# z = "cad"
# # print(type(z))
# if (type(z) == str):
#     print("T")

for x in myList:
    if (type(x) == int):
        Ints.append(x)
    elif (type(x) == float):
        Floats.append(x)
    else:
        Strings.append(x)

print("Ints ", Ints)
print("Strings ", Strings)
print("Floats ", Floats)




