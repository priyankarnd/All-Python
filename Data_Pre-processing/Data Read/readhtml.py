import pandas as pd

#Read html
uss=pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')

print(type(uss))
#print(uss)

u = uss[0]
print(type(u))

print(uss)

print(u)


