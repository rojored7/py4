import json
import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = ('http://py4e-data.dr-chuck.net/comments_1591875.json')#input('Enter - ')
html = urlopen(url, context=ctx)
data = html.read()
#print(data.decode())
aux=list()
info = json.loads(data)
#print(info)
for item in info.values():
    aux.append(item)
suma=0
for val in aux[1]:
    num=list(val.values())
    suma = suma + int(num[1])  
print(suma)
    
