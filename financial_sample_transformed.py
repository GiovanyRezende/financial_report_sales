import pandas as pd

df = pd.read_excel('/content/Financial Sample.xlsx')

df['Segment'] = df.Segment.str.upper()
df['Product'] = df.Product.str.upper()
df['Month Name'] = df['Month Name'].str.upper()
df['Units Sold'] = round(df['Units Sold']).astype('int64')
df = df.fillna('None')
df = df.drop(columns=['Month Name','Month Number','Year'])
df.to_excel('financial_sample_transformed.xlsx')