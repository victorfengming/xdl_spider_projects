#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by 秋叶夏风

# 本模块的功能:<>


from requests import *

proxy = {
    'http':'http://27.152.91.34:9999',
    'https':'http://27.152.91.34:9999'
}

url = 'https://www.baidu.com/s?wd=ip'
response = get(url,proxy=proxy)
with open('baidu.html','wb') as f:
    f.write(response.content)
