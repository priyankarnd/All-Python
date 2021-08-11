print("You can enter a maximum of 5 numbers")

l = int(input("How many numbers you want? "))

# initial sum is 0
b = 0

if l <= 0:
    print("Enter some positive value")
elif l > 5:
    print("Maximum 5 numbers are accepted")
else:
    for i in range(0,l):
        a = int(input("Enter a number: "))
        b += a
        # print("Summing up",b) 
    print("Final sum: ", b)