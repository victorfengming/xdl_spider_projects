#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by 秋叶夏风

# 本模块的功能:<>

from requests import get
from lxml import etree
## 我们公司就是一个做足球相关app的公司
# 1.足球相关新闻
# 2. 足球赛事
# 3. 足球锦囊
#
# 这个函数是负责下载详情页的相关信息的

def get_detailed_page_info(url):
    # 爬虫第三步
    response = get(url)
    # with open('163.html','wb') as f:
    #     f.write(response.content)
    # 你拿到页面的第一步就是用withopen 去下载一下这个信息
    # 看一下和浏览器中的内容是否一样,
    # 要是不一样,那就要加useragent reference cookie等信息了

    # 爬虫第四步
    # 获取具体信息
    html_ele = etree.HTML(response.text)
    # / html / body / div[4] / div / div[2] / div[2] / a
    # event_name = html_ele.xpath('//div[@class="leftList2"]/div[@class="c2"]/a/text()')[0]
    # print(event_name)

    # 表格里面的xpath,获取所有的tr://div[@class="leftList4"]/table/tbody/tr

    # 这个tbody是浏览器自动添加的标签,
    # 所以爬之前先下载下来,再说
    # 审查元素和查看网页源代码是不一样的.
    tr_ele_list = html_ele.xpath('//div[@class="leftList4"]/table/tr')
    for i in range(1,len(tr_ele_list),3):
        # print(tr_ele_list[i])
        # 链式编程.
        round = tr_ele_list[i].xpath('./td[1]/text()')[0].strip()
        time = tr_ele_list[i].xpath('./td[2]/text()')[0].strip()
        status = tr_ele_list[i].xpath('./td[3]/text()')[0].strip()
        host_team = tr_ele_list[i].xpath('./td[4]//a/text()')[0].strip()
        score = tr_ele_list[i].xpath('./td[5]//a/text()')[0].strip().replace(" ","").replace("\n","")
        guest_team = tr_ele_list[i].xpath('./td[6]//a/text()')[0].strip()
        print(round, time, status, host_team, score, guest_team)
        print('-'*50)

        # 结果这样
        """
        1 02:00 完场 里昂 4-0 斯特拉斯堡
        --------------------------------------------------
        1 02:00 完场 梅斯 1-3 甘冈
        --------------------------------------------------
        1 02:00 完场 蒙彼利埃 1-0 卡昂
        --------------------------------------------------
        1 02:00 完场 圣埃蒂安 1-0 尼斯
        --------------------------------------------------
        1 02:00 完场 特鲁瓦 1-1 雷恩
        --------------------------------------------------
        1 21:00 完场 里尔 3-0 南特
        --------------------------------------------------
        1 23:00 完场 安格斯 2-2 波尔多
        --------------------------------------------------
        """




if __name__ == '__main__':
    url = 'http://goal.sports.163.com/schedule/20170806.html'
    get_detailed_page_info(url)
    pass
















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
