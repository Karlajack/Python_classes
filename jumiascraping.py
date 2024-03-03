import requests
from bs4 import BeautifulSoup

url="https://www.jumia.co.ke/flash-sales"

response=requests.get(url)

soup=BeautifulSoup(response.content,'html.parser')

print(soup)

items=soup.find_all('div',class_='-fs20 -pts -pbxs')

print(items)

for item in items:
    print (item.text)
