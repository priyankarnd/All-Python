import pandas as pd
import numpy as np

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Load data
data = pd.read_csv('GlobalFirePower.csv')
print(data.head(5))

# index according to columns. Columns will be arranged alphabetically
# default ascending
x=data.sort_index(axis=1)
print(x.head(5))

#index according to columns. Columns will be arranged Z-A
#descending
x=data.sort_index(axis=1,ascending=False)
print(x.head(5))

#countries alphabetically A-Z (ascending order)
x=data.sort_values(by="ISO3")
print(x.head(5))

#sort by descending rank order
x=data.sort_values(by="Rank",ascending=False)
print(x.head(5))

# Double sort
x=data.sort_values(by=["Fit-for-Service","Total Population"])
print(x.head(5))

x=data.sort_values(by=["ISO3","Country"])
print(x.head(5))

# Sort by Fit-for-Service
x['mRank'] = x['Fit-for-Service'].rank(ascending=1)
print(x.head(6))

# Rank
# Rank data column wise #ascending
x=data.rank(axis=1)
print(x.head(5))
print(data.head(5))

# Rank data column wise #descending
x=data.rank(ascending=False)
print(x.head(5))



