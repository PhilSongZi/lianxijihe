# -*- coding: utf-8 -*-
from typing import Text
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
import random


# 一定要看清楚自己写的东西到底是数字还是字母，大写还是小写，憋几把检查了，看一万遍都看不出来，纯笨比...
# 获取网页内容:需要 headers 和请求的 url，得到页面的 text 内容，交由下一个函数解析页面,提取出每个故事的名字和url
def getHTMLText(url, headers):
    try:
        r = requests.get(url=url, headers=headers, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        # print(r.text)
        return r.text

    except:
        return "爬取失败。"


# BeautiSoup解析初始url的页面，提取页面中故事名字和url的列表
def parsehtml(html, namelist, urllist):
    url = 'http://www.tom61.com/'
    soup = BeautifulSoup(html, 'lxml')
    t = soup.find('dl', attrs={'class': 'txt_box', })
    # print(t)
    i = t.find_all('a')
    # print(i)
    for link in i:
        urllist.append(url + link.get('href'))
        namelist.append(link.get('title'))


# 从url列表中挨个解析页面，提取每一个故事的文本内容
def parsehtml2(html):
    text = []
    soup = BeautifulSoup(html, 'lxml')
    t = soup.find('div', class_='t_news_txt')
    for i in t.find_all('p'):
        text.append(i.text)
    # print(text)
    return "\n".join(text)


# 发送邮件
def sendemail(url, headers):
    msg_from = '1823753665@qq.com'           # 发送方邮箱
    password = 'ykjyehqufqckbjhj'           # 发送方邮箱的授权码
    receivers = ['greensun.h@gmail.com, 15530403220@163.com', '942362954@qq.com', '980785020@qq.com']           # 收件人邮箱

    subject = '今日份的睡前小故事~'           # 主题
    html = getHTMLText(url, headers)
    content = parsehtml2(html)              # 正文
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = ','.join(receivers)

    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)    # 邮件服务器及端口号
        s.login(msg_from, password)
        s.sendmail(msg_from, msg['To'].split(','), msg.as_string())
        print("发送成功！")
    except:
        print("发送失败！")
    finally:
        s.quit()


def main():
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',}

    # 建列表存url和爬取故事的名字
    urllist = []
    namelist = []

    # 获取urllist
    for i in range(1, 11):
        if i == 1:
            url = 'http://www.tom61.com/ertongwenxue/shuiqiangushi/index.html'
        else:
            url = 'http://www.tom61.com/ertongwenxue/shuiqiangushi/index_' + str(i) + '.html'
        print("正在爬取第 %s 页的故事链接..." % i)
        print(url + '\n')
        html = getHTMLText(url, headers)
        parsehtml(html, namelist, urllist)
    print("爬取链接完成。")

    # 对url爬取故事
    '''
    for i in urllist:
        html = getHTMLText(i, headers)
        parsehtml2(html)
    '''

    sendemail(random.choice(urllist), headers)


if __name__ == '__main__':
    main()
