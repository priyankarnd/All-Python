import pandas as pd

d=pd.read_csv('titanic.csv')

print(d.head())

# Shape of data
print(d.shape)

# What are the columns in dataframe
print(list(d))

# What are their data types
print(d.dtypes)

# Datatype of a particular column
print(d['Name'].dtype)

# Count rows
print(d.count())

# Statistical summary of quantitative
print(d.describe())

# How many NAs in data
print(d.isna().sum())

# Fill missing values with zero
filled_zeros = d.fillna(0)
print(filled_zeros.count())

#Replace age NA s with mean values
df=d.copy() ##make a copy
df.Age.fillna(df.Age.mean(), inplace=True)

print(df.isna().sum())



