#! usr/bin/env python3
#Chapter 12 Practice Problem: Spreadsheet to Text Files
#This program reads the contents of the cells in an Excel spreadsheet
#then writes the cells of the columns into a text file.

import os, openpyxl

#Get objects
os.chdir('/Users/spencercorwin/Desktop')
wb = openpyxl.load_workbook('testResult.xlsx')
sheet = wb.active

#Read all the rows in one column then go onto the next column
for c in range(0, sheet.max_column):
    #Create new text file
    file = open('textFromColumn'+str(c)+'.txt', 'w')
    for r in range(0, sheet.max_row):
        #Create list of strings in each column
        if sheet.cell(row = r+1, column = c+1).value == None:
            file.write('')
        else:
            file.write(str(sheet.cell(row = r+1, column = c+1).value) + '\n')
    file.close()
