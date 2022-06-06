import requests
from bs4 import BeautifulSoup

url = 'http://animixplay.to'
classname= "iframecontainer"


headers = {
    'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1',
    'Accept-language': 'en-US',
    'Referer': 'http://google.com',
    'DNT': '1'
}
r = requests.get(url, headers=headers)
# print(r.text)
data = r.text
soup = BeautifulSoup(data, 'html.parser')
html = soup.prettify()
# print(soup.find(class_=f'{classname}'))