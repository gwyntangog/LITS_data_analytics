def iso3166_conversion_function(country):
    """
        Input: Country name
        Output: Country name in ISO3166 standard. Reference: https://en.wikipedia.org/wiki/ISO_3166-1
    """
    conversion_dictionary = {'United States':'United States of America', 'Czech Republic':'Czechia', 'Republic of Moldova' : 'Moldova, Republic of',
                             'United Kingdom':'United Kingdom of Great Britain and Northern Ireland','Myanmar [Burma]':'Myanmar','Macau':'Macao',
                             'South Korea':'Korea, Republic of','North Korea':"Korea, Democratic People's Republic of",'Brunei':"Brunei Darussalam",
                             'Laos':"Lao People's Democratic Republic",'Vietnam':"Viet Nam",'Iran':"Iran, Islamic Republic of",'Palestinian Territories':"Palestine",
                            'Syria':"Syrian Arab Republic", 'Turkey':'Türkiye','British Virgin Islands':'Virgin Islands, British','Curacao':'Curaçao','Sint Maarten':'Sint Maarten (Dutch part)',
                            'U.S. Virgin Islands':'Virgin Islands, U.S.','Bolivia':'Bolivia, Plurinational State of','Columbia':'Colombia','Falkland Islands':'Falkland Islands (Malvinas)',
                            'Venezuela':'Venezuela, Bolivarian Republic of','Reunion':'Réunion','Tanzania':'Tanzania, United Republic of','Congo [Republic]':'Congo','Congo [DRC]':'Congo, Democratic Republic of the',
                            'São Tomé and Príncipe':'Sao Tome and Principe','Saint Helena':'Saint Helena, Ascension and Tristan da Cunha','Cocos [Keeling] Islands':'Cocos (Keeling) Islands',
                            'Micronesia':'Micronesia, Federated States of', 'U.S. Minor Outlying Islands':'United States Minor Outlying Islands'}
    if country in conversion_dictionary.keys():
        return conversion_dictionary[country]
    else:
        return country
