numbers = { 'data1' : 100, 'data2' : 54, 'data3' : 247 }

sum = 0

#sum = sum(numbers.values())

item = len(numbers)

for x in numbers:
    sum += numbers[x]

average = sum / item
average = round(average, 2)

print("Sum: ", sum)
print("Average: ", average)




