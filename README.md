# LITS_data_analytics

This project was made to analyze time-series data for The Engine Room's Light Touch Support (LiTS) Program.

## Housekeeping

Adding data:

1. For privacy purposes:
    1. Delete all sheets from the Excel file excluding "Internal Reporting Form".
    2. Remove all information under Individual Names and Organization Names (Columns C and D).
2. Rename the file into the year only. (e.g. "2023.xlsx").
3. Make sure the file is in the root directory.

## Deployment

This website is deployed on Render at https://lits-analyst.onrender.com/ .

Deployment details:

1. Under Environment, make sure the python version is 3.10.13 (Key: PYTHON_VERSION, Value: 3.10.13).
2. Under Settings, set Build Command as "$ pip install -r requirements.txt" and Start Command as "$ gunicorn app:server" . Do not include quotation marks.
3. To deploy, click on the "Manual Deploy" dropdown and select "Deploy latest commit".

## Contacts
This code was authored by Gwyneth Margaux Tangog (MIT SB '26). <br />
MIT email: gwynt@mit.edu <br />
Summer email: gwynmgtangog@gmail.com

&copy; Gwyneth Margaux Tangog
