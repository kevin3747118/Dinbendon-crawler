import requests
from bs4 import BeautifulSoup
import pymssql
import re

# r = requests.get('https://dinbendon.net/do/idine?wicket:pageMapName=wicket-0&map=true&shop=276839')
# soup = BeautifulSoup(r.text , 'lxml')
#
# shop_info = soup.find_all('td' , {'class' : 'content'})
#
# columns = []
# for i in shop_info:
#     columns.append(((i.text).replace('\n' , '')).replace('\t' , ''))
#
# info = []
# chose = (0 ,2, 3, 4, 6, 7)
# for j in chose:
#     info.append(columns[j])
# print(info)


#
# url = 'https://dinbendon.net/do/idine?shop=268010'
# print(str(re.findall('shop=.+' , url)).replace('shop=' , ''))
# shop_id = int(str(re.findall('shop=.+' , url)).replace('shop=' , '').replace('[\'' , '').replace('\']' , ''))
# print(shop_id)


res = requests.get('https://dinbendon.net/do/idine?shop=277494')
print(res.text)