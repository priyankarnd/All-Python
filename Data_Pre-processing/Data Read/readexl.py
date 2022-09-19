import pandas as pd

# Read excel file
x1 = pd.ExcelFile("boston1.xls")

# Print the sheet names
print(x1.sheet_names)

# Load 1 sheet
s1 = x1.parse('Sheet1')

print(s1)