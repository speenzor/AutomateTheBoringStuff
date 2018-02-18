#! usr/bin/env python3

#Chapter 12 Challenge - Blank Row Inserter

#This program takes two integers and a filename as command line arguments.
#It then inserts blank rows in an Excel sheet based on an input row number.
#The first integer is the row, the second integer is how many blank rows to
#insert. With a large number of rows and columns this can take some time.

import os, sys, openpyxl

insertrow = sys.argv[1]
blankrows = sys.argv[2]
filename = sys.argv[3]
os.chdir('/Users/spencercorwin/Desktop')
wb = openpyxl.load_workbook(filename)
sheet = wb.active
newwb = openpyxl.Workbook()
newsheet = newwb.active

for r in range(1, int(insertrow)):
    for c in range(1, sheet.max_column):
        newsheet.cell(row = r, column = c).value = sheet.cell(row = r, column = c).value
for r in range(int(insertrow)+int(blankrows), sheet.max_row+int(blankrows)):
    for c in range(1, sheet.max_column):
        newsheet.cell(row = r, column = c).value = sheet.cell(row = r, column = c).value

newwb.save('filename' + 'Result.xlsx')
