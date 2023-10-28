import os
import gspread
import pytest
from main import *

def gs_sheet():
    gs_sheet = gspread.service_account()

    assert gs_sheet
    
def test_open_spreadsheet():
    assert open_spreadsheet("KWOPE")

def test_create_emptysheet():
    """
    tests the create spreadsheet function
    """

    assert open_spreadsheet(True)
    assert create_spreadsheet(gc, title)
   
def test_load_file_into_dataframe():
    """
    tests the load dataframe function
    """
    assert type(df) == pd.DataFrame

        
