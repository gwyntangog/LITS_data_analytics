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
    from cleaning_functions.regional_division import regional_division
    ####Regional Divisions
    africa, asia, europe, latin_america, northern_america, oceania = regional_division()
    region_mapping = {'Africa': africa, 'Asia': asia, 'Europe': europe, 'Latin America and the Caribbean': latin_america, 'Northern America': northern_america, 'Oceania': oceania}
    ###Functions
    if region == 'All Regions':
            filtered_data = data
    else:
        filtered_data = data.loc[data['Country/Region'].isin(region_mapping[region])]
        filtered_data = filtered_data.dropna(subset = ['Country/Region'])
    region_histogram_figure = px.histogram(filtered_data,x="When", nbins = 12, title = f"Distribution of Clients in {region} Over Time ({year})")
    region_histogram_figure = region_histogram_figure.update_layout(yaxis_title = "Count")
    return region_histogram_figure
