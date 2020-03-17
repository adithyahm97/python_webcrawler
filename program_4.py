import requests
from bs4 import BeautifulSoup
res=requests.get('https://stackoverflow.com/questions')
res.text
soup=bs4.BeautifylSoup(res.text,'lxml')
#for link in soup.find_all('a',href=True):
    #print(link['href'])

for div in soup.findAll('div', attrs={'class':'user-details'}):
    print(div.find('a')['href'])
    print(div.find('a').contents[0])






