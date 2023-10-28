
import os
import gspread
import pandas as pd
import logging
from dotenv import load_dotenv


#make sure to share the mail(found in the json file key) of your gcp service, share that with the google sheet
logging.basicConfig(level=logging.INFO)

load_dotenv()
GSPREAD_KEY = os.getenv('PR_KEY')

def main():
    # intialize google sheets config

    gc = gspread.service_account()
    
    
    #connect to the google sheet
    worksheet = gc.open("KOWOPE").sheet1

    logging.info("new worksheet loaded successfully")
    return worksheet

# @functools.wraps(main)
def create_dataframe(worksheet):
    """
    this function loads worksheet into a dataframe
    """
    
    # get all records needed in json format
    sheet = worksheet.get_all_records()
    # create dataframe with the data
    df = pd.DataFrame(sheet)
    
    logging.info("Dataframe created succesfully")
    return df

   
def create_emptysheet(Spreadsheet, rows=100, cols=20):
    #create an empty sheet
    try:
        sheet_empty = gc.create('Spreadsheet')
    except:
        #  A new worksheet for new data.
        worksheet2 = sheet_empty.add_worksheet(Spreadsheet, rows, cols)
        logging.info("worksheet successfully created")
    return worksheet2

def populate_worksheet(worksheet2, df):
    """
    this function populates the new worksheet with data from dataframe:df
    """
    worksheet2.update([df.columns.values.tolist()] + df.values.tolist())
    logging.info("new worksheet successfully updated")


if __name__ == "__main__":
    main()