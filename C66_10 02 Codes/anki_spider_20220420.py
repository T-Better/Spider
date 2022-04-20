import re
from bs4 import BeautifulSoup
import requests
from selenium import webdriver

# company = '*华能信托'
# r1 = re.sub('[*]','',company)
# print(r1)

res1 = '''
<html lang="en">
    <body>
        <h1 class="title">华能信托是家好公司</h1>
        <h1 class="title">上海交大是所好学校</h1>
        <a href="https://www.baidu.com/" id="source">百度新闻</a>
    </body>
</html>
'''
soup1 = BeautifulSoup(res1,'html.parser')
r1 = soup1.select('#source')
for i in r1:
    print(i.text)
"""
# 如何对爬取以上url的爬虫设置超时时间5s？
url='https://www.baidu.com'
r2 = requests.get(url,timeout=5)

# selenium获取数据的函数是什么？怎么用？类似于requests.get()
browser = webdriver.Chrome()
url_finance = r'https://www.baidu.com'
browser.get(url_finance)
data = browser.page_source
"""
str3 = '''
<html lang="en">
    <body>
        <h1 class="title">华能信托是家好公司</h1>
        <h1 class="title">上海交大是所好学校</h1>
        <a href="https://www.baidu.com/" id="source">百度新闻</a>
    </body>
</html>
'''
r3 = BeautifulSoup(str3,'html.parser')
res3 = r3.select('#source')
for i in res3:
    print(i['href'])


