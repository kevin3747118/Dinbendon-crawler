#-*- coding: big5 -*-

import requests
from bs4 import BeautifulSoup
import pymssql
import re

cnxn = pymssql.connect(server='', user='',
                       password='',  database='')
cursor = cnxn.cursor()


# search = input("Enter the restaurant URL you want to search: " )
#post = requests.get('https://dinbendon.net/do/idine')

#url = str('d')
# url = 'https://dinbendon.net/do/idine?shop=277494'
# print(str(re.findall('shop=.+' , url)).replace('shop=' , ''))
# shop_id = int(str(re.findall('shop=.+' , url)).replace('shop=' , '').replace('[\'' , '').replace('\']' , ''))
# print(shop_id)
# print(url)


# product_name
def product_name_price(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    print(url)
    print(soup)
    #### even
    a = 0
    # print(soup)
    for i in soup.find_all('tr', {'class': 'even'}):
         c = i.text.split('\n')
         a += 1
         print(c)
         if a == 1:
            cursor.execute("""INSERT INTO  [dbo].[DIN_BEN_DON_PRODUCT] (Shop_ID , Product_Name , Product_Price) VALUES (%s , %s , %s) """,
                    (shop_id, c[2], c[5]))
            cnxn.commit()
            a = 0
            del c
    print('ok')

    ### odd
    a = 0

    for j in soup.find_all('tr' , {'class' : 'odd'}):
        c = j.text.split('\n')
        if '網友評價' not in c:
            if '地址' not in c :
                if '傳真' not in c:
                    if '店家詳細說明' not in c:
                        if '店家服務類型' not in c:
                            if '最後修改日' not in c:
                                a += 1
                                if a == 1:
                                    cursor.execute("""INSERT INTO  [dbo].[DIN_BEN_DON_PRODUCT] (Shop_ID , Product_Name , Product_Price) VALUES (%s , %s , %s) """,(shop_id, c[2], c[5]))
                                    cursor.execute("""DELETE FROM [dbo].[DIN_BEN_DON_PRODUCT] WHERE Product_Name = ''""")
                                    cnxn.commit()
                                    a = 0
                                    del c
    print('ok')

# product_name_price()
        #cursor.execute("""INSERT INTO  [dbo].[DIN_BEN_DON_PRODUCT] (Product_Name) VALUES (i.text)""")
         # print (i.text)
# product_price
#def product_price():
    # for j in soup.find_all('span' , {'style' : 'white-space: nowrap;'}):
        # cursor.execute("""INSERT INTO  [dbo].[DIN_BEN_DON_PRODUCT] (Shop_ID , Product_Price) VALUES (%s , %s) """ , (shop_id , j.text))
        # cnxn.commit()
        # print(j.text)

# shop_info
def shop_info(url):
    shop_content = soup.find_all('td' , {'class' : 'content'})
    columns = []

    for i in shop_content:
        columns.append(((i.text).replace('\n' , '')).replace('\t' , ''))

    info = []
    chose = (0 ,2, 3, 4, 6, 7)
    for j in chose:
        info.append(columns[j])
    cursor.execute("""INSERT INTO  [dbo].[DIN_BEN_DON] (Shop_ID , Shop_Name , Shop_Content , Shop_Address , Shop_TEL , Shop_City , Shop_Type) VALUES (%s , %s , %s , %s , %s , %s , %s )""",(shop_id, info[0], info[1], info[2], info[3], info[4], info[5]))
    cnxn.commit()
    #print(info[3])
    print("ok")


if __name__ == '__main__':
    search = input("Enter the restaurant URL you want to search: ")
    # search = url
    product_name_price(search)
    shop_info(search)
