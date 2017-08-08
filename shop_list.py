import requests
from bs4 import BeautifulSoup

r = requests.get('https://dinbendon.net/do/idine?wicket:pageMapName=wicket-0&map=true&shop=276839')
soup = BeautifulSoup(r.text , 'lxml')

# product_name
def product_name():
    for i in soup.find_all('td', {'style': 'width: 10em;'}):
        print (i.text)

# product_price
def product_price():
    for j in soup.find_all('span' , {'style' : 'white-space: nowrap;'}):
        print(j.text)

# shop_info
shop_info = soup.find_all('td' , {'class' : 'content'})
for k in shop_info:
    print((k.text).strip('\n'))

