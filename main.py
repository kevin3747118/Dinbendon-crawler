import requests
import json
from bs4 import BeautifulSoup
import re

def count_verification_num():
    dinbendon_res = requests.get('https://dinbendon.net/do/login')
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
