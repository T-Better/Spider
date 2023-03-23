import requests
import re
from bs4 import BeautifulSoup

"""
url="https://www.baidu.com/s"
keyword = "python"
kv = {'wd':keyword}
r = requests.get(url,params=kv)
print(r.text)
"""

res = '''文本A
百度新闻文本B'''

# r2 = re.findall('文本A(.*?)文本B',res,re.S)
# print(r2)

tmp1 = '''
<html lang="en">
    <body>
        <h1 class="title">华能信托是家好公司</h1>
        <h1 class="title">上海交大是所好学校</h1>
        <a href="https://www.baidu.com/" id="source">百度新闻</a>
    </body>
</html>
'''
# soup = BeautifulSoup(tmp1,'html.parse')
# s1 = soup.select('#source')
# print(s1)
# for i in s1:
#     print(i['href'])

soup1 = BeautifulSoup(tmp1,'html.parser')
s2 = soup1.select('.title')
for i in s2:
    print(i.text)
