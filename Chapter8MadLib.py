#! usr/bin/env python3
#Chapter 8 Practice Project- Create a Mad Lib program that reads in text files
#and lets the user add their own text anywhere ADJECTIVE, NOUN, ADVERB, or VERB
#appears in the text file.

import sys, os, pyperclip, shelve, re

#Read in text file
madLibFile = open('/Users/spencercorwin/madLib.txt')

#Read content of file
madLibContent = madLibFile.read()

#Look for keywords. Make a list of the keywords
nounRegex = re.compile(r'NOUN')
adjRegex = re.compile(r'ADJECTIVE')
verbRegex = re.compile(r'VERB')
adverbRegex = re.compile(r'ADVERB')

madLibNounList = nounRegex.findall(madLibContent)
madLibAdjList = adjRegex.findall(madLibContent)
madLibVerbList = verbRegex.findall(madLibContent)
madLibAdverbList = adverbRegex.findall(madLibContent)

madLibList = madLibNounList + madLibAdjList + madLibVerbList + madLibAdverbList

#Create loop asking for each keyword and store each entered word in shelve file
madLibShelf = shelve.open('madLibData')

for i in range(len(madLibList)):
    if madLibList[i] == 'ADJECTIVE' or madLibList[i] == 'ADVERB':
        print ('Please enter an ' + str(madLibList[i]) + ':') #fix string and lower
        madLibShelf[str(i)]=str(input())
    else:
        print ('Please enter a ' + str(madLibList[i]) + ':') #fix string and lower
        madLibShelf[str(i)]=str(input())

#Create new string to be placed in new file
madLibString2 = madLibContent
for i in range(len(madLibList)):
    madLibString2 = madLibString2.replace(str(madLibList[i]), str(madLibShelf[str(i)]), 1)

#Create new file with new string
madLibFile2 = open('madLib2.txt', 'w')
madLibFile2.write(madLibString2)

#Close shelve file and close new .txt file
madLibShelf.close()
madLibFile2.close()
