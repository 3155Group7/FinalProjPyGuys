# Reiley Meeks
# Quality of life index graph

import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from flask import Flask
from flask  import render_template
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from io import BytesIO
import plotly.graph_objs as go


app = Flask(__name__)


data = pd.read_csv('assets/countries_quality_of_life_index.18-10-2021.csv')


@app.route('/004')
def graph004():
    # Create World Map
    fig = px.choropleth(data_frame=data, locations='Name', locationmode='country names', color=' "Quality Of Life Index"')
    fig.write_html("templates/myplot.html")
    return render_template('myplot.html')

@app.route('/001')
def graph001():


    # Create Bar Chart of 5 Nations
    plt.figure(figsize=(15, 6))
    sns.barplot(data=data.sort_values(by=' "Quality Of Life Index"', ascending=False).head(5), x='Name',
                y=' "Quality Of Life Index"')
    plt.xticks(rotation=45)
    output = BytesIO()
    FigureCanvas(plt.gcf()).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

@app.route('/002')
def graph002():

    # 10 Nation Bar Chart
    plt.figure(figsize=(15, 6))
    sns.barplot(data=data.sort_values(by=' "Quality Of Life Index"', ascending=False).head(10), x='Name',
                y=' "Quality Of Life Index"')
    plt.xticks(rotation=45)
    output = BytesIO()
    FigureCanvas(plt.gcf()).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

@app.route('/003')
def graph003():

    # 15 Nation Bar Chart
    plt.figure(figsize=(15, 6))
    sns.barplot(data=data.sort_values(by=' "Quality Of Life Index"', ascending=False).head(15), x='Name',
                y=' "Quality Of Life Index"')
    plt.xticks(rotation=45)
    output = BytesIO()
    FigureCanvas(plt.gcf()).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

@app.route('/North-Carolina')
def graph005():

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
    fig.write_image("static/images/NCfig3.png")
    




    image3 = 'static/images/NCfig3.png'
    return render_template('North-Carolina.html', image2=image3)

@app.route('/North-Carolina_internet')
def graph006():
    # Load CSV file from Datasets folder
    df = pd.read_csv('assets/cities_internet_prices_historical.24-10-2021.csv')
    
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
    fig.write_image("static/images/NCfig1.png")
    
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
    fig.write_image("static/images/NCfig4.png")

    image = 'static/images/NCfig1.png'
    image4 = 'static/images/NCfig4.png'
    return render_template('North-carolina.html', image=image , image2=image4)
    


@app.route('/Home')
def home():
    return render_template('Home.html')


@app.route('/Countries-Around-the-Globe')
def countries():
    graph = '/003'
    interative= '/004'
    return render_template('Countries-Around-the-Globe.html', image=graph, iframe = interative)



app.run(host='0.0.0.0', port=5000)
