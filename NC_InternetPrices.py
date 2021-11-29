# @Jordan Detweiler
# Date 202101129

import pandas as pd
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('assets/cities_internet_prices_historical.24-10-2021.csv')

# Filtering US Cases
filtered_df = df[df['Region'] == 'North Carolina']
# Sort dateframe by desired data values
new_df = filtered_df.sort_values(by=['Internet Price, 2020'], ascending=[True])
new_df =new_df[new_df['Internet Price, 2020'] !=0]
#Preparing data
data = [go.Bar(x=new_df['City'], y=new_df['Internet Price, 2020'])]

# Preparing layout
layout = go.Layout(title='Internet Prices of NC Cities', xaxis_title="City",
                 yaxis_title="Internet Price")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
fig.show()