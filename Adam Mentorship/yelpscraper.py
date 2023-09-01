# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import lxml
import requests
import time
import sys


headers = {'User-Agent':'Google/7.0 (Windows; Intel Windows OS 10_11_2) Version/9.0.2'}

comment_list = list()

URL = "https://www.yelp.com/biz/the-spot-rockville-2"

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'lxml')

comments = soup.body.find('yelp-react-root')#.select('ul[class*="undefined list"]')


with open("yelpfile.xml", "w", encoding="utf-8") as f:

    f.write(soup.prettify())




#comments = soup.body.find('yelp-react-root').find_all('ul[class*="undefined list"]')
'''
for comm in comments:
    print(comm.get_text())


'''









'''


headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
url='https://www.yelp.com/biz/the-spot-rockville-2'

response=requests.get(url,headers=headers)



#print(response)

soup=BeautifulSoup(response.content,'lxml')


soup.body.contents

for item in soup.find_all('p'):
    reviewsList = item.select
    if item == "test":
    print(item)
    
   
if item.find('span'):
    print(item.prettify)

    thing = soup.select('[class*=span]')
    print(thing)
#print(item)
'''


