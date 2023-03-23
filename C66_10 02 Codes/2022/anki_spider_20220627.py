import requests

# 如何只获取百度首页的请求头
r = requests.head('https://www.baidu.com')
print(r.headers)







