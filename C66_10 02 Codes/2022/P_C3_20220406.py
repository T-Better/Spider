import re
import requests
"""
# 第三章课上练习
title = '<!--s-text--->双十一点燃线下经济  "小时达" 服务成<em>阿里巴巴</em>增长新引擎<!--/s-text-->'

title = re.sub('<.*?>','',title)
print(title)

company = '*华能信托'
company1 = re.sub('[*]','',company)
print(company1)
"""

# 爬不成功，因为查询百度前端代码格式早就变复杂了......
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
}
url = 'https://www.baidu.com/s?&wd=%E9%98%BF%E9%87%8C%E5%B7%B4%E5%B7%B4'
res = requests.get(url, headers=headers).text

# 提取网址和标题
p_href = '<h3 class="news-title_1YtI1"><a href="(.*?)"'
href = re.findall(p_href, res, re.S)
p_title = '<h3 class="news-title_1YtI1">.*?>(.*?)</a>'
title = re.findall(p_title, res, re.S)
# 提取日期和来源
p_date = '<span class="c-color-gray2 c-font-normal">(.*?)</span>'
date = re.findall(p_date, res)
p_source = '<span class="c-color-gray2 c-font-normal">(.*?)</span>'
source = re.findall(p_source, res)

# 数据清洗和打印
for i in range(len(title)):
    title[i] = re.sub('<.*?>','',title[i])
    print(str(i+1)+'.'+title[i]+'('+source[i]+' '+date[i]+')')
    print(href[i])


