import xml.etree.ElementTree as ET
import urllib
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl
import json
Sample_data =  "http://py4e-data.dr-chuck.net/comments_42.json"
Actual_data = "http://py4e-data.dr-chuck.net/comments_526004.json"

data_url = Actual_data
data = urllib.request.urlopen ( data_url ).read ()

commentinfo = json.loads(data)
sum = 0
for item in commentinfo['comments']:
    sum += int(item['count'])
print(sum)
