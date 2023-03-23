from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import re


# driver = webdriver.Chrome()
# driver.get('www.baidu.com')

# selenium获取数据的函数是什么？怎么用？类似于requests.get()
# data = driver.page_source

res = '''
<html lang="en">
    <body>
        <h1 class="title">华能信托是家好公司</h1>
        <h1 class="title">上海交大是所好学校</h1>
        <a href="https://www.baidu.com/" id="source">百度新闻</a>
    </body>
</html>
'''

soup = BeautifulSoup(res,'html.parser')

# 使用bs4通过id抓取百度新闻
a = soup.select('#source')
print(a)

# 爬标题文字
"""
title2 = soup.select('.title')
for i in title2:
    print(i.text)
"""

# 网站地址
"""
source1 = soup.select('#source')
print(source1)
for i in source1:
    print(i['href'])
"""

# 爬标题文字,使用bs4
"""
title = soup.select('h1')
for i in title:
    print(i.text)
"""

# 如何对爬取以下url的爬虫设置超时时间5s？
"""
url='https://www.baidu.com'
r = requests.get(url,timeout=5)
"""

title4 = '<!--s-text--->双十一点燃线下经济  "小时达" 服务成<em>阿里巴巴</em>增长新引擎<!--/s-text-->'
title5 = re.sub('<.*?>','',title4)
print(title5)

# 匹配
company = '*华能信托'
c1 = re.sub('[*]','',company)
print(c1)

res = '''文本A
百度新闻文本B'''

r2 = re.findall('文本A(.*?)文本B',res,re.S)
