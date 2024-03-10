import requests
from bs4 import BeautifulSoup
import csv

# requesting information from web

url = 'https://www.nytimes.com/'
response = requests.get(url)
#print(response.status_code)
#print(response.content)

# converting the response content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# find the articles in the web
articles = soup.find_all('div',class_='css-xdandi') 

data = []



# iterating through articles to get title

for article in articles[:10]:
    title = article.find('p',class_='indicate-hover').text.strip()
    #description = article.find('p',class_='summary-class').text.strip()
    #print(title)
           
  # creating title dictionaries
    #data.append({'title': title})
    data.append({'title': title})#, 'description':}# description})
    print(data)

with open('nytimes.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['title']) #, 'description'])
    writer.writeheader()
    writer.writerows(data)
"""  
# saving the articles dictinaries in CSV file
with open("nytimes.csv",'w',newline='') as file:
    writer=csv.DictWriter(file,fieldnames=['title'])
    writer.writerows(data)
    """
    

    