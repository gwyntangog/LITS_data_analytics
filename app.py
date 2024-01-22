# app.py
from cleaning_functions.clean_data import clean_data
from cleaning_functions.map_function import map_function
import pandas as pd
from dash import Dash, dcc, html, Input, Output
import matplotlib.pyplot as plt
import plotly.express as px


data = clean_data("LiTS Tracker - 2023.xlsx")

external_stylesheets = [
    {
        "href": (
            "http://fonts.googleapis.com/css?family=Roboto"
        ),
        "rel": "stylesheet",
    },
]
app = Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "LiTS Data Analyst"
# Reference for regional division: https://unstats.un.org/unsd/methodology/m49/
africa = ['Sub Saharan Africa', 'Algeria','Egypt','Libya','Morocco','Sudan','Tunisia','Western Sahara',
          'British Indian Ocean Territory','Burundi','Comoros','Djibouti','Eritrea','Ethiopia','French Southern Territories','Kenya','Madagascar',
          'Malawi','Mauritius','Mayotte','Mozambique','Reunion','Rwanda','Seychelles','Somalia','South Sudan','Uganda','Tanzania','Zambia','Zimbabwe'
          'Angola','Cameroon','Central African Republic','Congo [Republic]','Congo [DRC]','Equatorial Guinea','Gabon','São Tomé and Príncipe'
          'Botswana','Eswatini','Lesotho','Namibia','South Africa'
          'Benin','Burkina Faso','Cabo Verde',"Côte d'Ivoire",'Gambia','Ghana','Guinea','Guinea-Bissau','Liberia','Mali','Mauritania','Niger','Nigeria','Saint Helena','Senegal','Sierra Leone','Togo']
asia = ['Asia','Kazakhstan','Kyrgyzstan','Tajikistan','Turkmenistan','Uzbekistan',
        'China','Hong Kong','Macau','South Korea','North Korea','Japan','Mongolia',
        'Brunei','Cambodia','Indonesia','Laos','Malaysia','Myanmar','Philippines','Singapore','Thailand','Timor-Leste','Vietnam',
        'Afghanistan','Bangladesh','Bhutan','India','Iran','Maldives','Nepal','Pakistan','Sri Lanka',
        'Armenia','Azerbaijan','Bahrain','Cyprus','Georgia','Iraq','Israel','Jordan','Kuwait','Lebanon','Oman','Qatar','Saudi Arabia',
        'Palestinian Territories','Syria','Turkey','United Arab Emirates','Yemen']
europe = ['Europe','Belarus','Bulgaria','Czech Republic','Hungary','Poland','Republic of Moldova','Romania','Russian Federation','Slovakia','Ukraine',
          'Denmark','Estonia','Faroe Islands','Finland','Guernsey','Iceland','Ireland','Isle of Man','Jersey','Latvia','Lithuania','Norway','Svalbard and Jan Mayen', 'Sweden',
          'United Kingdom','Ireland','Albania','Andorra','Bosnia and Herzegovina','Croatia','Gibraltar','Greece','Holy See','Italy','Malta','Montenegro','North Macedonia','Portugal',
          'San Marino','Serbia','Slovenia','Spain',
          'Austria','Belgium','France','Germany','Liechtenstein','Luxembourg','Monaco','Netherlands','Switzerland']
latin_america = ['Latin America',
                 'Anguilla','Antigua and Barbuda','Aruba','Bahamas','Barbados','Bonaire, Sint Eustatius and Saba', 'British Virgin Islands',
                 'Cayman Islands','Cuba','Curacao','Dominica','Dominican Republic','Grenada','Guadeloupe','Haiti','Jamaica',
                 'Martinique','Montserrat','Puerto Rico','Saint Kitts and Nevis','Saint Lucia','Saint Vincent and the Grenadines',
                 'Sint Maarten','Trinidad and Tobago','Turks and Caicos Islands','U.S. Virgin Islands',
                 'Belize','Costa Rica','El Salvador','Guatemala','Hondura','Mexico','Nicaragua','Panama',
                 'Argentina','Bolivia','Bouvet Island','Brazil','Chile','Columbia','Ecuador','Falkland Islands','French Guiana','Guyana',
                 'Paraguay','Peru','South Georgia and the Sound Sandwich Islands','Suriname','Uruguay','Venezuela']
northern_america = ['North America',
                    'Bermuda','Canada','Greenland','Saint Pierre and Miquelon','United States']
oceania = ['Australia','Christmas Island','Cocos [Keeling] Islands', 'Heard Island and McDonald Islands','New Zealand','Norfolk Island',
           'Fiji','New Caledonia','Papua New Guinea','Solomon Islands','Vanuatu',
           'Guam','Kiribati','Marshall Islands','Micronesia','Nauru', 'Northern Mariana Islans','U.S. Minor Outlying Islands',
           'American Samoa','Cook Islands','French Polynesia','Niue','Pitcairn','Samoa','Tokelau','Tonga','Tuvalu','Wallis and Futuna']
region_mapping = {'Africa': africa, 'Asia': asia, 'Europe': europe, 'Latin America and the Caribbean': latin_america, 'Northern America': northern_america, 'Oceania': oceania}
regions = ['All Regions', 'Africa','Asia','Europe','Latin America and the Caribbean', 'Northern America','Oceania']
pie_dividers = ['Type','Level of Support']
sectors = ["All Sectors", 'Transparency and accountability / open government','Human rights / humanitarian', 'Philanthropy', 'Environmental justice', 'Civic Tech', 'Health', 'Sex worker rights', 'Gender-based violence',
           'Digital Security', 'Mental Health','Legal Empowerment','Communications','Gender','Racial Justice','Migration Justice','Domestic workers rights']

app.layout = html.Div(
    ###HEADER
    children=[
        html.Div([
            html.H1(children="LiTS Data Analytics Dashboard", className = "header-title"),
            html.P(
                children=(
                    "Analyze the distribution of LiTS across time and space! "
                    "Filter by sector, region, and more!"
                ),
                className = "header-description",
            ),
    ], className = "header"),
    ###HIST DROPDOWNS###
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
            ],
            className="menu",
        ),
    ### HISTOGRAM GRAPHS
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
    ###PIE DROPDOWNS###
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
            ],
            className="menu",
        ),
            ### PIE GRAPH
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
            ###MAP DROPDOWNS###
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
            ],
            className="menu",
        ),
        ###MAP GRAPH
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
    Input("sector-filter","value")
)
def update_charts(region, pie_div, sector):
    ###HISTOGRAM
    if region == 'All Regions':
        filtered_data = data
    else:
        filtered_data = data.loc[data['Country/Region'].isin(region_mapping[region])]
        filtered_data = filtered_data.dropna(subset = ['Country/Region'])
    region_histogram_figure = px.histogram(filtered_data,x="When", nbins = 12, title = f"Distribution of Clients in {region} Over Time")
    ###PIE CHART
    unique_types = data[f'{pie_div}'].unique()
    count_list = []
    label_list = []
    total = data.shape[0]
    for i in unique_types:
        count = data[data[f'{pie_div}'] == i].shape[0]
        count_list.append(count)
        percentage = round(count/total*100,1)
        label_list.append(f"{i} ({percentage}%)")
    pie_divided_figure = px.pie(values = count_list, names = label_list, title = f"Distribution of Clients by {pie_div}")
    ###MAP CHART
    if sector == "All Sectors":
        sector = None
    sector_map_figure = map_function(data, sector)
    return region_histogram_figure, pie_divided_figure, sector_map_figure

if __name__ == "__main__":
    app.run_server(debug=True)
