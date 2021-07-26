#Enter building number
print("Enter building number:")
b = input()
print(f'Your inputted building no. is: {b}')

#Calculate Column
col = int(b) % 5  #Calcualte modulo value

if ( col == 1 ):
    Column = "A"
elif ( col == 2 ):
    Column = "B"
elif ( col == 3 ):
    Column = "C"
elif ( col == 4):
    Column = "D"
else:
    Column = "E"

print(Column)

#calculate Row
if (col != 0):
    Row = int(b) / 5 + 1
else:
    Row = int(b) / 5

Row = int(Row)

print(Row)

print(f'The building is located at Column:{Column} and Row:{Row}')