# Omidiora_Emmanuel

Data-Epic project works

# Gspread library Importation (DATAEPIC)

## Scope of Project

The pipeline in this project ingests data from google sheeet, transforms it and loads it.
USUALLY this type of task is done using more laborious methods.

## Tools

- GSpread - API SDK for Google Sheets
- Jupyter - Notebook and lab tests
- Pandas - Handling small logics for data prepration

### Enable API access

- Go to your GCP Console and create a new project (or select the one you already have).
- In the box labeled “Search for APIs and Services”, search for “Google Drive API” and enable it.
- Go to “APIs & Services > Credentials” and choose “Create credentials > Service account key”.
- Fill out the form
- Click “Create” and “Done”.
- Press “Manage service accounts” above Service Accounts.
- Press on ⋮ near recently created service account and select “Manage keys” and then click on “ADD KEY" and Create new key”.
- Select JSON key type and press “Create”.
- This will automatically download a json file.
- Open the file and copy the client email
- Go to your spreadsheet and share it with this client-email, Just like you do with any other Google account
- Rename the file to service_account.json
- Store the json file in the directory of your gspread installation.

## Data

- Input data for is `KOWOPE.csv`

### Environment Variables

create an `.env` file to store all the variables needed to run this script successfully.

Run `python  .env` to create the file.
Copy the following into the file and replace with your details.

```
email = <replace with email>
service_file_path = <replace with file_path to secret.json>
sheet_title = <replace with sheet_title>
worksheet_title = <replace with worksheet_title>
file_path = <replace with file path>
```

## Workflow

`gspread_project.py` is the main script. This script takes as input;
## Kowope.csv

Output;
## data\Kowope.csv
##
##
##

The main script creates a new google spreadsheet. It then load the dataset into a pandas dataframe. The dataframe is thereafter used to fill the google worksheet.

To run the script, run
`   python gspread_project.py
  `
