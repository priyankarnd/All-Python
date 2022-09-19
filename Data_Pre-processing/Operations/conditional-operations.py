import numpy as np
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Load the data into a DataFrame
# data of endangered languages
data = pd.read_csv('endangeredLang.csv')

#isolate a column
print(data['Countries'])

#isolate 2 columns
df=data[['Countries','Name in English']]

print(df.head(6))

#isolate rows
print(data[3:10])

# conditional selection
print(data[data['Number of speakers']<5000]) #isolate the portion of df containing languages with less than 5000 speakers

# selecting all entries from index 6 onwards
print(data[6:])

#select entries at even index locations
print(data[::2])

#specify the ranges of rows and columns
print(data.iloc[0:8,0:7])

# select all columns for rows of index values 0 and 10
print(data.loc[[0, 10], :])

#isolate rowsa and columns
print(data[['Countries','Name in English']][4:8])

#isolate by row names
print(data[data.Countries == "Italy"])

#isolate by two row labels
x=data.loc[data['Countries'].isin(['Italy','Germany'])]
print(x.head(10))

df=data[:] #make a copy of the data frame stored in data

#replace "Number of Speakers" with "Number"
df.rename(columns={'Number of speakers':'Number'}, inplace=True)

print(df.head(10))

#specify 2 conditions to be fulfilled
print(df[(df.Countries == "India") & (df.Number<100)])