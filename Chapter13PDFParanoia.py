#! /usr/bin/env python3

"""
Automate the Boring Stuff Chapter 13 Challenge - PDF Paranoia

This script will go through every PDF in a folder (and its subfolders) and
encrypt the PDFs using a password privded on the command line. Save each
encryped DPF with an _encrypted.pdf suffix added to the original filename.
It will then delete the unencrypted file.
"""

import os
import sys
import PyPDF2

cwd = '/Users/spencercorwin/Desktop/decryptedPDFs'
os.chdir(cwd)
password = sys.argv[1]

#Get the filename for each file in the given directory (assumes no subfolders)
for folder,subfolders,filenames in os.walk(cwd):
    for filename in filenames:
        pdfReader = PyPDF2.PdfFileReader(open(filename, 'rb'))  #open the file
        if not pdfReader.isEncrypted:   #check if its already encrypted
            pdfWriter = PyPDF2.PdfFileWriter()
            for pageNum in range(pdfReader.numPages):
                pageObj = pdfReader.getPage(pageNum)
                pdfWriter.addPage(pageObj)
            pdfWriter.encrypt(password)
            resultPDF = open(filename.split('.')[0]+'_encrypted.pdf', 'wb')
            pdfWriter.write(resultPDF)
            resultPDF.close()
