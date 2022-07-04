# -*- codeing = utf-8 -*-

# 导入所需要的工具包
import random  # 生成随机数
import time
from numpy import number  # 时间
import requests  # 发送请求获取服务器响应
from bs4 import BeautifulSoup  # 分析数据，提取要挖掘的信息
import pandas

# 定制网站
# 关键词
userSeach = '高考'
# 定制page值
page = 1
# 定制计数器
viedoNum = 0
#
val = 0
# 定制主要界面
mainUrl = 'https://search.bilibili.com/all?keyword='+userSeach + \
    "&from_source=webtop_search&spm_id_from=333.1007&order=pubdate"


# -*- codeing = utf-8 -*-

# 导入所需要的工具包
import requests
import pandas
import re

# 需要爬取的网站放入列表中
urls =  ['https://api.bilibili.com/x/web-interface/web/channel/multiple/list?channel_id=8740&sort_type=hot&offset=257309942_1654932531&page_size=30',
 'https://api.bilibili.com/x/web-interface/web/channel/multiple/list?channel_id=8740&sort_type=hot&offset=982416052_1654950692&page_size=30',
 'https://api.bilibili.com/x/web-interface/web/channel/multiple/list?channel_id=8740&sort_type=hot&offset=641700737_1654945091&page_size=30',
 'https://api.bilibili.com/x/web-interface/web/channel/multiple/list?channel_id=8740&sort_type=hot&offset=684782342_1654959915&page_size=30',
 'https://api.bilibili.com/x/web-interface/web/channel/multiple/list?channel_id=8740&sort_type=hot&offset=639852176_1654969432&page_size=30',
 'https://api.bilibili.com/x/web-interface/web/channel/multiple/list?channel_id=8740&sort_type=hot&offset=684451807_1655005395&page_size=30',
 'https://api.bilibili.com/x/web-interface/web/channel/multiple/list?channel_id=8740&sort_type=hot&offset=342361396_1655018685&page_size=30',
 'https://api.bilibili.com/x/web-interface/web/channel/multiple/list?channel_id=8740&sort_type=hot&offset=642140193_1655031056&page_size=30',
 'https://api.bilibili.com/x/web-interface/web/channel/multiple/list?channel_id=8740&sort_type=hot&offset=639750740_1655050188&page_size=30',
 'https://api.bilibili.com/x/web-interface/web/channel/multiple/list?channel_id=8740&sort_type=hot&offset=727273447_1655092549&page_size=30',
 'https://api.bilibili.com/x/web-interface/web/channel/multiple/list?channel_id=8740&sort_type=hot&offset=427267366_1655111874&page_size=30',
 'https://api.bilibili.com/x/web-interface/web/channel/multiple/list?channel_id=8740&sort_type=hot&offset=342230125_1655130445&page_size=30',
 'https://api.bilibili.com/x/web-interface/web/channel/multiple/list?channel_id=8740&sort_type=hot&offset=897494098_1655174389&page_size=30',
 'https://api.bilibili.com/x/web-interface/web/channel/multiple/list?channel_id=8740&sort_type=hot&offset=939966262_1655199076&page_size=30']
 
        
# 定制访问头信息
headers = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36'}
# 因为需要翻页，所以需要列表存储数据
title = []  # 标题
author = []  # 作者
watch = []  # 播放量
brief = []  # 简介
# 遍历网址列表中的网址信息
for url in urls:
    # 获取服务器响应信息
    resp = requests.get(url=url, headers=headers)
    # print(resp.text) # 打印相关信息
    # 通过正则表达式获取相关信息
    title.extend(re.findall('"name":"(.*?)"', resp.text))
    author.extend(re.findall('"author_name":"(.*?)"', resp.text))
    watch.extend(re.findall('"view_count":"(.*?)"', resp.text))

print(len(title))
print(len(author))
print(len(watch))

# 导出数据
# 将所需要的数据用字典表示
info = {'标题': title, 'up主': author, '播放量(万)': watch}
# 字典转变成dataframe形式数据
dm_file = pandas.DataFrame(info)
# 写入表格
dm_file.to_excel('Data-总（最新）.xlsx', sheet_name="最新最热的数据")
