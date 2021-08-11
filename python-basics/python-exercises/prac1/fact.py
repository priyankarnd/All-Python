import math
from os import close, read 

x = int(input("Enter a number: "))

print(x)

try:
    factor = math.factorial(x)

    # if x < 0:
    #     raise Exception("Negative value is not accepted")
except Exception as e:
    print("Give non-negative value input", e)
else:
    print("Computation is complete")


try:
    print(f'The value is {factor}')
    f = open("value.txt","w")
    f.write(str(factor))
    f.close()
except Exception as e:
    print("Nothing to write",e)
else:
    print("Write completed in file")
finally:
    print("Program Complete")







