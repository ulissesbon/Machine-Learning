import pandas as pd
import numpy as np

df = pd.DataFrame({'A': [1, 2, np.nan, 4], 'B': [5, np.nan, 7, 8]})
print("DataFrame original:\n", df)

print("\nValores ausentes:")
print(df.isnull())

print("\nDeletar linhas NaN:")
print(df.dropna())

print("\nPreencher NaN com valor constante:")
print(df.fillna(0))

print("\nPreencher com média:")
df['A'] = df['A'].fillna(df['A'].mean())
df['B'] = df['B'].fillna(df['B'].mean())
print(df)