import pandas as pd

# Read .txt file
df = pd.read_csv("bostonTxt.txt", sep = "\t")

# Print df
print(df.head(6))