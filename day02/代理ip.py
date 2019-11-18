#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by 秋叶夏风

# 本模块的功能:<>
from re import *
from requests import get

from fake_useragent import UserAgent
ua = UserAgent()
url = "http://www.ip.cn"

headers = {
    'User-Agent':ua.random
}
prox = {
    'http':'47.75.90.57:80',
    'https':'47.75.90.57:80',
}
# 发起请求
# res = get(url,headers = headers,proxies=prox)
res = get(url,headers = headers)
res.encoding = 'utf-8'
# print(res.status_code)
# print(res.text)





# 判断能不能成

if res.status_code == 200:
    data = res.text
    pat = '<p>您现在的 IP：<code>(.*?)</code>'
    ip = search(pat,data).group(1)
    print(f"成了!,请求状态成功,当前ip是{ip}")
else:
    print('当前请求失败!')











'''

       ┌─┐       ┌─┐ + +
    ┌──┘ ┴───────┘ ┴──┐++
    │                 │
    │       ───       │++ + + +
    ███████───███████ │+
    │                 │+
    │       ─┴─       │
    │                 │
    └───┐         ┌───┘
        │         │
        │         │   + +
        │         │
        │         └──────────────┐
        │                        │
        │                        ├─┐
        │                        ┌─┘
        │                        │
        └─┐  ┐  ┌───────┬──┐  ┌──┘  + + + +
          │ ─┤ ─┤       │ ─┤ ─┤
          └──┴──┘       └──┴──┘  + + + +
                 神兽保佑
                代码无BUG!


'''
