import requests
from bs4 import BeautifulSoup
import csv

url="https://www.jumia.co.ke/mlp-warehouse-clearance-sale"

response=requests.get(url)
#print(response.status_code)

soup=BeautifulSoup(response.content,'html.parser')

#print(soup)

items=soup.find_all('div',class_='-paxs row _no-g _4cl-3cm-shs') 

#print(items)
data = []



# iterating through articles to get item details
for item in items:
  articles = item.find_all('article', class_='prd _fb _p col c-prd')
  for article in articles:
    #article_class = item.find('article', class_='prd _fb _p col c-prd')
    item_name = article.find('h3', class_='name').text.strip()
    item_price = article.find('div', class_='prc').text.strip()
    items_left = article.find('div', class_='stk').text.strip()
    discounts=article.find_all('div',class_='s-prc-w')
    prod_ratings=article.find_all('div',class_='rev')
    for disc in discounts:
      item_disc = disc.find('div', class_='bdg _dsct _sm').text.strip()
    for rating in prod_ratings:
      item_rating = rating.find('div', class_='stars _s').text.strip()
      verified_ratings = rating.find('div', class_='in').text.strip()
      
    

      data.append({'item_name': item_name,'item_price': item_price, 'item_disc': item_disc, 'item_rating': item_rating,'items_left': items_left})
      print(data)

#  writing in csv file
with open('jumia.csv', 'w', newline='') as file:
  writer = csv.DictWriter(file, fieldnames=['item_name', 'item_price','item_disc','item_rating','items_left'])
  writer.writeheader()
  writer.writerows(data)

  