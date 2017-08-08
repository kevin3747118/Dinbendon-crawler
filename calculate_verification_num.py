import requests
import json
from bs4 import BeautifulSoup
import re

dinbendon_url = 'https://dinbendon.net/do/login'
dinbendon_res = requests.get(dinbendon_url)

def count_verification_num():
    soup = BeautifulSoup(dinbendon_res.text , 'lxml')

    verif_code = str(soup.find_all('td' , {'class' : 'alignRight'}))

    verif_num = str(str(str(re.findall('em;\">.+</td' , verif_code)).split('em;\">')).split('</td'))
    num_a = int(verif_num[11:13])
    b = verif_num[14:16]

    for i in b:
        if i != "=":
            num_b = int(i)

    verif = num_a + num_b
    return verif

print(count_verification_num())



def get_shop_list():
    headers = {'Content-Type': 'application/json'}
    payload = {
        'username' : '',
        'password' : '7',
        'result' : count_verification_num(),
        'submit' : '%E7%'
    }
    r = requests.get('https://dinbendon.net/do/login' , )
    return r.text

print(get_shop_list())