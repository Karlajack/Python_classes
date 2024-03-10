import requests

url=("https://rickandmortyapi.com/api")

response=requests.get(url)
 
print(response.status_code)

#results=(response.json())

#print(results)
#data=(response.json)

#print(data)

#for characters in results[:20]:
   # print(characters)
   






