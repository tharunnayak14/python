import xml.etree.ElementTree as ET
import urllib
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl
import json
sample_data = "http://python-data.dr-chuck.net/comments_42.xml"
actual_data = "http://py4e-data.dr-chuck.net/comments_526003.xml"

data_url = actual_data
data = urllib.request.urlopen ( actual_data ).read ()

commentinfo = ET.fromstring(data)
lst = commentinfo.findall('comments/comment')
print('User count:', len(lst))
sum = 0
for item in lst:
    sum += int(item.find('count').text)
print(sum)