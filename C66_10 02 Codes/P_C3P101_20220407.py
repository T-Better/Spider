from bs4 import BeautifulSoup
res = '''
<div class="result1">
    <h1 class="title">华能信托是家好公司</h1>
<div1>
<div class="result2">
    <h1 class="title">华能信托是家好公司</h1>
</div>
'''

soup = BeautifulSoup(res, 'html.parser')
title3 = soup.select('.result1 h1')  # 多层次筛选 不仅是父子层搜寻
for i in title3:
    print(i.text)









