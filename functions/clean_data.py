def clean_data(filename,sheetname = "Internal Reporting Form"):
       """
       Input:
              filname: Name of excel sheet. Example: 'LiTS Tracker - 2023.xlsx'
              sheet_name: Name of sheet in file with the data. Example: 'Internal Reporting Form'
       Output:
              Cleaned data. Column names are changed for readability. Data types are changed for analysis purposes.
       """
       import pandas as pd
       # Reading the file.
       data = pd.read_excel(filename, sheet_name = sheetname)
       # Cleaning the columns.
       #2: Email
       data = data.rename(columns={"Email Address": "Email"})
       #5: Sectors
       data = data.rename(columns={'Sectors that the organisation works in (Mark all that apply, and then mark "Other" to provide more details if applicable.)': "Sectors"})
       #6: Type
       data = data.rename(columns={'Type of organisation': "Type"})
       #7: Scope
       data = data.rename(columns={"Organisation's Scope of Work": "Scope"})
       #8: Country/Region
       data = data.rename(columns={"Country/Region that the organisation or individual is primarily based in ": "Country/Region"})
       #11: How did the LiTS happen? Check all that apply
       data = data.rename(columns={"How did the LiTS happen? Check all that apply": "How"})
       #12: When did the LiTS occur?
       data = data.rename(columns={"When did the LiTS occur? ": "When"})
       data['When'] = pd.to_datetime(data['When']).dt.strftime('%m-%Y')
       #13: Phase Supported
       data = data.rename(columns={"During which phase of the project did we primarily provide support?": "Phase Supported"})
       #14: Output Type
       data = data.rename(columns={"What type of output (format) did you give them? Check all that apply": "Output Type"})
       #15: Information Type
       data = data.rename(columns={"What type of information did you provide? Check all that apply": "Information Type"})
       #16: Level of Support
       data['Level of Support'] = data['Level of Support'].replace('2 - medium (you did all of the "light" activities, plus pro-bono work including research, spending time making connections, or providing inputs to a document)', 'Medium')
       data['Level of Support'] = data['Level of Support'].replace('1 - light (you spent some time talking about an issue, and provided suggestions or connections)', 'Light')
       data['Level of Support'] = data['Level of Support'].replace('3 - heavy (you spent up to one full day of work or more; if more, select "Other" and type in the number of days you spent)', 'Heavy')
       #17: Brief Description
       data = data.rename(columns={"In your own words, briefly describe the problem they are trying to solve or challenge that they are facing.": "Brief Description"})
       #18: Feedback (Y/N)
       data = data.rename(columns={"Did the organisation or individual provide you with feedback on the LiTS process or how they used your advice?": "Feedback (Y/N)"})
       #19: Feedback
       data = data.rename(columns={'If you selected "Yes" please share the feedback from the partner.': "Feedback"})
       #20: Closed/Ongoing
       data = data.rename(columns={'Is the LiTS closed or ongoing?': "Closed/Ongoing"})
       #21: Conversation Description
       data = data.rename(columns={'Please briefly describe the conversation': "Conversation Description"})
       #22: Conclusions/Takeaways
       data = data.rename(columns={'Were there any conclusions or takeaways from the conversation': "Conclusions/Takeaways"})
       #Exporting
       cleaned_data = data.copy()
       return cleaned_data
