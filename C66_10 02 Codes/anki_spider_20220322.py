import requests
"""
url1 = r'https://pic.netbian.com/uploads/allimg/211102/112157-16358233172231.jpg'
path1 = r'D:/pics/p1.jpg'
r = requests.get(url1)
with open(path1, 'wb') as f:
    f.write(r.content)
"""
url2 = r'http://python123.io/ws'
json1 = {'key1':'value1'}
res = requests.post(url2, json=json1)