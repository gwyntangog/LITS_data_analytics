def pie_function(data, pie_div):
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
    pie_divided_figure = px.pie(values = count_list, names = label_list, title = f"Distribution of Clients by {pie_div}")
    return pie_divided_figure
