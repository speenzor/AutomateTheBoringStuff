#! usr/bin/env python3

"""
Automate the Boring Stuff Chapter 17 Challenge - Extending and Fixing the
Chapter Project Programs

This script will resize all images in the current working directory to fit
in a 300x300 square, and adds a cat logo to the lower-right corner. The extension
to the original script will not add the cat logo to the image if the logo takes
up half of the image's width or height it will not add the logo.
"""

import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

#Change directory to the Desktop and create a new folder
os.chdir('/Users/spencercorwin/Desktop')
os.makedirs('withLogo', exist_ok=True)

#Loop over all the files in the working directory
for filename in os.listdir('.'):
    
    #Skip over any files that aren't JPEG, PNG, GIF, or BMP types, or the logo image
    if not (filename.lower().endswith('.png') or filename.lower().endswith('.jpg') or filename.lower().endswith('.gif') or filename.lower().endswith('.bmp')) or filename == LOGO_FILENAME:
        continue

    im = Image.open(filename)
    width, height = im.size

    #Check if the image needs to be resized
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        if width > height:
            height = int((SQUARE_FIT_SIZE/width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE/height) * width)
            height = SQUARE_FIT_SIZE

        #Resize the image
        print('Resizing %s...' % (filename))
        im = im.resise((width,height))

        #Add the logo if it's not over half the width or height of the image
        if width >= logoWidth*2 and height >= logoHeight*2:
            print('Adding logo to %s...' % (filename))
            im.paste(logoIm, (width-logoWidth, height-logoHeight), logoIm)
        else:
            print('Logo too big. Skipping %s...' %(filename))

        #Save the changes
        im.save(os.path.join('withLogo', filename))
