from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
my_url='https://stackoverflow.com/questions'

uClient=uReq(my_url)
page_html=uClient.read()
uClient.close()
page_soup=soup(page_html,"html.parser")

containers=page_soup.findAll("div",{"class":"question-hyperlink"})
print(containers)


