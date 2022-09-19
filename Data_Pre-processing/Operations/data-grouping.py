import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Load data into data-frame
data = pd.read_csv('endangeredLang.csv')

#sort in descending order
large=data.sort_values(by='Number of speakers', ascending=False)
print(large.head(n=10))

#sort in ascending order
small=data.sort_values(by='Number of speakers', ascending=True)
print(small.head(n=10))

# sort by 2 parameters
x = data.sort_values(by = ["Number of speakers", "Latitude"])
print(x.head(5))

# Grouping
byStatus = data.groupby('Degree of endangerment')
#print(byStatus.head(n=10s))

print(data.groupby(['Degree of endangerment']).count())

# group on basis of two qualitative columns
bygroup_CnS = data.groupby(['Countries', 'Degree of endangerment'])
print(data.groupby(['Countries','Degree of endangerment']).count())

# group number of speakers by group labels (row names) from countries
x = data['Number of speakers'].groupby(data['Countries'])
print(x.head(n=10))

#Rank
# Row-wise
x = data.rank()
print(x.head())

# Column-wise
y = data.rank(axis = 1)
print(y.head())


