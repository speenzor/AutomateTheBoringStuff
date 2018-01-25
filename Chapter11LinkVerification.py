#Chapter 11- Link Verification
#Given the URL web page, will attempt to download every linked
#page on the page. The program should flag any pages that have
#a 404 “Not Found” status code and print them out as broken links.

import requests, bs4, time

#Get URL
url='https://wsj.com'
#Download page
res = requests.get(url)
#Check to make sure the url is valid
res.raise_for_status()
#Parse
soup = bs4.BeautifulSoup(res.text, 'html.parser')
#Gather all the a tags on the page w/ href elements
linkElems = soup.find_all('a', href = True)
 
for i in range(len(linkElems)):
    try:
        link = requests.get(linkElems[i].get('href'))
        if link.startswith('//'):
            link = 'http:' + link
        elif link.startswith('/'):
            link = 'http:/' + link
        elif link.startswith('#'):
            link = url + link
        if link.status_code == 404:
            print ('This link is broken: ' + linkElems[i].get('href'))
    except:
        print('Non valid link: '+ linkElems[i].get('href'))
