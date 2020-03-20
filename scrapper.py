import requests
from bs4 import BeautifulSoup

quote_page=requests.get('https://www.brainyquote.com/quote_of_the_day')
html = quote_page.text

soup=BeautifulSoup(html,'html.parser')

#print(soup)

name_box = soup.find('a', attrs={'class': 'b-qt qt_118824 oncl_q'})
name = name_box.text.strip() # strip() is used to remove starting and trailing

print(name)


