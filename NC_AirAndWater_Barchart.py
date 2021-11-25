# @Jordan Detweiler
# Date 202101125

import pandas as pd
import plotly.express as px

# Load CSV file from Datasets folder
df = pd.read_csv('assets/cities_air_quality_water_pollution.18-10-2021.csv')

# Filtering US Cases
filtered_df = df[df[' "Region"'] == ' "North Carolina"']

# Sort filtered frame by desired data values
new_df = filtered_df.sort_values(by=[' "AirQuality"', ' "WaterPollution"'], ascending=[True, True])

# Plot the figure and saving in a html file
fig = px.bar(new_df, x="City", y=[' "AirQuality"', ' "WaterPollution"'], title="Air Quality Score and Water Pollution")

# fig.update_layout(barmode='stack', xaxis={'categoryorder':'total ascending'})
fig.show()