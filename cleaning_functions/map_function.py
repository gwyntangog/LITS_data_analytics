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
       from cleaning_functions.sector_filter import sector_filter
       if sector == None:
              pass
       else:
              cleaned_data = sector_filter(cleaned_data,sector)
       # Reference for regional division: https://unstats.un.org/unsd/methodology/m49/
       africa = ['Sub Saharan Africa', 'Algeria','Egypt','Libya','Morocco','Sudan','Tunisia','Western Sahara',
          'British Indian Ocean Territory','Burundi','Comoros','Djibouti','Eritrea','Ethiopia','French Southern Territories','Kenya','Madagascar',
          'Malawi','Mauritius','Mayotte','Mozambique','Reunion','Rwanda','Seychelles','Somalia','South Sudan','Uganda','Tanzania','Zambia','Zimbabwe',
          'Angola','Cameroon','Central African Republic','Congo [Republic]','Congo [DRC]','Equatorial Guinea','Gabon','São Tomé and Príncipe',
          'Botswana','Eswatini','Lesotho','Namibia','South Africa',
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
                     'Belize','Costa Rica','El Salvador','Guatemala','Honduras','Mexico','Nicaragua','Panama',
                     'Argentina','Bolivia','Bouvet Island','Brazil','Chile','Columbia','Ecuador','Falkland Islands','French Guiana','Guyana',
                     'Paraguay','Peru','South Georgia and the South Sandwich Islands','Suriname','Uruguay','Venezuela']
       northern_america = ['North America',
                     'Bermuda','Canada','Greenland','Saint Pierre and Miquelon','United States']
       oceania = ['Australia','Christmas Island','Cocos [Keeling] Islands', 'Heard Island and McDonald Islands','New Zealand','Norfolk Island',
              'Fiji','New Caledonia','Papua New Guinea','Solomon Islands','Vanuatu',
              'Guam','Kiribati','Marshall Islands','Micronesia','Nauru', 'Northern Mariana Islands','U.S. Minor Outlying Islands',
              'American Samoa','Cook Islands','French Polynesia','Niue','Pitcairn','Samoa','Tokelau','Tonga','Tuvalu','Wallis and Futuna']

       ###Conversion of Country Names to ISO3166 Standard. Reference: https://en.wikipedia.org/wiki/ISO_3166-1
       ###Individual Countries

       compressed = cleaned_data[['Country/Region','Type','When']]

       compressed['Country/Region'] = compressed['Country/Region'].replace('United States','United States of America')

       compressed['Country/Region'] = compressed['Country/Region'].replace('Czech Republic', 'Czechia')
       compressed['Country/Region'] = compressed['Country/Region'].replace('Republic of Moldova', 'Moldova, Republic of')
       compressed['Country/Region'] = compressed['Country/Region'].replace('United Kingdom','United Kingdom of Great Britain and Northern Ireland')

       compressed['Country/Region'] = compressed['Country/Region'].replace('Myanmar [Burma]','Myanmar')
       compressed['Country/Region'] = compressed['Country/Region'].replace('Macau', 'Macao')
       compressed['Country/Region'] = compressed['Country/Region'].replace('South Korea', 'Korea, Republic of')
       compressed['Country/Region'] = compressed['Country/Region'].replace('North Korea', "Korea, Democratic People's Republic of")
       compressed['Country/Region'] = compressed['Country/Region'].replace('Brunei', "Brunei Darussalam")
       compressed['Country/Region'] = compressed['Country/Region'].replace('Laos', "Lao People's Democratic Republic")
       compressed['Country/Region'] = compressed['Country/Region'].replace('Vietnam', "Viet Nam")
       compressed['Country/Region'] = compressed['Country/Region'].replace('Iran', "Iran, Islamic Republic of")
       compressed['Country/Region'] = compressed['Country/Region'].replace('Palestinian Territories', "Palestine")
       compressed['Country/Region'] = compressed['Country/Region'].replace('Syria', "Syrian Arab Republic")
       compressed['Country/Region'] = compressed['Country/Region'].replace('Turkey','Türkiye')

       compressed['Country/Region'] = compressed['Country/Region'].replace('British Virgin Islands', 'Virgin Islands, British')
       compressed['Country/Region'] = compressed['Country/Region'].replace('Curacao', 'Curaçao')
       compressed['Country/Region'] = compressed['Country/Region'].replace('Sint Maarten', 'Sint Maarten (Dutch part)')
       compressed['Country/Region'] = compressed['Country/Region'].replace('U.S. Virgin Islands', 'Virgin Islands, U.S.')
       compressed['Country/Region'] = compressed['Country/Region'].replace('Bolivia', 'Bolivia, Plurinational State of')
       compressed['Country/Region'] = compressed['Country/Region'].replace('Columbia', 'Colombia')
       compressed['Country/Region'] = compressed['Country/Region'].replace('Falkland Islands', 'Falkland Islands (Malvinas)')
       compressed['Country/Region'] = compressed['Country/Region'].replace('Venezuela', 'Venezuela, Bolivarian Republic of')

       compressed['Country/Region'] = compressed['Country/Region'].replace('Reunion', 'Réunion')
       compressed['Country/Region'] = compressed['Country/Region'].replace('Tanzania', 'Tanzania, United Republic of')
       compressed['Country/Region'] = compressed['Country/Region'].replace('Congo [Republic]', 'Congo')
       compressed['Country/Region'] = compressed['Country/Region'].replace('Congo [DRC]', 'Congo, Democratic Republic of the')
       compressed['Country/Region'] = compressed['Country/Region'].replace('São Tomé and Príncipe', 'Sao Tome and Principe')
       compressed['Country/Region'] = compressed['Country/Region'].replace('Saint Helena', 'Saint Helena, Ascension and Tristan da Cunha')

       compressed['Country/Region'] = compressed['Country/Region'].replace('Cocos [Keeling] Islands', 'Cocos (Keeling) Islands')
       compressed['Country/Region'] = compressed['Country/Region'].replace('Micronesia', 'Micronesia, Federated States of')
       compressed['Country/Region'] = compressed['Country/Region'].replace('U.S. Minor Outlying Islands', 'United States Minor Outlying Islands')

       ###Northern America
       northern_america_copy = list(map(lambda x: x.replace('United States', 'United States of America'), northern_america))
       ###Europe
       europe_copy = list(map(lambda x: x.replace('Czech Republic', 'Czechia'), europe))
       europe_copy = list(map(lambda x: x.replace('Republic of Moldova', 'Moldova, Republic of'), europe_copy))
       europe_copy = list(map(lambda x: x.replace('United Kingdom', 'United Kingdom of Great Britain and Northern Ireland'), europe_copy))
       ###Asia
       asia_copy = list(map(lambda x: x.replace('Myanmar [Burma]', 'Myanmar'), asia))
       asia_copy = list(map(lambda x: x.replace('Macau', 'Macao'), asia_copy))
       asia_copy = list(map(lambda x: x.replace('South Korea', 'Korea, Republic of'), asia_copy))
       asia_copy = list(map(lambda x: x.replace('North Korea', "Korea, Democratic People's Republic of"), asia_copy))
       asia_copy = list(map(lambda x: x.replace('Brunei', "Brunei Darussalam"), asia_copy))
       asia_copy = list(map(lambda x: x.replace('Laos', "Lao People's Democratic Republic"), asia_copy))
       asia_copy = list(map(lambda x: x.replace('Vietnam', "Viet Nam"), asia_copy))
       asia_copy = list(map(lambda x: x.replace('Iran', "Iran, Islamic Republic of"), asia_copy))
       asia_copy = list(map(lambda x: x.replace('Palestinian Territories', "Palestine"), asia_copy))
       asia_copy = list(map(lambda x: x.replace('Syria', "Syrian Arab Republic"), asia_copy))
       asia_copy = list(map(lambda x: x.replace('Turkey','Türkiye'), asia_copy))
       ###Latin America
       latin_america_copy = list(map(lambda x: x.replace('British Virgin Islands', 'Virgin Islands, British'), latin_america))
       latin_america_copy = list(map(lambda x: x.replace('Curacao', 'Curaçao'), latin_america_copy))
       latin_america_copy = list(map(lambda x: x.replace('Sint Maarten', 'Sint Maarten (Dutch part)'), latin_america_copy))
       latin_america_copy = list(map(lambda x: x.replace('U.S. Virgin Islands', 'Virgin Islands, U.S.'), latin_america_copy))
       latin_america_copy = list(map(lambda x: x.replace('Bolivia', 'Bolivia, Plurinational State of'), latin_america_copy))
       latin_america_copy = list(map(lambda x: x.replace('Columbia', 'Colombia'), latin_america_copy))
       latin_america_copy = list(map(lambda x: x.replace('Falkland Islands', 'Falkland Islands (Malvinas)'), latin_america_copy))
       latin_america_copy = list(map(lambda x: x.replace('Venezuela', 'Venezuela, Bolivarian Republic of'), latin_america_copy))
       ###Africa
       africa_copy = africa.copy()
       africa_copy = list(map(lambda x: x.replace('Reunion', 'Réunion'), africa_copy))
       africa_copy = list(map(lambda x: x.replace('Tanzania', 'Tanzania, United Republic of'), africa_copy))
       africa_copy = list(map(lambda x: x.replace('Congo [Republic]', 'Congo'), africa_copy))
       africa_copy = list(map(lambda x: x.replace('Congo [DRC]', 'Congo, Democratic Republic of the'), africa_copy))
       africa_copy = list(map(lambda x: x.replace('São Tomé and Príncipe', 'Sao Tome and Principe'), africa_copy))
       africa_copy = list(map(lambda x: x.replace('Saint Helena', 'Saint Helena, Ascension and Tristan da Cunha'), africa_copy))
       ###Oceania
       oceania_copy = oceania.copy()
       oceania_copy = list(map(lambda x: x.replace('Cocos [Keeling] Islands', 'Cocos (Keeling) Islands'), oceania_copy))
       oceania_copy = list(map(lambda x: x.replace('Micronesia', 'Micronesia, Federated States of'), oceania_copy))
       oceania_copy = list(map(lambda x: x.replace('U.S. Minor Outlying Islands', 'United States Minor Outlying Islands'), oceania_copy))
       #Making DataFrame
       compressed['Country/Region'] = compressed['Country/Region'].str.upper()
       unique_countries = compressed['Country/Region'].unique()
       time_list = compressed['When'].unique()
       country_list_out = []
       iso_alpha_list_out = []
       time_list_out=[]
       number_list_out = []
       ###CLEANING 1
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
       ###CLEANING 2
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
       maximum = choropleth_data['Number'].max()
       if sector:
              choropleth_title = f'LiTS per Country ({sector})'
       else:
              choropleth_title = 'LiTS per Country (All Sectors)'
       fig = px.choropleth(data_frame = choropleth_data, locations='ISO Alpha', color='Number',animation_frame = 'Time',hover_name='Country',
                            projection='natural earth', title=choropleth_title,color_continuous_scale=px.colors.sequential.Reds, range_color = (0,maximum))
       return fig
