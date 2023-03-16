# 爬：百度搜索python的结果
import requests

def parse(url,kv):
    # 爬：百度搜索python的结果
    r = requests.post(url,params=kv)
    r.raise_for_status()
    return r.text


if __name__ == "__main__":
    url = r"https://www.baidu.com/s"
    kv = {'wd': 'python'}
    bdata = parse(url, kv)
    with open('./baidu.txt',mode='w',encoding='UTF8') as f:
        f.write(bdata)



