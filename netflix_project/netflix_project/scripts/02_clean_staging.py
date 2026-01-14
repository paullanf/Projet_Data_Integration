import pandas as pd
raw = '../data_lake/raw/netflix_titles.csv'
out = '../data_lake/staging/netflix_titles_staging.csv'
df = pd.read_csv(raw)
df = df.drop_duplicates(subset=['show_id'])
df['type'] = df['type'].str.strip().str.lower()
for col in ['director','cast','country']:
 df[col] = df[col].fillna('Unknown')
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce').dt.date
keep = ['show_id','type','title','country','release_year','rating','duration','listed_in','date_added']
df = df[keep]
df.to_csv(out, index=False)
print('Saved to STAGING')