import requests

# 只爬取百度首页的报文头数据
rh = requests.head('http://www.baidu.com')
print(rh.headers)