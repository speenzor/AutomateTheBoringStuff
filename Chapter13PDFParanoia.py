#! /usr/bin/env python3

"""
Automate the Boring Stuff Chapter 13 Challenge - PDF Paranoia

This script will go through every PDF in a folder (and its subfolders) and
encrypt the PDFs using a password privded on the command line. Save each
encryped DPF with an _encrypted.pdf suffix added to the original filename.
It will then send the unencrypted file to trash.

The second function does the same thing in reverse. It searches the folder
and subfolders for encrypted files, decryptes them with a given password, and
if the password for a file is incorrect it will tell the use and move to the
next file.
"""

import os
import sys
import send2trash
import PyPDF2

cwd = '/Users/spencercorwin/Desktop/unencryptedPDFs'
os.chdir(cwd)
password = sys.argv[1]

def encryptFolder(cwd, password):
#Get the filename for each file in the given directory
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
                #Delete the original file
                send2trash.send2trash(filename)
            
def decryptFolder(cwd, password):
#Get the filename for each file in the given directory
    for folder,subfolders,filenames in os.walk(cwd):
        for filename in filenames:
            pdfReader = PyPDF2.PdfFileReader(open(filename, 'rb'))  #open the file
            if pdfReader.isEncrypted:   #check if the file is encrypted
                if pdfReader.decrypt(password) == 0:
                    print ('Password for '+filename+' is incorrect.')
                    continue
                else:
                    pdfReader.decrypt(password)
                pdfWriter = PyPDF2.PdfFileWriter()
                for pageNum in range(pdfReader.numPages):
                    pageObj = pdfReader.getPage(pageNum)
                    pdfWriter.addPage(pageObj)
                pdfWriter.encrypt(password)
                resultPDF = open(filename.split('.')[0]+'_decrypted.pdf', 'wb')
                pdfWriter.write(resultPDF)
                resultPDF.close()
