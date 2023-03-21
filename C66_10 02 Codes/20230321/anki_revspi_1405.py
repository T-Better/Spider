import requests
from bs4 import BeautifulSoup


res = '''
<html lang="en">
    <body>
        <h1 class="title">华能信托是家好公司</h1>
        <h1 class="title">上海交大是所好学校</h1>
        <a href="https://www.baidu.com/" id="source">百度新闻</a>
    </body>
</html>
'''

soup1 = BeautifulSoup(res,'html.parser')

# 通过id抓取百度新闻
s1 = soup1.select('#source')
print(s1)

for i in s1:
    print(i['href'])













