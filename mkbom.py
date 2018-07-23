# -*- coding: utf-8 -*-
__author__ = 'zhouxiaowei'
import xlrd
import xlwt
target_head = 3
target = 'usb_bom.xlsx'
allbom = 'all_bom.xlsx'
finalbom = 'fianl.xls'
#处理list里面的重复值函数
def f8(seq):
    seen = set()
    return [x for x in seq if x not in seen and not seen.add(x)]
#处理target bom，先把top和bottom元件分开，并把bottom元件加上（），然后合并value相同的位号
def merge_bom(target_bom):
    workbook = xlrd.open_workbook(target_bom)
    sheet0 = workbook.sheet_by_index(0)
    sheet0_list=[]
    for i in range(0,sheet0.nrows):
        sheet0_list.append(sheet0.row_values(i))
#删除Excel的头部标题
    target_head = 3
    target_tail = 2
    while target_head > 0:
        sheet0_list.pop(0)
        target_head-=1
    while target_tail > 0:
        sheet0_list.pop()
        target_tail-=1
#把bottom的位号加上（）
    sheet0_list_3=[]
    temp=[]
    for i in range(0,len(sheet0_list)):
        if sheet0_list[i][2] == 'Bottom':
            sheet0_list[i][0]='('+sheet0_list[i][0]+')'
#把封装和value合并
        sheet0_list[i][3]+='_'+sheet0_list[i][1]
        temp.append(sheet0_list[i][3])
#去除value重复的值
    sheet0_list_3=f8(temp)
#合并value相同的项
    #temp1=[[0 for col in range(0)] for row in range(len(sheet0_list_3))]
    temp1=[]
    print(len(temp1))
    for i in range(0,len(sheet0_list_3)):
        temp=[]
        for j in range(0,len(sheet0_list)):
            if sheet0_list_3[i] == sheet0_list[j][3]:
                temp.append(sheet0_list[j][0])
        temp1.append(temp)
        temp1[i].append(sheet0_list_3[i])
#统计位号的数量
    for i in range(0,len(temp1)):
        temp1[i].append(len(temp1[i])-1)

    return temp1



print(merge_bom(target))