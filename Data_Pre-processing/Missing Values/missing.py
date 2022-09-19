import pandas as pd
import numpy as np

#Create sample data
df = pd.DataFrame([[1,np.nan,2],[2,3,5],[np.nan,4,6]])  # Some cells have no values NA
print(df)

# Check if dataframes contain NA
print(df.isnull())

# Drop NA; all rows with NA will be dropped
print(df.dropna())

# Drop columns where cells have NA
print(df.dropna(axis=1))

# Threshold determines maximum no. of NA values that can be kept
print(df.dropna(thresh=3))

# fill NA entries with zero
print(df.fillna(0))

# specify a forward-fill to propagate the previous value forward
print(df.fillna(method="ffill"))

#fill forward column wise
print(df.fillna(method="ffill",axis=1))

#back-fill to propagate the next values backward
print(df.fillna(method="bfill"))