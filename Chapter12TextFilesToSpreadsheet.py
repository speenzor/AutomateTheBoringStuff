#! usr/bin/env python3

#Chapter 12 Challenge - Text Files to Spreadsheet

#This program reads the contents of several text files and inserts the contents
#into a spreadsheet, with one line of text per row. The lines of the first
#text file will be in the cells of column A, the lines of the second text
#file will be in the cells of column B, and on and on.

import os, openpyxl

#Get objects
os.chdir('/Users/spencercorwin/Desktop')
wb = openpyxl.Workbook()
sheet = wb.active
fileList = ['text1.txt','text2.txt']

#Nested for loops to write to Excel
for c in range(len(fileList)):
    #Create list of strings from the file
    file = open(os.path.join(os.getcwd(),fileList[c]))
    fileContent = file.readlines()
    #Assign each string in the textList file to a cell
    for r in range(len(fileContent)):
        sheet.cell(row = r+1, column = c+1).value = fileContent[r]

wb.save('testResult.xlsx')
