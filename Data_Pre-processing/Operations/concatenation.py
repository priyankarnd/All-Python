import pandas as pd
import numpy as np

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Data 1
df1 = pd.DataFrame([['a',1],['b',2]], columns = ['letter', 'number'])
print(df1)

# Data 2
df2 = pd.DataFrame([['c',3],['d',4]], columns = ['letter', 'number'])
print(df2)

# Concatenation
print(pd.concat([df1, df2]))

# Data 3
df3 = pd.DataFrame([['c', 3, 'cat'],['d', 4, 'dog']], columns = ['letter', 'number', 'animal'])
print(df3)

# Concatenation
print(pd.concat([df1, df3]))

#only columns common for both data frames are joined togther
print(pd.concat([df1, df3], join="inner"))