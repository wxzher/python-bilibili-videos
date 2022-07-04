# -*- codeing = utf-8 -*-

# 导入所需要的工具包
import requests
import pandas
import re

# 需要爬取的网站
url = 'https://api.bilibili.com/x/space/arc/search?mid=1131457022&ps=30&tid=0&pn=1&keyword=%E9%AB%98%E8%80%83&order=pubdate'

# 定制访问头信息
headers = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36'}

# 获取服务器响应的信息
resp = requests.get(url=url, headers=headers)
# print(resp.text) # 打印
# 通过正则表达式获取数据
title = re.findall('"title":"(.*?)"', resp.text)
author = re.findall('"author":"(.*?)"', resp.text)
watch = re.findall('"play":(\d{1,})', resp.text)
brief = re.findall('"description":"(.*?)"', resp.text)
# 处理播放量，将其统一成万的单位
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
dm_file.to_excel('Data-人民日报.xlsx', sheet_name="人民日报的数据")
