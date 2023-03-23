import re

with open('re_test.txt', 'r', encoding='utf-8') as f:
    s = f.read()
# print(s)
pattern = "）(\w+.\w+.\w+.\w+)"
res = re.findall(pattern,s,re.S)
print(res)

