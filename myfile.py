
#!/usr/bin/python3


from bs4 import BeautifulSoup


import urllib.request

url=input("Enter the url: ")


page = urllib.request.urlopen(url)
web = BeautifulSoup(page, 'lxml')
m=0
def headlineNews():
	z=i.find('a').text
	print(m,'. ', z )
	

#this is for setopati.com
for i in web.find_all('h2',class_="entry-title"):
	m=m+1
	if m>11:
		break
	headlineNews()

#this is for ekantipur.com
for i in web.find_all('div', class_="display-news-title"):
	m=m+1
	if m>11:
		break
	headlineNews()

#this is for ratopati.com

for i in web.find_all('div', class_ ="item-content"):
	m=m+1
	if m>11:
		break
	headlineNews()

#this is for light nepal.news
for i in web.find_all('div',class_="main-list small-list clearfix"):
	m=m+1
	if m>11:
		break
	headlineNews()

