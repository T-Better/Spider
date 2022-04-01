import requests

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}
url_bd_albb = r'https://www.baidu.com/s?ie=UTF-8&wd=%E9%98%BF%E9%87%8C%E5%B7%B4%E5%B7%B4'
r = requests.get(url_bd_albb, headers = header)
local_path1 = r'D:\Git_Reps\SoftTest\Spider_Man\Spider\C66_10 02 Codes\百度搜索阿里巴巴20220401.txt'
with open(local_path1, 'w', encoding='utf-8') as f:
    f.write(r.text)
    print(r.text)
    print('爬取成功')

