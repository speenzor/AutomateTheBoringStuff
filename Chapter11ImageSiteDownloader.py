#! usr/bin/env python3

#Chapter 11 Challenge - Image Site Downloader

#This script uses BeautifulSoup to download the first 20 images from a search of imgur.com
import sys, requests, os, bs4

print('Please enter search:')
search= input()

os.chdir('/Users/spencercorwin/Desktop')
os.makedirs('imgur', exist_ok=True)
res = requests.get('http://imgur.com/search?q='+str(search))
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text)
photoElem = soup.select('img')
for i in range(20):
    try:
        photoUrl = 'http:' + photoElem[i].get('src')
        print('Downloading image %s...' % (photoUrl))
        res = requests.get(photoUrl)
        res.raise_for_status()
    except:
        continue
    #Save image to /Desktop/imgur
    photoFile = open(os.path.join('imgur',os.path.basename(photoUrl)),'wb')
    for chunk in res.iter_content(100000):
        photoFile.write(chunk)
    photoFile.close()
