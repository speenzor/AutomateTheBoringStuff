#! usr/bin/env python3
#Chapter 8 Practive Project- Regex Search- This is a program that
#opens all .txt files in a folder and searches for any line that
#matches a user-supplied regular expression. The results will print to
#the screen

#Import dependencies
import os, re, pprint

#Ask for pathway for the folder where the .txt files are
print ('Please provide the folder pathway:')
pathway = input()
while os.path.isdir(pathway) == False:
    print ('Please provide the folder pathway:')
    pathway = input()
    if os.path.isdir(pathway) == True:
        print ('Pathway stored')
        break

#Ask for the user-supplied regex
print('Please provide your regular expression:')
inputRegex = str(input())

#Create regex
userRegex = re.compile(inputRegex)

#Make list of files in the pathway
fileList = os.listdir(pathway)

#Open the files. Read the files. Put all the text into a string
folderContent = ''
for i in range(len(fileList)):
    fileNext = open(pathway + '/' + fileList[i])
    fileNextContent = fileNext.read()
    folderContent = folderContent + fileNextContent
    #Close file? (pathway + str(fileList[i])).close()

#Search string for regex
findAll = userRegex.findall(folderContent)
finalPrint = ' '.join(findAll)

#Print string
print (finalPrint)
