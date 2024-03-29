#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by 秋叶夏风

# 本模块的功能:<用于练习xpath>

from requests import get
# 调用xpath的包
from lxml import etree
url = "http://lol.178.com/"

response = get(url)

# with open("178.html",'wb') as f:
#     f.write(response.content)

# 需要找到的是,/html/head/title

html_ele = etree.HTML(response.text)
# print(html_ele)

# title_ele = html_ele.xpath('/html/head/title')

# 找到了标签,如何找到标签内的内容
# print(title_ele[0].text)

# 另一种方式,就是xpath获取内部的字符串
# 串/html/head/title/text()'
# title_ele = html_ele.xpath('/html/head/title/text()')
# print(title_ele[0])

# 注意,最前面要是有一个/的话,就是从根目录开始
# 绝对路径方式这是

# meta_ele = html_ele.xpath('/html/head/meta[1]')
# print(meta_ele[0])

# 在Xpath中可以通过索引的方式获取具体的哪个标签
# 在python中从0开始,这里从1,开始

# charset_str = html_ele.xpath('/html/head/meta[1]/@charset')

# 通过@获取标签下面的属性
# print(charset_str[0])
# 记住,所有的xpath都会给我们返回一个列表,要在取第几个才行

# /html/head/link[1]/@href
# href_str = html_ele.xpath("/html/head/link[1]/@href")
# print(href_str[0])

# 谓词相关信息'/html/body/div[@class="wrap"]/@class'
# /html/body/div[2]
# div_ele = html_ele.xpath('/html/body/div[1]/@class')
# div_ele = html_ele.xpath('/html/body/div[@class="wrap"]/@class')

# div_ele = html_ele.xpath('/html/body/div[@class="wrap"]/div[1]/div[@class="head"]/@class')

# div_ele = html_ele.xpath('/html/body/div[1]/div/div[5]/div[3]/div[2]/ul[1]/li[2]/a/span[1]/text()')
# print(div_ele[0])


# /html/body/div[2]/div/div[5]/div[3]/div[2]/ul[1]/li[2]/a/span[1]

# 搜索内容 //div[@class="head"]

# div_ele = html_ele.xpath('//div[@class="head"]/div[1]/div[1]/a/text()')
# print(div_ele)

# div_ele = html_ele.xpath('//div[@class="Oldversion"]/a/text()')
# div_ele = html_ele.xpath('//div[@class="Oldversion"]/a/@href')
# print(div_ele)

# 获取所有的属性包含 itemprop的meta标签: /html/head/meta[@itemprop]/@itemprop
# 谓词
# div_ele = html_ele.xpath('/html/head/meta[@itemprop]/@itemprop')
# print(div_ele)

# 获取所有的属性不包含 itemprop的meta标签: '/html/head/meta[not(@itemprop)]'
# 需要使用not函数
# 函数
# div_ele = html_ele.xpath('/html/head/meta[not(@itemprop)]')
# print(div_ele)


# # 找到刚刚的ul,XPATH: //ul[@class="ul-nav-main"]//text()
# div_ele = html_ele.xpath('//ul[@class="ui-nav-main"]//text()')
# print(div_ele)
#
# # 列表推导式
# strs = [item for item in div_ele if item.strip()]
# print(strs)

# contains()函数 包不包含什么
# starts_with() 以什么开头的














