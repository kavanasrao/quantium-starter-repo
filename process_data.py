import pandas as pd



df_one = pd.read_csv('data/daily_sales_data_0.csv')
df_two = pd.read_csv('data/daily_sales_data_1.csv')
df_three = pd.read_csv('data/daily_sales_data_2.csv')


#merge the three dataframe into dataframe 

df = pd.concat([df_one, df_two, df_three], ignore_index=True)

# Filter the value

df = df[df['product'] == 'pink morsel']

df['price'] = df['price'].str.replace('$', ''). astype(float)


df['sales'] = df['quantity'] * df['price']


df = df[['sales', 'date', 'region']]

df.to_csv('output_data.csv', index=False)

