from bs4 import BeautifulSoup
# 使用bs4通过id抓取百度新闻
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
s1 = soup.select('#source')
print(s1)

