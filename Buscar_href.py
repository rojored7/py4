# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = ('http://py4e-data.dr-chuck.net/comments_1591872.html')#input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags

rows = soup.find('table',attrs={"border":"2"}).find_all('tr')
text=[]
num = 0
for row in rows:
    cell=row.find_all('td')[1]
    text.append(cell.get_text().strip())
for tx in text[1:]:
    num = num + int(tx)
print(num)    

