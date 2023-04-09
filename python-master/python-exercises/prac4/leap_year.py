year = int(input("Enter a year: "))

if year <= 0:
    print("A positive year input is required")
else:
    if (year % 100 == 0) and (year % 400 != 0):
        print("This is not a leap year")
    elif (year % 4 == 0) or (year % 400 == 0):
        print("This is a leap year")
    else:
        print("This is not a leap year")

