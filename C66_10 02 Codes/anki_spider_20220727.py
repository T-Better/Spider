import requests


url1 = 'https://pic.netbian.com/uploads/allimg/211102/112157-16358233172231.jpg'
p1 = r'D:/pics/p1.jpg'

r = requests.get(url1)
with open(p1,'wb') as f:
    f.write(r.content)

f.close()

