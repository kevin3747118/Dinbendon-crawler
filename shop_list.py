import requests
from bs4 import BeautifulSoup
import re

r = requests.get('https://dinbendon.net/do/idine?wicket:pageMapName=wicket-0&map=true&shop=276839')

soup = BeautifulSoup(r.text , 'lxml')

a = str(soup.find_all('div'))


#b = re.findall('<div>.+</div>' ,a)




print(a)