def map_function(cleaned_data, sector):
       """
       Input:
              filename: Name of excel file.
              sector: Name of sector to filter with.
       Output:
              Heatmap of LiTS cases in countries over time.
       """
       #Imports
       import pandas as pd
       import matplotlib.pyplot as plt
       import numpy as np
       import plotly.express as px
       from iso3166 import countries_by_apolitical_name
       # from cleaning_functions.clean_data import clean_data
       # cleaned_data = clean_data(filename)
       from cleaning_functions.sector_filter import sector_filter
       if sector == None:
              pass
       else:
              cleaned_data = sector_filter(cleaned_data,sector)
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
       regions = [africa, asia, europe, latin_america, northern_america, oceania]
       region_names = ['Africa','Asia','Europe','Latin America and the Caribbean', 'Northern America','Oceania']

       ###Choropleth Heatmap
       compressed = cleaned_data[['Country/Region','Type','When']]
       compressed['Country/Region'] = compressed['Country/Region'].replace('United Kingdom','United Kingdom of Great Britain and Northern Ireland')
       compressed['Country/Region'] = compressed['Country/Region'].replace('United States','United States of America')
       compressed['Country/Region'] = compressed['Country/Region'].replace('Turkey','Türkiye')
       compressed['Country/Region'] = compressed['Country/Region'].replace('Congo [DRC]','Congo, Democratic Republic of the')

       #Making DataFrame
       compressed['Country/Region'] = compressed['Country/Region'].str.upper()
       unique_countries = compressed['Country/Region'].unique()
       time_list = compressed['When'].unique()
       country_list_out = []
       iso_alpha_list_out = []
       time_list_out=[]
       number_list_out = []
       for country in unique_countries:
              for time in time_list:
                     if country == 'NORTH AMERICA':
                            northern_america_copy = list(map(lambda x: x.replace('United States', 'United States of America'), northern_america))
                            for sub_country in northern_america_copy[1:]:
                                   country = sub_country.upper()
                                   dataframe = compressed[np.logical_and(compressed['Country/Region']=='NORTH AMERICA', compressed['When']==time)]
                                   number = dataframe.shape[0]
                                   country_list_out.append(country)
                                   time_list_out.append(time)
                                   number_list_out.append(number)
                                   iso_alpha_list_out.append(countries_by_apolitical_name[f'{country}'].alpha3)
                     elif country == 'EUROPE':
                            europe_copy = list(map(lambda x: x.replace('Czech Republic', 'Czechia'), europe))
                            europe_copy = list(map(lambda x: x.replace('Republic of Moldova', 'Moldova, Republic of'), europe_copy))
                            europe_copy = list(map(lambda x: x.replace('United Kingdom', 'United Kingdom of Great Britain and Northern Ireland'), europe_copy))
                            for sub_country in europe_copy[1:]:
                                   country = sub_country.upper()
                                   dataframe = compressed[np.logical_and(compressed['Country/Region']=='EUROPE', compressed['When']==time)]
                                   number = dataframe.shape[0]
                                   country_list_out.append(country)
                                   time_list_out.append(time)
                                   number_list_out.append(number)
                                   iso_alpha_list_out.append(countries_by_apolitical_name[f'{country}'].alpha3)
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
       choropleth_data = pd.DataFrame(choropleth_dict)
       maximum = choropleth_data['Number'].max()
       if sector:
              choropleth_title = f'LiTS per Country ({sector})'
       else:
              choropleth_title = 'LiTS per Country (All Sectors)'
       fig = px.choropleth(data_frame = choropleth_data, locations='ISO Alpha', color='Number',animation_frame = 'Time',hover_name='Country',
                            projection='natural earth', title=choropleth_title,color_continuous_scale=px.colors.sequential.Reds, range_color = (1,maximum))
       return fig
