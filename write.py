'''
Data:2019/9/6
Auth:PinXiao
Function:upload new data to special google sheet on drive
'''

import pygsheets
import pandas as pd
#authorization
gc = pygsheets.authorize(service_file='HST-AUTO-CREATE-SHEET-e9c890c6fe4c.json')

# Create empty dataframe
df = pd.DataFrame()

# Create a column
df['欄位名稱'] = ['A', 'B', 'finish']

#輸出測試
print(df['欄位名稱'])

#open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
sheet = gc.open('test')

#select the first sheet 
worksheets = sheet[0]

#update the first sheet with df, starting at cell B2. 
worksheets.set_dataframe(df,(1,1))
