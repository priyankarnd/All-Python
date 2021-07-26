1.
a> df.drop(columns=['B', 'C'])
b> df['Year Built'].between(1950,2000,inclusive = True)
c> df.shape

2.
a> df["Age"] = ""
   df["Avg. Room size"] = ""

b>
from datetime import date
today = date.today()

current_year = today.year

df["Age"] = df["Age"].apply(lambda x: x - current_year)

Avg_room_size_col = df["Gr Liv Area"] / df["TotRms AbvGrd"]
df["Avg. Room size"] = Avg_room_size_col

df.describe().loc[['min','max','std'], 'Column names']

4.
df2 = df[df.Neighborhood == "NWAmes"]
des = df2.sort_values(by = "SalePrice", ascending=False)

To print a specific row we have couple of pandas method

loc - It only get label i.e column name or Features
iloc - Here i stands for integer, actually row number
ix - It is a mix of label as well as integer
How to use for specific row

loc
df.loc[row,column]
For first row and all column

df.loc[0,:]
For first row and some specific column

df.loc[0,'column_name']
iloc
For first row and all column

df.iloc[0,:]
For first row and some specific column i.e first three cols

df.iloc[0,0:3]

5.
df = pd.DataFrame([[5.1, 3.5, 0], [4.9, 3.0, 0], [7.0, 3.2, 1],
                   [6.4, 3.2, 1], [5.9, 3.0, 2]],
                  columns=['length', 'width', 'species'])
ax1 = df.plot.scatter(x='length',
                      y='width',
                      c='DarkBlue')

2>
https://www.geeksforgeeks.org/selection-sort/
