import pandas as pd

data=pd.read_csv("all_stocks_5yr.csv")
print(data.head(6))

# convert "date" to datetime type
data.date = pd.to_datetime(data.date)
print(data.dtypes)

## Set the DataFrame index using existing columns.
## inplace=True : the dataframe will not be modified
data.set_index('date', inplace=True)



