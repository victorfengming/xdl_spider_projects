#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by 秋叶夏风

# 本模块的功能:<>

# 爬虫第一步,需求分析
# 获取免费代理,并验证代理的可用性

# 爬虫第二部,找到xicidaili

from requests import get

def get_free_proxy():
    url = "https://www.xicidaili.com/nn/"
    # 爬虫第三部
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
    }
    response = get(url,headers=headers)
    # 先下载下来再说
    with open('xici.html','wb') as f:
        f.write(response.content)


get_free_proxy()





