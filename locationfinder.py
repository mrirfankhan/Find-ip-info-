from bs4 import BeautifulSoup
import requests
import json

url=requests.get("https://www.showmyip.com/")
find1=BeautifulSoup(url.content,'html.parser')
ip=find1.find("h2",attrs={'id':'ipv4'}).text
info=requests.get(f"https://ipapi.co/{ip}/json/").json()
for i,j in info.items():
	print(f"{i} : {j}")
