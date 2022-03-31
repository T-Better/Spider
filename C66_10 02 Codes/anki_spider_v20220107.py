import requests

url1 = r'https://pic.netbian.com/uploads/allimg/211102/112157-16358233172231.jpg'
path1 = r'D:\BaiduNetdiskWorkspace\Super_coder\Soft_test\C66_10 爬虫\202201070922.jpg'

r = requests.get(url1)
with open(path1, 'wb') as f:
    f.write(r.content)
