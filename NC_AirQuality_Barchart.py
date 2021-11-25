# @Jordan Detweiler
# Date 202101125

import pandas as pd
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('assets/cities_air_quality_water_pollution.18-10-2021.csv')

# Filtering US Cases
filtered_df = df[df[' "Region"'] == ' "North Carolina"']

# Sort dateframe by desired data values
new_df = filtered_df.sort_values(by=[' "AirQuality"'], ascending=[True])

# Preparing data
data = [go.Bar(x=new_df['City'], y=new_df[' "AirQuality"'])]

# Preparing layout
layout = go.Layout(title='Air Quality of NC Cities', xaxis_title="City",
                   yaxis_title="Air Quality")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
fig.show()