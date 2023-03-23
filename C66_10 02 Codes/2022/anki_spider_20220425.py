import requests
from bs4 import BeautifulSoup
import re
"""
url="https://www.baidu.com/s"
keyword = 'python'
try:
    kv = {'wd':keyword}
    r = requests.get(url,params=kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print('失败')
"""

str1 = '''
<div class="result1">
    <h1 class="title">华能信托是家好公司</h1>
<div1>
<div class="result2">
    <h1 class="title">华能信托是家好公司</h1>
</div>
'''
soup1 = BeautifulSoup(str1, 'html.parser')
soup1.select('.title')
for i in soup1:
    print(i.text)

str2 = '''文本A
百度新闻文本B'''
# 如何正则匹配百度新闻并打印出来？
r = re.findall('文本A(.*?)文本B', str2, re.S)
print(r)
