# -*- coding = utf-8 -*-
# @Time : 2020/4/22 22:15
# @Author : MooreChow
# @File : demo1.py 
# @Software: PyCharm

import os
import sys
from test01 import t01
import re
from bs4 import BeautifulSoup
import urllib.request,urllib.error
import xlwt
import sqlite3

path_template =os.path.dirname(os.path.dirname(os.path.abspath('.')))
# 拼接模板文件路径
input_dir = path_template + r'\input\douban_xlrd.xlsx'
# 拼接生成数据文件路径
output_dir = path_template + r'\output\douban_output.xls'


def main():
    baseurl = "https://movie.douban.com/top250?start="
    savepath = ".\\douban_movie_Top250.xls"
    # 1.爬取网页
    datalist = get_data(baseurl)

    # ask_url(baseurl)

    # 3.保存到excel文件
    save_data(datalist)

#影片的链接
findlink = re.compile(r'<a href="(.*?)">')
#影片的海报
findImgSrc = re.compile(r'<img.*src=(.*?)"',re.S) #re.S让换行符包含在字符中
#影片的片名
findTitle = re.compile(r'<span class="title">(.*?)</span>')
#影片评分
findRating = re.compile('<span class="rating_num" property="v:average">(.*?)</span>')
#评价人数
findJudge = re.compile('<span>(\d*)人评价</span>')
#电影概况
findInq = re.compile('<span class="inq">(.*?)</span>')
#找到影片相关内容
findBd = re.compile('<p class="">(.*?)</p>', re.S)


# 爬取网页
def get_data(basrurl):
    datalist = []
    for i in range(0,10):  # 循环10次，TOP250
        url = basrurl + str(i*25) + '&filter='
        html = ask_url(url)

        # 2.解析数据
        soup = BeautifulSoup(html,"html.parser")
        # datalist = soup.find_all(re.compile("a"))
        for item in soup.find_all('div',class_="item"):
            data = []
            item = str(item)
            # print(item)
            # break
            link = re.findall(findlink,item)[0]
            data.append(link)
            img = re.findall(findImgSrc,item)[0]
            data.append(img)
            title = re.findall(findTitle,item)
            if(len(title) == 2):
                title_01 = title[0]
                data.append(title_01)
                title_02 = title[1].replace(u'\xa0', u'')  # 替换无关符号
                title_02 = title_02.replace(u'/', u'')     # 替换无关符号
                data.append(title_02)
            else:
                data.append(title[0])
                data.append(' ')

            rating = re.findall(findRating, item)[0]
            data.append(rating)
            judgenum = re.findall(findJudge, item)[0]
            data.append(judgenum)

            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq = inq[0].replace(".","")
            data.append(inq)

            bd = re.findall(findBd, item)[0]
            bd = re.sub('<br(\s+)?/>(\s+?)',' ',bd)
            bd = re.sub('/'," ",bd)
            bd = bd.replace(u'\xa0', u'')
            data.append(bd.strip())
            #print(data)
            datalist.append(data)


    return datalist

# 得到一个制定的URL网页的内容
def ask_url(url):
    head = {  #模拟浏览器头部信息，向服务器发送消息
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
    }
    #用户代理，表示高速服务端我们是什么类型的浏览器，我们可以接受什么内容
    request = urllib.request.Request(url,headers=head)
    html = ""

    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)

    return html

def save_data(datalist):
    xlsx_out = xlwt.Workbook(encoding='utf-8')
    # 输出表格新建sheet
    worksheet = xlsx_out.add_sheet('My Work')

    # 写表头
    worksheet.write(0, 0, label='URL')
    worksheet.write(0, 1, label='POSTER')
    worksheet.write(0, 2, label='NAME')
    worksheet.write(0, 3, label='RATING')
    worksheet.write(0, 4, label='JUDGE NUM')
    worksheet.write(0, 5, label='INQUIRE')
    worksheet.write(0, 6, label='BRIEF')

    # print(type(datalist))
    # print(len(datalist[0]))
    # print(len(datalist))
    # print(type(datalist[1]))
    # print(type(datalist[2]))

    for k in range(len(datalist)):
        for j in range(len(datalist[0])):
            worksheet.write(k + 1, j, datalist[k][j])
            #print(datalist[k][j])


    xlsx_out.save(output_dir)



if __name__ == '__main__':
    main()



