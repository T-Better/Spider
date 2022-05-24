import requests
from bs4 import BeautifulSoup

"""
url1 = r'http://python123.io/ws/demo.html'
r = requests.get(url1)

soup = BeautifulSoup(r.text,'html.parser')
print(soup.prettify())
"""
"""
# 只爬取百度首页的报文头数据
r2 = requests.head('https://www.baidu.com')
print(r2.headers)
"""

# post如何带着请求头爬取http://www.baidu.com的数据，请求头为：user-agent:Chrome/10
h1 = {"user-agent":"Chrome/10"}
r3 = requests.post('http://www.baidu.com',headers = h1)
print(r3.text)
