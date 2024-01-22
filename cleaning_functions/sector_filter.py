def sector_filter(cleaned_data,sector_name):
    """
    Input:
        cleaned data: Data cleaned by clean_data
        sector_name: Name of the sector you want to filter for
    Output:
        filtered_data: filtered data that can be passed into histogram_function and map_function
    """
    filtered_data = cleaned_data[cleaned_data['Sectors'].str.contains(sector_name, case = False)]
    return filtered_data
