import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer



d=pd.read_csv('pima-indians-diabetes.csv', header=None)

# How many zeros in column
print((d[[1,2,3,4,5,6,7,8]] == 0).sum())

# mark zero values as missing or NaN
d[[1,2,3,4,5]] = d[[1,2,3,4,5]].replace(0, np.NaN)

# Check 0 values
print((d[[1,2,3,4,5,6,7,8]] == 0).sum())

# built-in imputation techniques
values = d.values
imputer = SimpleImputer() ## call the function

transformed_values = imputer.fit_transform(values)
# count the number of NaN values in each column
print(np.isnan(transformed_values).sum())