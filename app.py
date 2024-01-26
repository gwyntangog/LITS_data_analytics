# app.py
from functions.clean_data import clean_data
from functions.map_function import map_function
from functions.histogram_function import histogram_function
from functions.pie_function import pie_function
import pandas as pd
from dash import Dash, dcc, html, Input, Output
import dash
import matplotlib.pyplot as plt
import plotly.express as px
import os

#Initialize the app
app = Dash(__name__,)
server = app.server
app.title = "LiTS Data Analyst"

#Checking number of years to protect from updates
years = []
directory = os.getcwd()
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".xlsx"):
        list_name = filename[:-5]
        years.append(list_name)
years.sort(reverse = True)
default_year = years[0]

#Dropdown options
regions = ['All Regions', 'Africa','Asia','Europe','Latin America and the Caribbean', 'Northern America','Oceania']
pie_dividers = ['Type','Level of Support']
sectors = ["All Sectors", 'Transparency and accountability / open government','Human rights / humanitarian', 'Philanthropy', 'Environmental justice', 'Civic Tech', 'Health', 'Sex worker rights', 'Gender-based violence',
           'Digital Security', 'Mental Health','Legal Empowerment','Communications','Gender','Racial Justice','Migration Justice','Domestic workers rights']

#App layout
app.layout = html.Div(
    #Header
    children=[
        html.Div([
            html.Div([dcc.Link(href='https://www.theengineroom.org/',
                               children = [html.Img(src=dash.get_asset_url('logo.png'), className = "logo")])]),
            html.H1(children="LiTS Data Analytics Dashboard", className = "header-title"),
            html.P(
                children=(

                    "Analyze the distribution of LiTS across time and space! "
                    "Filter by sector, region, and more!"
                ),
                className = "header-description",
            ),
    ], className = "header"),
    #Histogram dropdowns
        html.Div(
        children=[
            html.Div(
                children=[
                    html.Div(children="Region", className="menu-title"),
                    dcc.Dropdown(
                        id="region-filter",
                        options=[
                            {"label": region, "value": region}
                            for region in regions
                        ],
                        value="All Regions",
                        clearable=False,
                        className="dropdown",
                    ),
                ]
            ),
            html.Div(
                children=[
                    html.Div(children="Year", className="menu-title"),
                    dcc.Dropdown(
                        id="year1",
                        options=[
                            {"label": year1, "value": year1}
                            for year1 in years
                        ],
                        value=default_year,
                        clearable=False,
                        className="dropdown",
                    ),
                ]
            ),
        ],
        className="menu",
    ),
    #Histogram graph
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="region-histogram",
                        config={"displayModeBar": False},
                    ),
                    className="card",
                ),
            ],
            className="wrapper",
        ),
    #Pie dropdowns
        html.Div(
        children=[
            html.Div(
                children=[
                    html.Div(children="Pie Divider", className="menu-title"),
                    dcc.Dropdown(
                        id="pie-filter",
                        options=[
                            {"label": pie_div, "value": pie_div}
                            for pie_div in pie_dividers
                        ],
                        value="Type",
                        clearable=False,
                        className="dropdown",
                    ),
                ]
            ),
        html.Div(
            children=[
                html.Div(children="Year", className="menu-title"),
                dcc.Dropdown(
                    id="year2",
                    options=[
                        {"label": year2, "value": year2}
                        for year2 in years
                    ],
                    value=default_year,
                    clearable=False,
                    className="dropdown",
                ),
            ]
        ),
        ],
        className="menu",
        ),
    #Pie graph
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="pie-divided",
                        config={"displayModeBar": False},
                    ),
                    className="card",
                ),
            ],
            className="wrapper",
        ),
    #Map dropdowns
        html.Div(
        children=[
            html.Div(
                children=[
                    html.Div(children="Sector", className="menu-title"),
                    dcc.Dropdown(
                        id="sector-filter",
                        options=[
                            {"label": sector, "value": sector}
                            for sector in sectors
                        ],
                        value="All Sectors",
                        clearable=False,
                        className="dropdown",
                    ),
                ]
            ),
        html.Div(
            children=[
                html.Div(children="Year", className="menu-title"),
                dcc.Dropdown(
                    id="year3",
                    options=[
                        {"label": year3, "value": year3}
                        for year3 in years
                    ],
                    value=default_year,
                    clearable=False,
                    className="dropdown",
                ),
            ]
        ),
    ],
    className="menu",
        ),
    #Map graph
        html.Div(
    children=[
        html.Div(
            children=dcc.Graph(
                id="sector-map",
                config={"displayModeBar": False},
            ),
            className="card",
        ),
    ],
    className="wrapper",
),
    ]
)

@app.callback(
    Output("region-histogram", "figure"),
    Output("pie-divided","figure"),
    Output("sector-map", "figure"),
    Input("region-filter", "value"),
    Input("pie-filter", "value"),
    Input("sector-filter","value"),
    Input("year1","value"),
    Input("year2", "value"),
    Input("year3", "value")
)

def update_charts(region, pie_div, sector, year1, year2, year3):
    #Getting data by year
    data = clean_data(f"{year1}.xlsx")
    #Histogram function
    region_histogram_figure = histogram_function(data, region, year1)
    #Getting data by year
    data = clean_data(f"{year2}.xlsx")
    #Pie function
    pie_divided_figure = pie_function(data,pie_div, year2)
    #Getting data by year
    data = clean_data(f"{year3}.xlsx")
    #Map function
    if sector == "All Sectors":
        sector = None
    sector_map_figure = map_function(data, sector,year3)
    return region_histogram_figure, pie_divided_figure, sector_map_figure

if __name__ == "__main__":
    app.run_server(debug=True)
