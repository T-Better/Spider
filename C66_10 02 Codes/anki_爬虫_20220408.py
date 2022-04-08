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
# r1 = soup1.select('div .title')
#
# for i in r1:
#     print(i.text)
res2 = '''
<html lang="en">
    <body>
        <h1 class="title">华能信托是家好公司</h1>
        <h1 class="title">上海交大是所好学校</h1>
        <a href="https://www.baidu.com/" id="source">百度新闻</a>
    </body>
</html>
'''
soup2 = BeautifulSoup(res2, 'html.parser')
r2 = soup2.select('#source')
print(r2)
for i in r2:
    print(i['href'])

# import re
#
# title = '<!--s-text--->双十一点燃线下经济  "小时达" 服务成<em>阿里巴巴</em>增长新引擎<!--/s-text-->'
# r3 = re.sub('<.*?>','', title)
# print(r3)

# 如何对爬取以上url的爬虫设置超时时间5s？
# import requests
#
# url='https://www.baidu.com'
# r5 = requests.get(url, timeout=5)






