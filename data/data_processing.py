import pandas as pd
import csv

df_0 = pd.read_csv('daily_sales_data_0.csv')
df_1 = pd.read_csv('daily_sales_data_1.csv')
df_2 = pd.read_csv('daily_sales_data_2.csv')

df = pd.concat([df_0, df_1, df_2])

df = df[df['product'] == 'pink morsel']

df['price'] = df['price'].str.replace('$', '', regex=False).astype(float)

df['sales'] = df['price'] * df['quantity']

df = df[['sales', 'date', 'region']]

df.to_csv('formatted_data.csv', index=False)