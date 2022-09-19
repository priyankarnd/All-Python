import pandas as pd

d=pd.read_csv('titanic.csv')

# How many NAs in data
print(d.isna().sum())

# Fill in the most common string values

# Identify the most common Cabin type
print(d['Cabin'].value_counts().index[0])  # most common category of Cabins

#Fill in
print(d['Cabin'].fillna(d['Cabin'].value_counts().index[0]))