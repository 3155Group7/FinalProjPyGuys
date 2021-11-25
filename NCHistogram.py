# @Jordan Detweiler
# Date 202101125

import pandas as pd
import plotly.express as px

# Load CSV file from Datasets folder
df = pd.read_csv('assets/cities_air_quality_water_pollution.18-10-2021.csv')

# Filtering US Cases
filtered_df = df[df[' "Region"'] == ' "North Carolina"']

# sort filtered dataframe
new_df = filtered_df.sort_values(by=[' "AirQuality"'], ascending=[False])

# create graph
fig = px.density_heatmap(new_df, x=' "AirQuality"', y=' "WaterPollution"', marginal_x="histogram", marginal_y="histogram")
fig.show()
