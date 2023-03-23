from bs4 import BeautifulSoup
import requests

res = '''
<html lang="en">
    <body>
        <h1 class="title">华能信托是家好公司</h1>
        <h1 class="title">上海交大是所好学校</h1>
        <a href="https://www.baidu.com/" id="source">百度新闻</a>
    </body>
</html>
'''
soup1 = BeautifulSoup(res, 'html.parser')
r1 = soup1.select('#source')
print(r1)
for i in r1:
    print(i['href'])

res2 = '''
<div class="result1">
    <h1 class="title">华能信托是家好公司</h1>
<div1>
<div class="result2">
    <h1 class="title">华能信托是家好公司</h1>
</div>
'''
"""
soup2 = BeautifulSoup(res2, 'html.parser')
r2 = soup2.select('div .title')
for i in r2:
    print(i.text)
"""
url='https://www.baidu.com'
r3 = requests.get(url,timeout=5)

