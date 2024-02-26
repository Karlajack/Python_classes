
import requests

response=requests.get("https://Zinduaschool.come")

print (response.status.code)

print(response.content)