n = int(input("How many numbers you want to enter? "))

lst = [] # Initialize empty list

for x in range(0,n):
    y = int(input("Enter your input: "))
    lst.append(y)

print(lst)

evn_no = [] # even no list
odd_no = [] # odd no list

count = 0

for x in lst:
    if x % 2 == 0:
        count += 1
        evn_no.append(x)
    else:
        odd_no.append(x)
        

print(f'There are {count} even numbers in your list')

print("Even number list: ")
print(evn_no)

print("Odd number list: ")
print(odd_no)

evn_no.extend(odd_no)

print(evn_no)







