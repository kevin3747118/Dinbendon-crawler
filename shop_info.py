#-*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import pymssql
import re

# cnxn = pymssql.connect(server='', user='',
#                        password='',  database='')
# cursor = cnxn.cursor()


# search = input("Enter the restaurant URL you want to search: " )
#post = requests.get('https://dinbendon.net/do/idine')

#url = str('d')
url = 'https://dinbendon.net/do/idine?shop=209534'

# print(url)
# print(str(re.findall('shop=.+' , url)).replace('shop=' , ''))
shop_id = int(str(re.findall('shop=.+' , url)).replace('shop=' , '').replace('[\'' , '').replace('\']' , ''))
# print(shop_id)
# print(url)


# product_name
def product_name_price(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    # print(url)
    # print(soup)
    # #### even
    # a = 0
    # # print(soup)
    # for i in soup.find_all('tr', {'class': 'even'}):
    #      c = i.text.split('\n')
    #      a += 1
    #      print(c)
    #      if a == 1:
    #         cursor.execute("""INSERT INTO  [dbo].[DIN_BEN_DON_PRODUCT] (Shop_ID , Product_Name , Product_Price) VALUES (%s , %s , %s) """,
    #                 (shop_id, c[2], c[5]))
    #         cnxn.commit()
    #         a = 0
    #         del c
    # print('ok')

    ### odd
    a = 0
    p_name_lst = list()
    for p_name in soup.find_all('td' , {'style' : 'width: 10em;'}):
        correct_pname = p_name.text.replace('♨', '').replace('⌂', '').replace('\n', '')
        p_name_lst.append(correct_pname)

    p_price_lst = list()
    for p_price in soup.find_all('td' , {'style' : 'width: 20em;'}):
        correct_pprice = p_price.text.replace('\n', '')
        p_price_lst.append(correct_pprice)

    """
    -*- list comprehension -*- 
    目地 : (餐點, 價格)
    
    step1 : 沒意外的話，p_name_lst跟p_price_lst的長度會一至
    step2 : for loop任意一個list的長度
    step3 : 用index的方式取參點跟價格list裡面的值，做成 [(x1, y1), (x2, y2), ... , (xn, yn)]；
            1、2及n為step 2 for loop的index
    """
    p_name_price = [(shop_id, p_name_lst[i], p_price_lst[i]) for i in range(len(p_price_lst))]

    cursor.executemany(sql_command, p_name_price)
    cnxn.commit()
    
    # print(p_name_price)

        # c = j.text.split('\n')
        # if '網友評價' not in c:
        #     if '地址' not in c :
        #         if '傳真' not in c:
        #             if '店家詳細說明' not in c:
        #                 if '店家服務類型' not in c:
        #                     if '最後修改日' not in c:
        #                         a += 1
        #                         if a == 1:
        #                             cursor.execute("""INSERT INTO  [dbo].[DIN_BEN_DON_PRODUCT] (Shop_ID , Product_Name , Product_Price) VALUES (%s , %s , %s) """,(shop_id, c[2], c[5]))
        #                             cursor.execute("""DELETE FROM [dbo].[DIN_BEN_DON_PRODUCT] WHERE Product_Name = ''""")
        #                             cnxn.commit()
        #                             a = 0
        #                             del c
    # print('ok')

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
# def shop_info(url):
#     r = requests.get(url)
#     soup = BeautifulSoup(r.text, 'lxml')
#     shop_content = soup.find_all('td' , {'class' : 'content'})
#     columns = []
#
#     for i in shop_content:
#         columns.append(((i.text).replace('\n' , '')).replace('\t' , ''))
#
#     info = []
#     chose = (0 ,2, 3, 4, 6, 7)
#     for j in chose:
#         info.append(columns[j])
#         print(info)
#     cursor.execute("""INSERT INTO  [dbo].[DIN_BEN_DON] (Shop_ID , Shop_Name , Shop_Content , Shop_Address , Shop_TEL , Shop_City , Shop_Type) VALUES (%s , %s , %s , %s , %s , %s , %s )""",(shop_id, info[0], info[1], info[2], info[3], info[4], info[5]))
#     cnxn.commit()
#     #print(info[3])
#     print("ok")


if __name__ == '__main__':
    # search = input("Enter the restaurant URL you want to search: ")
    # search = url
    product_name_price(url)
    # shop_info(url)