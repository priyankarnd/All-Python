list = [ (12,3,10), (5,3), (11,10,90), (12,13,51)]

n = 10

output = []

for x in list:
    print(x)
    if n in x:
        output.append(x)

print(output)

