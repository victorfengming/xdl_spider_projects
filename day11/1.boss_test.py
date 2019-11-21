#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by 秋叶夏风

# 本模块的功能:<>

from requests import get
from lxml import etree


headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
}
# html = ''
def parse_detailed_page(url):
    # response = get(url,headers=headers)
    with open('detailed_parse.html','r+',encoding='utf-8') as f:
        html = f.readlines()
    return html




url = 'https://www.zhipin.com/job_detail/187fe018dd2a187e0nd83t60E1M~.html?ka=search_list_10'
html = parse_detailed_page(url)

print()

html_ele = etree.HTML(str(html))

publish_ele = html_ele.xpath('//div[@class="job-author"]/span/text()')[0]
title_ele = html_ele.xpath('//h1/text()')[0]
salary = html_ele.xpath('//span[@class="badge"]/text()')[0]
all_info = html_ele.xpath('//div[@class="info-primary"]/p//text()')
job_desc = html_ele.xpath('//div[@class="text"]//text()')
print(title_ele)






























