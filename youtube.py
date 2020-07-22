import requests, json, os, time, random, webbrowser

from bs4 import BeautifulSoup

from pprint import pprint


a=input("What do you want to search in -_- Youtube -_-\n Enter Here \n ")
a=a.split()
url="https://www.youtube.com/results?search_query="
print("toplist")
for i in range(len(a)):
	if i==(len(a)-1):
		url+=a[i]
	else:
		url+=a[i]+"+"
urldata=requests.get(url).text
soup=BeautifulSoup(urldata, "html.parser")
contents=soup.find_all("div", class_="yt-lockup-content")
link_data=[]
count=1
for i in contents:
	link=i.find("a")["href"]
	link=link.split("=")
	if link[0]=="/watch?v":
		data=i.find("a")["href"]
		title=i.find("a")["title"]
		print(count, title)
		count+=1
		link_data.append("https://www.youtube.com"+data)
inp=int(input("which one do you want to search"))
webbrowser.open(link_data[inp-1])

