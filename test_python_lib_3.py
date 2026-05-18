import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(requests.get('https://quotes.toscrape.com/').text,'lxml')

for i in soup.find_all('div',{'class':'quote'}):
    print(i.text)