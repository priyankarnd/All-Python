import pandas as pd

data = [['Alex','$12'],['Bob','$15'],['Clarke','$17']]
df = pd.DataFrame(data,columns=['Name','Allowance'])
print (df)

print(df['Allowance'].describe())

# Replace $ with blank
df['Allowance'] = df['Allowance'].map(lambda value: value.replace('$',''))
print(df)

print(df['Allowance'].describe())

# Convert to float
df['Allowance'] = df['Allowance'].astype(float)

print(df)
print(df['Allowance'].describe())
