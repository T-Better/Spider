from bs4 import BeautifulSoup



res = '''
<div class="result1">
    <h1 class="title">华能信托是家好公司</h1>
<div1>
<div class="result2">
    <h1 class="title">华能信托是家好公司</h1>
</div>
'''
s1 = BeautifulSoup(res, 'html.parser')
r1 = s1.select('.title')
for i in r1:
    print(i.text)











