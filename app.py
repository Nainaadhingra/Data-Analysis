# Run this app with `python app.py` and
# visit http://127.0.0.1:8050 in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv(r'C:\Users\Naina\Downloads\cars_engage_2022 (1).csv')

fig = px.pie(df, names='Body_Type')
fig2 = px.pie(df, names='Type')
res = []
for ft in df['Fuel_Type'].unique():
    ddf = df.loc[df['Fuel_Type']==ft]
    str1 = ft, len(ddf)
    res.append(str1)
#long_df = px.data.medals_long()
dddf = pd.DataFrame(res, columns=['Fuel_Type', 'Number'])
fig3 = px.bar(dddf, x='Fuel_Type', y = 'Number', color='Fuel_Type')

fig4 = px.pie(df, names='Body_Type')

d = []
for arai_mileage in df['ARAI_Certified_Mileage']:
    #print(arai_mileage)
    if type(arai_mileage) != float:
        d.append((arai_mileage.split(' ')[0]))
    elif type(arai_mileage) == str:
        d.append(0.0)
    else:
        d.append(0.0)
df['ARAI_Certified_Mileage'] = d
df['ARAI_Certified_Mileage'] = df['ARAI_Certified_Mileage'].apply(pd.to_numeric, errors='coerce').dropna()
fig5 = px.scatter(df, x = 'Model', y='ARAI_Certified_Mileage', color='Model', hover_data=['Variant'])

d = []
for bs in df['Boot_Space']:
    #print(arai_mileage)
    if type(bs) != float:
        d.append((bs.split(' ')[0]))
    elif type(bs) == str:
        d.append(0.0)
    else:
        d.append(0.0)
df['bs'] = d
df['bs'] = df['bs'].apply(pd.to_numeric, errors='coerce').dropna()
fig6 = px.scatter(df, x = 'Model', y='bs', color='Model', hover_data=['Variant'])


fig6 = px.scatter(df, x='Make', y='Number_of_Airbags', color='Model', hover_data=['Number_of_Airbags', 'Make', 'Model'])
fig6.update_layout(showlegend=False)


fig7 = px.scatter(df, x='Make', y='Cylinders', color='Model', hover_data=['Cylinders', 'Make', 'Model'])
fig7.update_layout(showlegend=False)

app.layout = html.Div(children=[
    html.H1(children='Data analysis'),
    
    html.Div(children='''
        Data Analysis is a process of inspecting, cleansing, transforming, and modelling data with the goal of discovering useful information, informing conclusions, and supporting decision-making.

 7 Steps of Data Analysis
s1.	Define the business objective.- Step one of the data analysis process should be to clearly state and understand the business objective.

2.	Source and collect data.- The goal is to find data that is relevant to solving the problem or supports an analytical solution of the stated objective

3.	Process and clean the data.- the data collected is processed and verified. Raw data must be converted into a usable format and this often requires parsing, transforming, and encoding. 

4.	Perform exploratory data analysis (EDA).- the data is examined carefully for possible logical groupings and hidden relationships. Basic statistical methods and graphs can be used, as well as more advanced methods like clustering, principal component analysis, or other dimension reduction methods.

5.Select, build, and test models.-The next step after exploratory data analysis is model  selection, building, and testing. In this step, the analytical approach is put together and  tested.

6.Deploy models.- The goal of model deployment is to produce outputs that lead to a decision or action.

7.Monitor and validate against stated objectives. -The final step in a data analysis process is monitoring and validation. After decisions have been put into play and allowed a short time to work, it's important to go back and check to see if outcomes are as expected.

6 Types of Data Analysis
•	Descriptive Analysis.
•	Exploratory Analysis.
•	Inferential Analysis.
•	Predictive Analysis.
•	Causal Analysis.
•	Mechanistic Analysis.'''
    ),
    html.H1(children='''
        Types of cars in the Dataset
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),

    html.H1(children='Gear Transmission type of the vehicles in the dataset'),

    html.Div(children='''
        Gear Transmission type is one of the factors in designing the vehicle.Car transmissions are just one part of the fascinating and complex process that occurs every time you start your engine to go for a ride. Usually, automatic transmission is a necessity in the trafficked roads.
    '''),

    dcc.Graph(
        id='example-graph2',
        figure=fig2
    ),

    html.H1(children='Fuel Types'),

    html.Div(children='''
        Fuel type is one of the factors while buying the vehicle. Fuelling your vehicle with the correct oil ensures your vehicle's optimum performance
    '''),

    dcc.Graph(
        id='example-graph3',
        figure=fig3
    ),

    html.H1(children='Body Types of vehicles'),

    html.Div(children='''
        The easiest way to define a vehicle is by how it looks. What's the first thing you notice when a vehicle comes toward you on the street? Its shape. That's called the "body type."
    '''),

    dcc.Graph(
        id='example-graph4',
        figure=fig4
    ),

        html.H1(children='Body Types of vehicles VS Mileage'),

    html.Div(children='''
       Car's mileage can be calculated by dividing the number of kilometers that you have driven by the number of liters of fuel that filled the second time.
    '''),

    dcc.Graph(
        id='example-graph5',
        figure=fig5
    ),

        html.H1(children='Company VS Airbags'),

    html.Div(children='''
        An airbag is an inflatable safety device designed to protect the occupants of a car in case of a collision. 
    '''),

    dcc.Graph(
        id='example-graph6',
        figure=fig6
    ),

    html.H1(children='Company VS Cylinder'),

    html.Div(children='''
        A cylinder is a vital part of the engine. It's a chamber where fuel is combusted and power is generated.
    '''),

    dcc.Graph(
        id='example-graph7',
        figure=fig7
    ),

    
])

if __name__ == '__main__':
    app.run_server(debug=True)
