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

# 使用beautifulsoup爬取里面的网站
s1 = BeautifulSoup(res, 'html.parser')
r1 = s1.select('#source')
print(r1)
for i in r1:
    print(i['href'])
    print(i.text)










