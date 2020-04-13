#-*-coding:utf-8-*-
# Time:2020/4/6 23:13
# Author:Zhoumo

# 读取表格模板中的表头数据以及样式，在基础上添加插入数据
# 模板格式  日期  销售商  来源省份  单价（元/吨）  入库量（吨）
# 我们需要将excel表格的数据进行处理以后再保存在另外一个文件中去

import os
import xlrd
import xlwt
import xlutils3

from xlutils.copy import copy
import time

path_template =os.path.dirname(os.path.dirname(os.path.abspath('.')))
# 拼接模板文件路径
input_dir = path_template + r'\input\xlrd.xlsx'
# 拼接生成数据文件路径
output_dir = path_template + r'\output\output.xls'

def w_table():
    # 读取工作簿
    xlsx_in = xlrd.open_workbook(input_dir)
    xlsx_out = xlwt.Workbook(encoding='utf-8')
    # 读取对应的第一张表格
    table = xlsx_in.sheet_by_index(0)
    # 复制工作簿
    # newTB = copy(table)
    # 获取第一个工作表sheet0
    # newSht = newTB.sheets

    # 输出表格新建sheet
    worksheet = xlsx_out.add_sheet('My Work')

    # 写表头
    worksheet.write(0, 0, label='NAME')
    worksheet.write(0, 1, label='QUANTITY')

    dealer1 = dict()
    rows_num = table.nrows

    for row in range(1,rows_num):
        cell_value = table.cell_value(row, 1)
        unit_price = table.cell_value(row, 4)

        if cell_value in dealer1.keys():
            price_value = dealer1[cell_value] + unit_price
            dealer2 = {cell_value:price_value}
            dealer1.update(dealer2)
        else:
            dealer2 = {cell_value:unit_price}
            dealer1.update(dealer2)

    print(dealer1)

    i = 0
    j = 0

    for k,v in dealer1.items():
        worksheet.write(i+1,j,k)
        worksheet.write(i + 1, j + 1, v)
        i = i + 1

    #for n in

    xlsx_out.save(output_dir)

w_table()





