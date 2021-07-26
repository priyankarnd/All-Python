curbal = 10000  #initial investment

year = 0  #year beginning

newbal = 0

for year in range(0,40):
    newbal = curbal + .08 * curbal  # new balance with growth
    curbal = newbal  # upadte current balances
    print(f'Year: {year+1}')
    print(f'Current balance: {curbal}')

curbal = round(curbal,2)

print(f'The new balance is: {curbal}')