import requests
from bs4 import BeautifulSoup

r = requests.get(r'http://python123.io/ws/demo.html')
soup = BeautifulSoup(r,'html.parser')
print(soup.prettify())



