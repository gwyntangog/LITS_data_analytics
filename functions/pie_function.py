def pie_function(data, pie_div, year):
    """
    Inputs:
        data: data to be used
        pie_div: way of dividing the pie
        year: year of data
    Output:
        pie_divided_figure: pie chart of LiTS in that year divided by category pie_div
    """
    #Imports
    import pandas as pd
    import plotly.express as px
    #Function
    unique_types = data[f'{pie_div}'].unique()
    count_list = []
    label_list = []
    total = data.shape[0]
    for i in unique_types:
        count = data[data[f'{pie_div}'] == i].shape[0]
        count_list.append(count)
        percentage = round(count/total*100,1)
        label_list.append(f"{i} ({percentage}%)")
    pie_divided_figure = px.pie(values = count_list, names = label_list, title = f"Distribution of Clients by {pie_div} in {year}")
    return pie_divided_figure
