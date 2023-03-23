import requests
from bs4 import BeautifulSoup


url = r'http://python123.io/ws/demo.html'
r = requests.get(url)
s = BeautifulSoup(r.text)
print(s.prettify())


# get方式获取百度首页数据，提取其中的状态码、响应正文、编码方式、从内容中分析出的响应内容编码方式和http响应内容的二进制
print(r.status_code)
print(r.text)
print(r.encoding)
print(r.apparent_encoding)
print(r.content)
