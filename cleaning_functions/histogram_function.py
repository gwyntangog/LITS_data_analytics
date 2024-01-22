

def histogram_function(filename, information_type= None):
    """
    Input:
       filename: filename of output
       information_type: information to filter for. Choose one of the following:
      1. General information about The Engine Room
      2. Feedback on a proposal or application
      3. Partnership - Connections to peers or experts
      4. Project - Help with project design or implementation
      5. Project - Mapping of comparable projects or provision of lateral insipring examples
      6. Policy & Advocacy - Feedback on contextual analysis or political economy
      7. Policy & Advocacy - Feedback on advocacy strategy or projects
      8. Technical - Feedback and recommendations on a platform/website
      9. Technical - Feedback on Designs / Mockups / Wireframes
      10. Technical - Resources, Learnings or Guidelines
      11. Responsible Data - Resources and Learnings
      12. Responsible Data - Guidance or Feedback on RD policies
      13. OrgSec - Guidance or Feedback on Policies
      14. OrgSec - Resources, Learnings or Tools
      15. OrgSec - Connections with Support and / or Expertise
    Output:
       6 histograms of the number of LiTS per 6 regions over time.
    """
    #Imports
    import pandas as pd
    import matplotlib.pyplot as plt
    from cleaning_functions.clean_data import clean_data
    from cleaning_functions.information_type_filter import information_type_filter
    cleaned_data = clean_data(filename)
    if information_type == None:
        information_type_name = "All Information Types"
    else:
        cleaned_data = information_type_filter(cleaned_data,information_type)
        information_type_name = information_type
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
    northern_america = ['North America','Bermuda','Canada','Greenland','Saint Pierre and Miquelon','United States']
    oceania = ['Australia','Christmas Island','Cocos [Keeling] Islands', 'Heard Island and McDonald Islands','New Zealand','Norfolk Island',
              'Fiji','New Caledonia','Papua New Guinea','Solomon Islands','Vanuatu',
              'Guam','Kiribati','Marshall Islands','Micronesia','Nauru', 'Northern Mariana Islans','U.S. Minor Outlying Islands',
              'American Samoa','Cook Islands','French Polynesia','Niue','Pitcairn','Samoa','Tokelau','Tonga','Tuvalu','Wallis and Futuna']
    regions = [africa, asia, europe, latin_america, northern_america, oceania]
    region_names = ['Africa','Asia','Europe','Latin America and the Caribbean', 'Northern America','Oceania']
    for i in range(len(regions)):
       region = regions[i]
       region_data = cleaned_data.loc[cleaned_data['Country/Region'].isin(region)]
       region_data = region_data.dropna(subset = ['Country/Region'])
       region_name = region_names[i]
       plt.hist(x='When', data = region_data)
       plt.title(f"LiTS in {region_name} over time ({information_type_name})")
       plt.xlabel("Month")
       plt.ylabel("Number of LiTS")
       plt.savefig(f"Figures/{region_name} Count ({information_type_name}).png")
       plt.clf()
