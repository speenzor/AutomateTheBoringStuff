#! usr/bin/env python3
#renameDates.py - Rename filenames with American MM-DD-YYYY date format
#to European DD-MM-YYYY.

import shutil, os, re

#Create regex
datePattern = re.compile(r'''^(.*?)
    ((0|1)?\d)-
    ((0|1|2|3)?\d)-
    ((19|20)\d\d)
    (.*?)$
    ''', re.VERBOSE)

#Loop over the files in the working directory.
for amerFilename in os.listdir('.'):
    mo = datePatter.search(amerFilename)

    #Skip files without a date.
    if mo == None:
        continue

    #Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    #Form the European-style filename.
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearParty + afterPart

    #Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    eruoFilename = os.path.join(absWorkingDir, euroFilename)

    #Rename the files.
    print ('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
    #shutil.move(amerFilename, euroFiename) #uncomment after testing
