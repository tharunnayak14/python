# network technology
# http
# hyper text transfer protocol
# url-uniform resource locator
import socket

mysock = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
mysock.connect ( ('data.pr4e.org', 80) )
cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n".encode ()
mysock.send ( cmd )

while True:
    data = mysock.recv ( 512 )
    if len ( data ) < 1:
        break
    print ( data.decode () )

mysock.close ()

print ( ord ( 'i' ) )

# using urllib in python
import urllib.request, urllib.error

fhand = urllib.request.urlopen ( 'http://data.pr4e.org/romeo.txt' )
counts = dict ()
for line in fhand:
    words = line.decode ().strip ()
    for word in words:
        counts[word] = counts.get ( word, 0 ) + 1
print ( counts )

# import urllib.request, urllib.error
# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
from bs4 import BeautifulSoup

url = input ( 'Enter - ' )
html = urllib.request.urlopen ( url ).read ()
soup = BeautifulSoup ( html, 'html.parser' )

# retrieve all of anchor tags,  all links in the website
tags = soup ( 'a' )
for tag in tags:
    print ( tag.get ( 'href', None ) )
