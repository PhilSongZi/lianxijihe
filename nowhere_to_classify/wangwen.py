# -*- coding: utf-8 -*-


import requests
from bs4 import BeautifulSoup
import sys


'''
梳理一下过程：
url:https://www.bbiquge.cc/
1.从url得到想要的book的url
2.获得book详情页面包含的分章节url和章节名字
3.claw&sava
解析网页：bs4库的BeautifulSoup，解析器lxml（不知道为啥我这html解析器老是报错，蒜了就lxml了 多好用）
类的函数:1.初始化 2.获得url 3.获得文本内容 4.存
'''


class download_txt(object):

    def __init__(self):
        self.url = 'http://www.biqukan.com/'
        self.new_url = 'https://www.bbiquge.cc/book_127045/'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',}
        self.urls = []      # 章节对应url列表
        self.names = []     # 章节名列表
        self.nums = 0           # 章节数

    def get_url(self):
        try:
            r = requests.get(url=self.new_url, headers=self.headers, timeout=30)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            html = r.text
            # print(html)
            soup = BeautifulSoup(html, 'lxml')
            div = soup.find_all('div', id='list')
            # print(div)
            # 用beautifulsoup查找到某标签后，要进一步查其子标签，可以把它赋值给一变量，再beautifulsoup解析，查找标签。
            a_bf = BeautifulSoup(str(div[0]), 'lxml')
            a = a_bf.find_all('a')
            print(a)
            self.nums = len(a) - 12    # 切片处理。因为前12项是最新章节，去掉之后才是真章节数。# 切锤子片，直接减也行。
            # 直接获得所有a标签包含的链接，爬章节内容时直接对url和name切片去掉前12章即可从第一章开始爬。
            for each in a:
                self.names.append(each.string)
                self.urls.append(self.new_url + each.get('href'))

        except:
            print("爬取链接失败")

    def get_contents(self, url):
        try:
            r = requests.get(url=url, headers=self.headers, timeout=30)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            html = r.text
            print(html)
            soup = BeautifulSoup(html, 'lxml')
            texts = soup.find_all('div', id='content')
            print(texts)
            return texts
        except:
            print("爬取章节内容失败！")

    def save_txt(self):
        pass


if __name__ == '__main__':
    book1 = download_txt()
    book1.get_url()
    # print("开始下载小说：")
    # print(book1.urls[12])
    # book1.get_contents(book1.urls[12])
