import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

e = pd.read_csv('ebola.csv')
print(e.head(5))

print(e['Country'].unique())

## convert to date time
e['Date'] = e['Date'].apply(pd.to_datetime)
print(e.head(5))

## ascending
e = e.sort_values(by='Date')
print(e.head())

# Minimum date
date0 = e['Date'].min()
print(date0)

# number of days since start
e['Start'] = e['Date'].apply(lambda date: (date - date0).days)
print(e.head())