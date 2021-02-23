'''
Data:2019/9/6
Auth:PinXiao
Function:create new worksheet to special google sheet on drive
Reference:https://www.maxlist.xyz/2018/09/25/python_googlesheet_crud/
'''

import pygsheets
import pandas as pd
#authorization
gc = pygsheets.authorize(service_file='HST-AUTO-CREATE-SHEET-e9c890c6fe4c.json')

#open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
spreadsheet = gc.open('test')

worksheet = spreadsheet.add_worksheet(title="new_work_sheet", rows="100", cols="20")

wks_list = spreadsheet.worksheets()
print(wks_list)

print("create new worksheet successfully......")

