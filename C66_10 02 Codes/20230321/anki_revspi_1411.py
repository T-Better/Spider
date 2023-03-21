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

s2 = BeautifulSoup(res,'html.parser')
t = s2.select('h1')
for i in t:
    print(i)
    print(i.text)

url='https://www.baidu.com'
r = requests.get(url,timeout=5)



