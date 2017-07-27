#!/usr/bin/python3

from bs4 import BeautifulSoup

import urllib.request

def headline_news():
 url = input("Enter the url:").lower()
 url = url.replace("http://",'')
 url = "http://"+url 

 a = 0
 try:
  page = urllib.request.urlopen(url)
  soup = BeautifulSoup(page, 'lxml')
   
#this is for setopati.com
  if "Setopati" in (soup.find("title").text):
          for i in soup.find_all('h2',class_="entry-title"):
             a = a+1
             
             z = i.find('a').text
             print("-",z,"\n")
		


#this is for ekantipur.com
  if "ekantipur" in (soup.find("title").text):
	  for i in soup.find_all("div",class_="display-news-title"):
           a = a+1   
           z = i.find('a').text
           print("-",z,"\n")


#this is for ratopati.com
  if "Ratopati" in (soup.find("title").text):
	  for i in soup.find_all('div', class_ ="item-content"):
            a=a+1
            z = i.find('a').text
            print("-",z,"\n")



#this is for light nepal.news
  if "Light Nepal" in (soup.find("title").text):
          for i in soup.find_all('div',class_="main-list small-list clearfix"):
           a=a+1
           z = i.find('a').text
           print("-",z,"\n")
  if a == 0:
     print("Not the desired site")

 except Exception as e:
  print(e)

headline_news()

