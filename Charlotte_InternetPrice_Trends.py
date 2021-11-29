# @Jordan Detweiler
# Date 202101129

import pandas as pd
import plotly.express as px

# Load CSV file from Datasets folder
df = pd.read_csv('data/cities_internet_prices_historical.24-10-2021.csv')

# Filtering US Cases
prefiltered_df = df[df['Region'] == 'North Carolina']
filtered_df = prefiltered_df[prefiltered_df['City'] == 'Charlotte']
# Sort dateframe by desired data values
new_df = filtered_df.sort_values(by=['Internet Price, 2020'], ascending=[True])
new_df =new_df[new_df['Internet Price, 2020'] !=0]

#create arrays to store prices and years
price=[0]*6
year=[0]*6

#loop through data frame to get the price of every year skipping any with a value of zero
for i in range(15,21):
    if new_df['Internet Price, 20'+str(i)].values[0] != 0:
        price[i-15]=new_df['Internet Price, 20'+str(i)].values[0]
        year[i-15]='20'+str(i)

#configure graph
fig = px.line(x=year, y=price, title='Charlotte Internet Prices by Year')
fig.show()