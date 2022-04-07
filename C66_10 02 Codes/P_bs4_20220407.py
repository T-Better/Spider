res = '''
<html lang="en">
    <body>
        <h1 class="title">华能信托是家好公司</h1>
        <h1 class="title">上海交大是所好学校</h1>
        <a href="https://www.baidu.com/" id="source">百度新闻</a>
    </body>
</html>
'''
from bs4 import BeautifulSoup

soup = BeautifulSoup(res, 'html.parser')
"""
title = soup.select('h1')
for i in title:
    print(i.text)
"""
"""
# 通过class属性
title2 = soup.select('.title')
for i in title2:
    print(i.text)
"""

# 通过id抓取百度新闻
source1 =soup.select('#source')
print(source1)

for i in source1:
    print(i['href'])

