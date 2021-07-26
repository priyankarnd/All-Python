#Initial credit card number
print("Enter a 16-digit Credit Card Number:")
c = input()
print(c)

#Modified credit card number
final = ""

#Operate on the number
for x in range(0,16):
    print(c[x])
    #Locate the position
    if (x % 2 == 0): #Even Position digits
        d = 2 * int(c[x])  #Double the digit
        if (d >= 10):  #If greater than 10
            s = str(d)
            d = int(s[0]) + int(s[1])  #Sum up the digits
            d = str(d)
        else:   #if less than 10, keep it intact
            d = str(d)
    else:   #Odd position digits
        d = str(c[x])
    final = final + d

print(final)

final_str = str(final) # convert to string
str_len = len(final_str)  #find length of string
sum = 0

for x in range(0,str_len):
    sum = sum + int(final_str[x])  # Add every digit of no.

print(sum)

#Check validity
if (sum % 10 == 0):
    print("This is a valid credit card")
else:
    print("Credit card is not valid")






    #d = 2 * int(c[x])
    #print(d)

# s = ""
# print(s)
#
# s = s + "1"
# print(s)
#
# s = s + "2"
# print(s)
