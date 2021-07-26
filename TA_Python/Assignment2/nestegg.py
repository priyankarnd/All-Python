curbal = 10000  #initial investment

year = 0  #year beginning

newbal = 0

while (curbal < 25000):
    year += 1  # 1 year has passed
    newbal = curbal + .08 * curbal   # new balance with growth
    curbal = newbal    #upadte current balances
    print(f'Year: {year}')
    print(f'Current balance: {curbal}')

else:
    print(f'Years taken: {year}')



