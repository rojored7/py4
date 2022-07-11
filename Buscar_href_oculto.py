from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
#('http://py4e-data.dr-chuck.net/known_by_Ambreen.html')
Link=input('Enter - ')
Nombre=input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
letras=list()
tags = soup('a')

for tag in tags:
    tag.contents[0]
    letras.append(tag.get('href', None))
    #print('URL:', tag.get('href', None))
    
print(letras[int(Link)])

for i in range(int(Nombre)):
    
    urlaux = (letras[int(Link)])
    letras.clear()
    html1 = urlopen(urlaux, context=ctx).read()
    soup1 = BeautifulSoup(html1, "html.parser")    
    tags = soup1('a')
    for tag in tags:
        tag.contents[0]
        letras.append(tag.get('href', None))
    #print('URL:', tag.get('href', None))
    print(letras[int(Link)])
      
