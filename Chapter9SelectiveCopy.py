#! usr/bin/env python3

#Chapter 9 Challenge - Selective Copy

#A program that walks through a folder tree and searches for files with a certain
#file extention (such as .pdf or .jpg). Copy these files from their location
#to a new folder.

import os, shutil

#Get directory, extension, and copy location from user
print ('Please input search directory:')
directory = input()
print ('Please input file extension:')
extension = input()
print ('Please input location of new folder:')
location = input()

#Walk through folder tree
for foldernames, subfolders, filenames in os.walk(directory):
    for filename in filenames:
        if filename.endswith(extension):
            shutil.copy(os.path.join(os.path.abspath(foldernames), filename), location)
