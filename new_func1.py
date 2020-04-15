#-*-coding:utf-8-*-
# Time:2020/4/14 0:24
# Author:Zhoumo

import os
import xlwt
import pymysql

file_dir1 = 'x:/'
file_dir2 = 'z:/'

'''
for root1,dir1,file1 in os.walk(file_dir1):
    for name in file1:
        print(os.path.join(file_dir1,name))

for root2, dir2, file2 in os.walk(file_dir2):
    for name in file2:
        print(os.path.join(file_dir2,name))
'''

# 格式：pymysql.connect("服务器地址","用户名","用户密码","数据库名",charset)
database = pymysql.connect("127.0.0.1","root","1qaz@WSX3edc","testdb",charset='utf8')

# 初始化指针
cursor = database.cursor()

insert_sql = "INSERT INTO BOOKINDEX (NO,BOOKNAME,PATH) VALUES (%s,%s,%s)"

count = 0

for root1,dir1,file1 in os.walk(file_dir1):
    for name in file1:
        # data = [name,dir1,'1']
        count = count + 1
        cursor.execute(insert_sql,(count,name,os.path.join(root1,name)))

for root2,dir2,file2 in os.walk(file_dir2):
    for name in file2:
        # data = [(name,root2+dir2,1)]
        count = count + 1
        cursor.execute(insert_sql,(count,name,os.path.join(root2,name)))

database.commit()
database.close()
