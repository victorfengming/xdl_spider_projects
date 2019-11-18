import requests,re
from fake_useragent import UserAgent
ua = UserAgent()

# 访问的url地址
url = 'http://httpbin.org/get'
headers = {
    'User-Agent':ua.random
}
proxy = {
    'http':'47.75.90.57:80',
    'https':'47.75.90.57:80',
}
# 发起请求
res = requests.get(url,headers=headers,proxies=proxy,timeout=5)
# res = requests.get(url,headers=headers)

# print(res.status_code)
# print(res.text)

try:
    print(res.json()['origin'])
except:
    print('当前ip不好使')