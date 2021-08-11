import even_detector

qstn = str(input("Do you want to search a number? "))

if qstn == "yes":
    n = int(input("Enter the number you want to search: "))
    if n in even_detector.evn_no:
        print("Yes the number is present in the list")
    else:
        print("Sorry no such number is there in the list")
elif qstn == "no":
    print("Okay. Have a good day!")
else:
    print("Please enter yes or no")



