import requests

url = r'https://detail.tmall.com/item.htm?id=659465187615'

try:
    r = requests.get(url)
    r.raise_for_status()
    print(r.text)
except Exception as res:
    print(res)

