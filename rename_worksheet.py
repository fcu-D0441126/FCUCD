'''
Data:2019/9/6
Auth:PinXiao
Function:rename worksheet to special google sheet on drive
Reference:https://www.maxlist.xyz/2018/09/25/python_googlesheet_crud/
'''

import pygsheets
import pandas as pd
#authorization
gc = pygsheets.authorize(service_file='HST-AUTO-CREATE-SHEET-e9c890c6fe4c.json')

#open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
sheet = gc.open('test')

wks_list = sheet.worksheets()
print(wks_list)

#select the first sheet 
wks = sheet[0]
#wks2 = sht.worksheet_by_title("sheet2")

#更新名稱
wks.title = "test_change_1"

print("Rename successfully......")
