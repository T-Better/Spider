from bs4 import BeautifulSoup
import re

res = '''
<div class="result1">
    <h1 class="title">华能信托是家好公司</h1>
<div1>
<div class="result2">
    <h1 class="title">华能信托是家好公司</h1>
</div>
'''

# s1 = BeautifulSoup(res,'html.parser')
# t1 = s1.select('.result1 h1')
# for i in t1:
#     print(i.text)

title = '<!--s-text--->双十一点燃线下经济  "小时达" 服务成<em>阿里巴巴</em>增长新引擎<!--/s-text-->'
rt = re.sub('<.*?>','',title)
print(rt)
