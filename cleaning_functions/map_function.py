def map_function(cleaned_data, sector, year):
       """
       Input:
              filename: Name of excel file.
              sector: Name of sector to filter with.
       Output:
              Heatmap of LiTS cases in countries over time.
       """
       #Imports
       import pandas as pd
       import numpy as np
       import plotly.express as px
       from iso3166 import countries_by_apolitical_name
       from cleaning_functions.sector_filter import sector_filter
       from cleaning_functions.iso3166_conversion_function import iso3166_conversion_function
       from cleaning_functions.regional_division import regional_division

       #Sector filter
       if sector == None:
              pass
       else:
              cleaned_data = sector_filter(cleaned_data,sector)

       #Countries and Regions
       africa, asia, europe, latin_america, northern_america, oceania = regional_division()
       compressed = cleaned_data[['Country/Region','Type','When']]

       iso3166_converted_list = []
       for country in list(compressed['Country/Region']):
              iso3166_converted_list.append(iso3166_conversion_function(country))
       compressed['Country/Region'] = iso3166_converted_list

       ###Northern America
       northern_america_copy = []
       for country in northern_america:
              northern_america_copy.append(iso3166_conversion_function(country))

       ###Europe
       europe_copy = []
       for country in europe:
              europe_copy.append(iso3166_conversion_function(country))

       ###Asia
       asia_copy = []
       for country in asia:
              asia_copy.append(iso3166_conversion_function(country))

       ###Latin America
       latin_america_copy = []
       for country in latin_america:
              latin_america_copy.append(iso3166_conversion_function(country))

       ###Africa
       africa_copy = []
       for country in africa:
              africa_copy.append(iso3166_conversion_function(country))

       ###Oceania
       oceania_copy = []
       for country in oceania:
              oceania_copy.append(iso3166_conversion_function(country))

       #Making DataFrame
       no_data = False
       if len(list(compressed['Country/Region'])) == 0:
              no_data = True
       else:
              compressed['Country/Region'] = compressed['Country/Region'].str.upper()
       unique_countries = compressed['Country/Region'].unique()
       time_list = compressed['When'].unique()
       country_list_out = []
       iso_alpha_list_out = []
       time_list_out=[]
       number_list_out = []

       #Cleaning 1: Breaking regions into countries
       for country in unique_countries:
              for time in time_list:
                     if country == 'NORTH AMERICA':
                            for sub_country in northern_america_copy[1:]:
                                   sub_country = sub_country.upper()
                                   dataframe = compressed[np.logical_and(compressed['Country/Region']=='NORTH AMERICA', compressed['When']==time)]
                                   number = dataframe.shape[0]
                                   country_list_out.append(sub_country)
                                   time_list_out.append(time)
                                   number_list_out.append(number)
                                   iso_alpha_list_out.append(countries_by_apolitical_name[f'{sub_country}'].alpha3)
                     elif country == 'EUROPE':
                            for sub_country in europe_copy[1:]:
                                   sub_country = sub_country.upper()
                                   dataframe = compressed[np.logical_and(compressed['Country/Region']=='EUROPE', compressed['When']==time)]
                                   number = dataframe.shape[0]
                                   country_list_out.append(sub_country)
                                   time_list_out.append(time)
                                   number_list_out.append(number)
                                   iso_alpha_list_out.append(countries_by_apolitical_name[f'{sub_country}'].alpha3)
                     elif country == 'ASIA':
                            for sub_country in asia_copy[1:]:
                                   sub_country = sub_country.upper()
                                   dataframe = compressed[np.logical_and(compressed['Country/Region']=='ASIA', compressed['When']==time)]
                                   number = dataframe.shape[0]
                                   country_list_out.append(sub_country)
                                   time_list_out.append(time)
                                   number_list_out.append(number)
                                   iso_alpha_list_out.append(countries_by_apolitical_name[f'{sub_country}'].alpha3)
                     elif country == 'LATIN AMERICA':
                            for sub_country in latin_america_copy[1:]:
                                   sub_country = sub_country.upper()
                                   dataframe = compressed[np.logical_and(compressed['Country/Region']=='LATIN AMERICA', compressed['When']==time)]
                                   number = dataframe.shape[0]
                                   country_list_out.append(sub_country)
                                   time_list_out.append(time)
                                   number_list_out.append(number)
                                   iso_alpha_list_out.append(countries_by_apolitical_name[f'{sub_country}'].alpha3)
                     elif country == 'SUB SAHARAN AFRICA':
                            for sub_country in africa_copy[1:]:
                                   sub_country = sub_country.upper()
                                   dataframe = compressed[np.logical_and(compressed['Country/Region']=='SUB SAHARAN AFRICA', compressed['When']==time)]
                                   number = dataframe.shape[0]
                                   country_list_out.append(sub_country)
                                   time_list_out.append(time)
                                   number_list_out.append(number)
                                   iso_alpha_list_out.append(countries_by_apolitical_name[f'{sub_country}'].alpha3)
                     elif country == 'OCEANIA':
                            for sub_country in oceania_copy[1:]:
                                   sub_country = sub_country.upper()
                                   dataframe = compressed[np.logical_and(compressed['Country/Region']=='OCEANIA', compressed['When']==time)]
                                   number = dataframe.shape[0]
                                   country_list_out.append(sub_country)
                                   time_list_out.append(time)
                                   number_list_out.append(number)
                                   iso_alpha_list_out.append(countries_by_apolitical_name[f'{sub_country}'].alpha3)
                     else:
                            dataframe = compressed[np.logical_and(compressed['Country/Region']==country, compressed['When']==time)]
                            number = dataframe.shape[0]
                            country_list_out.append(country)
                            time_list_out.append(time)
                            number_list_out.append(number)
                            iso_alpha_list_out.append(countries_by_apolitical_name[f'{country}'].alpha3)
       choropleth_dict = {
              'Country': country_list_out, 'Time': time_list_out, 'ISO Alpha':iso_alpha_list_out,'Number':number_list_out
       }
       intermediate_data = pd.DataFrame(choropleth_dict)

       #Cleaning 2: Removing double counting from breaking the regions into countries
       country_list = intermediate_data['Country'].unique()
       time_list = intermediate_data['Time'].unique()
       country_out = []
       time_out = []
       iso_out = []
       count_out = []
       for country in country_list:
              for time in time_list:
                     dataframe = intermediate_data[np.logical_and(intermediate_data['Country']==country, intermediate_data['Time']==time)]
                     count = dataframe['Number'].sum()
                     country_out.append(country)
                     time_out.append(time)
                     iso_out.append(countries_by_apolitical_name[f'{country}'].alpha3)
                     count_out.append(count)
       final_dict = {
              'Country': country_out, 'Time': time_out, 'ISO Alpha':iso_out,'Number':count_out
       }
       choropleth_data = pd.DataFrame(final_dict)

       #Plotting
       maximum = choropleth_data['Number'].max()
       if sector:
              choropleth_title = f'LiTS per Country ({sector}) in {year}'
       else:
              choropleth_title = f'LiTS per Country (All Sectors) in {year}'
       if no_data:
              choropleth_title = f"No LiTS in {sector} in {year}"
       else:
              pass
       fig = px.choropleth(data_frame = choropleth_data, locations='ISO Alpha', color='Number',animation_frame = 'Time',hover_name='Country',
                            projection='natural earth', title=choropleth_title,color_continuous_scale=px.colors.sequential.Reds, range_color = (0,maximum))
       return fig
