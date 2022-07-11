import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')#('http://py4e-data.dr-chuck.net/comments_42.xml')#

html = urlopen(url, context=ctx)
data = html.read()
coment=list()
tree = ET.fromstring(data)
print(data.decode())
print(tree)
suma=0
result=tree.findall(('.//comment'))
for item in result:
    
    coment.append(item.findtext('.//count'))
    suma=suma+int(item.findtext('.//count'))
print(result)
print(suma)

