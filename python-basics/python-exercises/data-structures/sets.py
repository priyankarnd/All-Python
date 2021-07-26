#Input set
numset = { 3, 29, 5, 4, 87, 34, 43, 12, 2}

maxnum = max( numset )
minnum = min( numset )

# print(maxnum)
# print(minnum)

print(f'Maximum : {maxnum}')
print(f'Minimum : {minnum}')

set1 = { 12, 55, 6, 7, 9, 2}
set2 = { 9, 2, 7, 12, 6}

for x in set2:
    set1.discard(x)

for y in set1:
    print(f'The difference is the value {y} from set 1')

print("The difference is the value ", set1-set2, "from set 1")



