# Reiley Meeks
# Quality of life index graph

import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('assets/countries_quality_of_life_index.18-10-2021.csv')

# Create World Map
fig = px.choropleth(data_frame=data, locations='Name', locationmode='country names', color=' "QualityOfLifeIndex"')
fig.show()

# Create Bar Chart
plt.figure(figsize=(15, 6))
sns.barplot(data=data.sort_values(by=' "QualityOfLifeIndex"', ascending=False).head(10), x='Name',
            y=' "QualityOfLifeIndex"')
plt.xticks(rotation=45)
plt.show()
