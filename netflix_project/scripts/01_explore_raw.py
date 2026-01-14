import pandas as pd
df = pd.read_csv('../data_lake/raw/netflix_titles.csv')
print(df.head())
print('Rows:', len(df))
print(df.isna().sum())
