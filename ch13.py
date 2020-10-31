# data on the web
# xml
# json

# eXtensible markup language(XML)

# <people>
#   <person>
#       <name> tharun </name>
#       <phone> 231823 </phone>
#   </person>
#   <person>
#       <name> nayak </name>
#       <phone type = "intl"> 234342 </phone>
#       <email />
#   </person>
# </people>

# xml schema
import xml.etree.ElementTree as ET

data = '''<stuff>
<people>
    <person>
    <name> chuck </name>
    <phone type = "intl"> 32132 </phone>
    <email hide = "yes"/>
    </person>
    <person>
    <name> bob </name>
    <phone type = "intl"> 1237623 </phone>
    <email hide = "yes"/>
    </person>
</people>
</stuff>'''
# tree = ET.fromstring(data)

# print('Name:', tree.find('name').text)
# print('Attr:', tree.find('email').get('hide'))

stuff = ET.fromstring ( data )
lst = stuff.findall ( 'people/person' )
print ( 'person count:', len ( lst ) )
for i in lst:
    print ( i.find ( 'name' ).text )
    print ( i.find ( 'phone' ).text )

# json
import json

data = '''{
    "name" : " tharun",
    "phone" :{
        "type" : "intl",
        "number" : "23891238"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads ( data )  # info is a dictionary
print ( info["name"] )
print ( info["email"]["hide"] )

yo = '''[
    {
        "id" : "01",
        "x" : "7",
        "name" : "tharun"
    },
    {
        "id" : "07",
        "x" : "4",
        "name" : "nayak"
    }
]'''
info = json.loads ( yo ) # info is a list here
print ( len ( yo ) )
for i in info:
    print ( i["name"] )
    print ( i["id"] )
    print ( i["x"] )

# application program interface
