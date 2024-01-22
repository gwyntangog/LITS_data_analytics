def pie_function (filename):
    """
    Input:
        filename: filename of output
    Output:
        pie chart with division by Type of Organization
    """
    #Imports
    import pandas as pd
    import matplotlib.pyplot as plt
    from cleaning_functions.clean_data import clean_data
    from cleaning_functions.information_type_filter import information_type_filter
    cleaned_data = clean_data(filename)
    unique_types = cleaned_data['Type'].unique()
    count_list = []
    label_list = []
    total = cleaned_data.shape[0]
    for i in unique_types:
        count = cleaned_data[cleaned_data['Type'] == i].shape[0]
        count_list.append(count)
        percentage = round(count/total*100,1)
        label_list.append(f"{i} ({percentage}%)")

    plt.pie(x=count_list,labels = label_list,labeldistance=1.0)
    plt.savefig(f"Figures/Pie Chart.png")
