#!/usr/bin/python3

import socket
from urllib.request import urlopen, URLError, HTTPError

socket.setdefaulttimeout(20)

url = []
for i in range(3):
 url.append(input("Enter the address of the website : ").lower())

for i in range(3):
 url[i] = url[i].replace("http://",'')
 url[i] = "http://" + url[i]

 try:
    response = urlopen(url[i])

 except HTTPError as e:
    if e.code == 400:
        print ('HTTP error type =  Bad Request')
    if e.code == 401:
        print('HTTP error type = Unauthorized')
    if e.code == 403:
        print('HTTP error type = Forbidden')
    if e.code == 404:
        print('HTTP error type = Not Found')
    if e.code == 500:
        print('HTTP error type = Internal Server Error')
    if e.code == 502:
        print('HTTP error type = Bad Gateway')
    if e.code == 503:
        print('HTTP erro type = Service Unavailable')
    if e.code == 504:
        print('HTTP error type = Gateway Timeout')
 except URLError:
    print ('We failed to reach a server because the URL entered is incorrect, Please check the URL and enter again.')

 else:
    html = response.read()
    print ('Website is working perfectly!')
 
