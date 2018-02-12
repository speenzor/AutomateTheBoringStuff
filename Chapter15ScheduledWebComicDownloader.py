#! /usr/bin/env python3

"""Automate the Boring Stuff - Chapter 15 - Scheduled Web Comic Downloader
by Spencer Corwin 02/08/18

This is a program that checks the websites of several web comics and automatically
downloads the images if the comic was updated since the program's last visit. The program will download any new comics
to a folder on the desktop"""

import requests, os, bs4, threading, shelve

os.chdir('/Users/spencercorwin/Desktop')    #set directory to Desktop
os.makedirs('New Images', exist_ok=True)    #store new comics in this new folder

if not os.path.exists('oldUrlsFile.db'):
    oldUrls = []        #this list will be used to store the Urls of the already downloaded comics
    shelfFile = shelve.open('oldUrlsFile')
    shelfFile['oldUrls'] = oldUrls
    shelfFile.close()

def downloadNewComics(website):
    #Download the page.
    print('Downloading page http://%s...' % (website))
    res = requests.get('http://%s' % (website))
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'lxml')

    #Find the URL of the comic image
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image')
    else:
        comicUrl = comicElem[0].get('src')
        shelfFile = shelve.open('oldUrlsFile')
        oldUrls = shelfFile['oldUrls']
        shelfFile.close()
        if comicUrl not in oldUrls:
            #Download the image if it doesn't exist in the oldUrls list
            print('Downloading image %s...' % (comicUrl))
            res.raise_for_status()

            #Save the image to ./Desktop/New Images
            imageFile = open(os.path.join('New Images',os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

            #Updated the oldUrls list with the new url
            oldUrls.append(comicUrl)
            shelfFile = shelve.open('oldUrlsFile')
            shelfFile['oldUrls'] = oldUrls
            shelfFile.close()
        else:
            print('Comic image on http://%s is old' % website)


#Create and start the Thread objects.
downloadThreads = []        #a list of all the Thread objects
comicWebsites =['xkcd.com','lefthandedtoons.com','bizzaro.com','buttersafe.com']
for comicSite in comicWebsites:
    downloadThread = threading.Thread(target=downloadNewComics, args=([comicSite]))
    downloadThreads.append(downloadThread)
    downloadThread.start()

#Wait for all threads to end.
for downloadThread in downloadThreads:
    downloadThread.join()
print('Done for today.')
