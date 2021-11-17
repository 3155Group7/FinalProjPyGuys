# Reiley Meeks
# Quality of life index graph

import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('assets/countries_quality_of_life_index.18-10-2021.csv')

# Create World Map
fig = px.choropleth(data_frame=data, locations='Name', locationmode='country names', color=' "Quality Of Life Index"')
fig.show()

# Create Bar Chart of 5 Nations
plt.figure(figsize=(15, 6))
sns.barplot(data=data.sort_values(by=' "Quality Of Life Index"', ascending=False).head(5), x='Name',
            y=' "Quality Of Life Index"')
plt.xticks(rotation=45)
plt.show()

# 10 Nation Bar Chart
plt.figure(figsize=(15, 6))
sns.barplot(data=data.sort_values(by=' "Quality Of Life Index"', ascending=False).head(10), x='Name',
            y=' "Quality Of Life Index"')
plt.xticks(rotation=45)
plt.show()

# 15 Nation Bar Chart
plt.figure(figsize=(15, 6))
sns.barplot(data=data.sort_values(by=' "Quality Of Life Index"', ascending=False).head(15), x='Name',
            y=' "Quality Of Life Index"')
plt.xticks(rotation=45)
plt.show()
