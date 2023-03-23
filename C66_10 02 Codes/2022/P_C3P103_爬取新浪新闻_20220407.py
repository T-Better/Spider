import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
}
url = 'http://news.sina.com.cn/china/'
res = requests.get(url, headers = headers)
res.encoding = 'utf-8'
res = res.text

soup = BeautifulSoup(res, 'html.parser')
a = soup.select(".feed-card-item h2 a")  # select内容写的也是对的，但不知道为啥还是返回为空，感觉被反爬了
print(a)






