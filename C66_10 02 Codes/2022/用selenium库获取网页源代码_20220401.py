from selenium import webdriver

browser = webdriver.Chrome()
url_finance = r'https://finance.sina.com.cn/realstock/company/sh000001/nc.shtml'
browser.get(url_finance)
data = browser.page_source  # 获取源码
local_path_finance = r'/SoftTest/Spider_Man/Spider/C66_10 02 Codes/2022/上证指数sourcepage_20220401.txt'
with open(local_path_finance, 'w+',encoding='utf-8') as f:
    f.write(data)
browser.close()



