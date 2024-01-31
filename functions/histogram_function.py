def histogram_function(data, region, year):
    """
    Input:
        data: data to be used
        region: region to filter by
        year: year of interest
    Output:
        region_histogram_figure: histogram of number of LiTS in that region in that year
    """
    ###Imports
    import pandas as pd
    import plotly.express as px
    from functions.regional_division import regional_division
    import matplotlib.pyplot as plt
    import plotly.graph_objs as go
    ####Regional Divisions
    africa, asia, europe, latin_america, northern_america, oceania = regional_division()
    region_mapping = {'Africa': africa, 'Asia': asia, 'Europe': europe, 'Latin America and the Caribbean': latin_america, 'Northern America': northern_america, 'Oceania': oceania}
    ###Functions
    if region == 'All Regions':
            filtered_data = data
    else:
        filtered_data = data.loc[data['Country/Region'].isin(region_mapping[region])]
        filtered_data = filtered_data.dropna(subset = ['Country/Region'])
    filtered_data['When'] = pd.to_datetime(filtered_data['When'])
    region_histogram_figure = go.Figure(go.Histogram(x=filtered_data["When"], nbinsx = 12))
    region_histogram_figure = region_histogram_figure.update_layout(yaxis_title = "Count", title = f"Distribution of Partners in {region} Over Time ({year})", xaxis = {"title":"Month","tickformat" : '%B', 'nticks':12, 'tickangle':45})
    return region_histogram_figure
