import numpy as np
import pandas as pd

# Example of importing data from CSV file
df = pd.read_csv('data.csv')

# Example of performing some operations on the DataFrame
print(df)

# Example of filtering rows based on certain conditions
filtered_df = df[df['column_name'] > 0]

# Example of handling missing values in a column
df.fillna(value, inplace=True)

# Example of using functions to manipulate data
df.apply(lambda x: (x > 5).astype(int))
