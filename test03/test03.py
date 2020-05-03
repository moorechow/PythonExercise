# -*- coding = utf-8 -*-
# @Time : 2020/5/2 15:29 
# @Author : MooreChow
# @File : test03.py 
# @Software: PyCharm

import urllib.request,urllib.parse,urllib.error

# baseurl = "http://httpbin.org/post"
# data = bytes(urllib.parse.urlencode({"hello":"World"}),encoding='utf-8')
# response = urllib.request.urlopen(baseurl,data=data)
#
#
# print(response.read().decode('utf-8'))

# baseurl = "http://httpbin.org/get"
# try:
#     response = urllib.request.urlopen(baseurl,timeout=0.1)
#     print(response.read().decode('utf-8'))
# except urllib.error.URLError as e:
#     print("time out!")

# baseurl = "http://www.baidu.com"
# response = urllib.request.urlopen(baseurl)
# print(response.getheader("Server"))

baseurl = "http://www.douban.com"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
}

req = urllib.request.Request(url=baseurl,headers=headers,method="POST")
response = urllib.request.urlopen(req)

print(response.read().decode("utf-8"))
