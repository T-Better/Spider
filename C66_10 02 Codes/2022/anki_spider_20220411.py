import re
from bs4 import BeautifulSoup
import requests

# title = '<!--s-text--->双十一点燃线下经济  "小时达" 服务成<em>阿里巴巴</em>增长新引擎<!--/s-text-->'
# title1 = re.sub('<.*?>','',title)
# print(title1)

res = '''
<div class="result1">
    <h1 class="title">华能信托是家好公司</h1>
<div1>
<div class="result2">
    <h1 class="title">华能信托是家好公司</h1>
</div>
'''
soup = BeautifulSoup(res, 'html.parser')
title3 = soup.select('.result1 h1')
for i in title3:
    print(i.text)

url='https://www.baidu.com'
r = requests.get(url,timeout=5)

res2 = '''
<html lang="en">
    <body>
        <h1 class="title">华能信托是家好公司</h1>
        <h1 class="title">上海交大是所好学校</h1>
        <a href="https://www.baidu.com/" id="source">百度新闻</a>
    </body>
</html>
'''
soup2 = BeautifulSoup(res2,'html.parser')
e1 = soup2.select('body #source')
for i in e1:
    print(i['href'])

res3 = '''文本A
百度新闻文本B'''
pattern='文本A(.*?)文本B'
r3 = re.findall(pattern,res3,re.S)
print(r3)

company = '*华能信托'
r4 = re.sub('[*]','',company)
print(r4)
