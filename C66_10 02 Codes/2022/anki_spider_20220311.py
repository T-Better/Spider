# 爬虫：如何只获取百度首页的请求头
import requests

url = "http://www.baidu.com"
r = requests.head(url)
print(r.headers)
