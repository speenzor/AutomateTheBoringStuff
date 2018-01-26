#! usr/bin/env python3
#Chapter 12 Challenge: Spreadsheet Cell Inverter
#This program inverts the row and column of cells in a spreadsheet

import os, openpyxl, pprint

os.chdir('/Users/spencercorwin/Desktop')
wb = openpyxl.load_workbook('testFile.xlsx')
sheet = wb.active
resultSheet = wb.create_sheet(index=2, title='resultSheet')
sheetData = []

for r in range(0, sheet.max_row):
    sheetData.append([])
    for c in range(0, sheet.max_column):
        sheetData[r].append(sheet.cell(row = r+1, column = c+1).value)
for r in range(0, sheet.max_row):
    for c in range(0, sheet.max_column):
        resultSheet.cell(row = c+1, column = r+1).value = sheetData[r][c]

wb.save('myTestResult.xlsx')
