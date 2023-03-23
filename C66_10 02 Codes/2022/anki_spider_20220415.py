import re
from bs4 import BeautifulSoup

res = '''
    <div class="result1">
        <h1 class="title">华能信托是家好公司</h1>
    <div1>
    <div class="result2">
        <h1 class="title">华能信托是家好公司</h1>
    </div>
    '''
# soup1 = BeautifulSoup(res, 'html.parser')
# res1 = soup1.select('div .title')
# for i in res1:
#     print(i.text)

str2 = '''
<html lang="en">
    <body>
        <h1 class="title">华能信托是家好公司</h1>
        <h1 class="title">上海交大是所好学校</h1>
        <a href="https://www.baidu.com/" id="source">百度新闻</a>
    </body>
</html>
'''
soup2 = BeautifulSoup(str2,'html.parser')
res2 = soup2.select('#source')
for i in res2:
    print(i['href'])
