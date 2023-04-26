from bs4 import BeautifulSoup as befu
res = '''
<div class="result1">
    <h1 class="title">华能信托是家好公司</h1>
<div1>
<div class="result2">
    <h1 class="title">华能信托是家好公司</h1>
</div>
'''
s1 = befu(res,'html.parser')
r1 = s1.select('h1')
for i in r1:
    print(i.text)













