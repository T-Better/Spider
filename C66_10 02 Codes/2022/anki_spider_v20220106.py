import requests

def get_baidu(url):
    try:
        r = requests.get(url)  
        r.raise_for_status
        return r.content
    except:
        return 'error req'


if __name__ == '__main__':
    url1 = 'http://www.baidu.com'
    res = get_baidu(url1)
    print(res)
    