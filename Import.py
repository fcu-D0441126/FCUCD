'''
Data:2019/9/6
Auth:PinXiao
Function:import data from special google sheet on drive
'''

import pygsheets
import pandas as pd
#authorization
gc = pygsheets.authorize(service_file='HST-AUTO-CREATE-SHEET-e9c890c6fe4c.json')

#open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
spreadsheet = gc.open('test')

title_name = input("title_name:")
worksheet = spreadsheet.add_worksheet(title=title_name, rows="100", cols="20")

wks_list = spreadsheet.worksheets()
print(wks_list)

print("create new worksheet successfully......")


# Create empty dataframe
df = pd.DataFrame()

# Create a column
df['姓名'] = ['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1uhIIU9TkY7_IEznEr7AePlCMKHKs4d1HKjAO-1-fiKw/edit#gid=167092850","社員表!C2:C20")']

#輸出測試
print(df['姓名'])

#select the first sheet 
wks2 = spreadsheet.worksheet_by_title(title_name)

#update the first sheet with df, starting at cell B2. 
wks2.set_dataframe(df,(1,1))