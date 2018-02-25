#! usr/bin/env python3

"""
Automate the Boring Stuff Chapter 17 Challenge - Identifying Folders on
the Hard Drive

This script will walk through every folder on a hard drive and find potential
photo folders (forgotten folders that may or may not have photos in them). In
this script a 'photo folder' will be any folder where more than half of the
files are photos (ending in .png or .jpg) and be larger than 500 pixels in
width and height. It will print the absolute path of any 'photo folders'.
"""

import os
from PIL import Image

for foldername, subfolders, filenames in os.walk('/'):
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    for filename in filenames:
        
        #Check if the file extension isn't .png or .jpg
        if not (filename.lower().endswith('.png') or filename.lower().endswith('.jpg')):
            numNonPhotoFiles += 1
            continue    #skip the file if not a photo file

        #Open the image file using the Pillow module
        try:
            ImObj = Image.open(filename)
            width, height = ImObj.size
        except:
            continue

        #Check if width and height are larger than 500
        if width >= 500 and height >= 500:
            numPhotoFiles += 1
        else:
            #Image is too small to be a photo
            numNonPhotoFiles += 1

    #If more than half of the files were photos, print the folder path
    if numPhotoFiles > numNonPhotoFiles:
        print('This folder is a photo-folder: %s' % (os.path.join(os.path.abspath('.'))))
