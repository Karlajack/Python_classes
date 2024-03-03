
import requests
from bs4 import BeautifulSoup
import csv

#response=requests.get("https://zinduaschool.com")
#response=requests.get("https://hojaleaks.com")

#url="https://hojaleaks.com"

#response=requests.get(url)

#print(response.status_code)

#soup=BeautifulSoup(response.content,'html.parser')

#print(soup)

#paragraphs=soup.find_all('p')

#print(paragraphs)

#for paragraph in paragraphs:
    #print(paragraph.text)
#print(response.content)

# cd-to change folder
#py -m ensurepip --upgrade

# installing requests module
#py -m pip install requests
#py pip install requests



# scarp https:\\hojaleaks.com/python and get the titles/headings of the first three articles

url="https://hojaleaks.com/python"
response=requests.get(url)

soup=BeautifulSoup(response.content,'html.parser')

#print(soup)

titles=soup.find_all('h1')

#print(titles)

articles=0
for title in titles:
    if articles<3:
        print(title.text)
        articles+=1


# 

#with open("info.csv",'w') as file:
    #writer=csv.witer()
    #for paragraph in paragraphs:
       # writer()writelines


       #with open("info.csv",'w') as file:
    #writer=csv.witer()
    #for paragraph in paragraphs:
       # writer()writelines

