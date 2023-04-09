u = int(input("Upper range of the interval: "))
l = int(input("Lower range of the interval: "))



if u <= 0 or l <= 0:
    print("Input positive number")
else:
    prime_no = []
    for i in range(l,u+1):   
        for x in range(2,i):
            if i % x == 0:
                break
        else:
            prime_no.append(i)

    print(prime_no)





