
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
    "&from_source=webtop_search&spm_id_from=333.934&order=click"


# 定制所有界面
# 获取网页响应
mainSoup = BeautifulSoup(requests.get(url=mainUrl).text, "html.parser")
# 寻找代表网页数量的标签
pages = mainSoup.find('li', class_="page-item last")
# 判断网页数量来考虑pages的值
if(pages):
    pages = int(pages.text)
else:
    pages = 1
# 定义我们需要的数据
num = []  # 序号
title = []  # 标题
url = []    # 网址
brief = []  # 简介
author = []  # 作者/up主
watch = []  # 观看数/播放量
danmu = []  # 弹幕数
refreshtime = []    # 上传时间
# 循环获取网址数据
while page <= pages:
    o = (page-1)*36
    mainUrl = 'https://search.bilibili.com/all?keyword='+userSeach + \
        "&from_source=webtop_search&spm_id_from=333.934&order=click" + \
        '&page='+page.__str__()+"&o="+o.__str__()
    # 获取网页数据
    mainSoup = BeautifulSoup(requests.get(mainUrl).text, "html.parser")
    # 获取需要的数据
    for item in mainSoup.find_all('li', class_="video-item matrix"):
        # 计数器加一
        viedoNum += 1
        # 序号
        num.append(viedoNum.__str__())
        # 包含有效信息的“a”标签
        val = item.find('a', class_="img-anchor")
        # 获取标题信息
        title.append(val["title"])
        # 获取链接信息
        url.append(val['href'])
        # 获取简介信息
        # 注意用strip()方法去除空格和空行
        brief.append(item.find('div', class_="des hide").text.strip())
        # 获取up主信息
        author.append(item.find('a', class_="up-name").text.strip())
        # 获取播放量信息
        watch.append(item.find('span', title='观看').text.strip())
        # 获取弹幕数量信息
        danmu.append(item.find('span', title='弹幕').text.strip())
        # 获取上传时间信息
        refreshtime.append(item.find('span', title='上传时间').text.strip())

        # 提示视频爬取完成
        print("第"+viedoNum.__str__()+"个视频爬取完成")

    # 停顿几秒，以免网站把我们当作爬虫处理，虽然我们本来就是
    time.sleep(random.random() + 1)
    # 循环的计时器
    page += 1

# 整理信息导入表格
# 定制表头信息和对应的列表
info = {'序号': num, '标题': title, '网址': url, '简介': brief,
        'up主': author, '播放量(万)': watch, '弹幕': danmu, '发布时间': refreshtime}
# 建立一个dataframe类型的文件
dm_file = pandas.DataFrame(info)
# 存储到指定的表格中
dm_file.to_excel('Data-总（播放量）.xlsx', sheet_name="高考关键词的数据")
