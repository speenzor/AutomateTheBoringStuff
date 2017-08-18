#! usr/bin/env python3
#Chapter 9 Deleting Unneeded Files
#A program that walks through a folder tree and if a file in the directory
#is greater than 100MB in size then it sends it to trash.

import os, shutil, send2trash

#Get the directory from user
print ('Please enter directory to search:')
directory = input()

#Walk through folder tree and delete files greater than 100MB in size
for foldername, subfolders, filenames in os.walk(directory):
    for filename in filenames:
        if os.path.getsize(os.path.join(os.path.abspath(foldername),filename)) > 100000000:
            send2trash.send2trash (os.path.join(os.path.abspath(foldername),filename))
            print ('File ' + filename + ' deleted.')
