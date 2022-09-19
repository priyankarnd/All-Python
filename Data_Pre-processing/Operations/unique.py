import pandas as pd
from collections import Counter

indc=pd.read_csv("Indicators.csv")

# How many unique countries
countries = indc['CountryName'].unique().tolist()
print(countries)

# Array format
x=indc['CountryName'].unique()
print(x)

# How many countries
print(len(countries))

# How many individual countries
c = Counter(countries)
print(c)

# List all country codes
ccode = indc['CountryCode'].tolist()
print(ccode)

# Most common country code
cc = Counter(ccode)
print(cc.most_common(1))

# 2 most common country codes
print(cc.most_common(2))

# First 20 indicator names
print(indc['IndicatorName'][:20])







