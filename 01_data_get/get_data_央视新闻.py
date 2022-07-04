# -*- codeing = utf-8 -*-

# 导入所需要的工具包
import requests
import pandas
import re

# 需要爬取的网站放入列表中
urls = ['https://api.bilibili.com/x/space/arc/search?mid=456664753&ps=30&tid=0&pn=1&keyword=%E9%AB%98%E8%80%83&order=pubdate',
        'https://api.bilibili.com/x/space/dynamic/search?keyword=%E9%AB%98%E8%80%83&pn=1&ps=30&mid=1131457022']
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
    title.extend(re.findall('"title":"(.*?)"', resp.text))
    author.extend(re.findall('"author":"(.*?)"', resp.text))
    watch.extend(re.findall('"play":(\d{1,})', resp.text))
    brief.extend(re.findall('"description":"(.*?)"', resp.text))

# 对播放量信息进行处理，使其单位为万
i = 0
while i < len(watch):
    watch[i] = int(watch[i]) / 10000
    i += 1

# 导出数据
# 将所需要的数据用字典表示
info = {'标题': title, 'up主': author, '播放量(万)': watch, '简介': brief}
# 字典转变成dataframe形式数据
dm_file = pandas.DataFrame(info)
# 写入表格
dm_file.to_excel('Data-央视新闻.xlsx', sheet_name="央视新闻的数据")
