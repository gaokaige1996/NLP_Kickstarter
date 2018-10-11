from bs4 import BeautifulSoup
from lxml import etree
import urllib.request
import re
import math

def risk(url,n):
    #url = 'https://www.kickstarter.com/projects/337373206/my-first-solo-album-the-long-awaited-dear-conner/'
    html2 = urllib.request.urlopen(url).read()
    html2 = str(html2)
    soup = BeautifulSoup(html2, 'lxml')
    with open(str(n) + '.txt', 'w') as f:
        for i in soup.find_all('div', class_='mb3 mb10-sm mb3 js-risks'):
            for a in i.find_all('p'):
                g= a.get_text()
                f.write(g)

#url = 'https://www.kickstarter.com/projects/337373206/my-first-solo-album-the-long-awaited-dear-conner/'





file = open('tech_change.txt')
n= 1
for line in file.readlines():
    line=line.strip('\n')
    print(n)
    try:
       risk(line,n)
       n = n+1
    except:
        print('error in link',line)
        n = n+1
