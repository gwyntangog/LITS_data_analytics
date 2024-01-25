def regional_division():
    """
    Input: No input
    Output: Regional divisions into 6 UN regions. Reference: https://unstats.un.org/unsd/methodology/m49/
    """
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
    oceania = ['Oceania','Australia','Christmas Island','Cocos [Keeling] Islands', 'Heard Island and McDonald Islands','New Zealand','Norfolk Island',
            'Fiji','New Caledonia','Papua New Guinea','Solomon Islands','Vanuatu',
            'Guam','Kiribati','Marshall Islands','Micronesia','Nauru', 'Northern Mariana Islands','U.S. Minor Outlying Islands',
            'American Samoa','Cook Islands','French Polynesia','Niue','Pitcairn','Samoa','Tokelau','Tonga','Tuvalu','Wallis and Futuna']
    return africa, asia, europe, latin_america, northern_america, oceania
