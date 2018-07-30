# -*- coding: utf-8 -*-
__author__ = 'zhouxiaowei'
import xlrd
import xlwt
target_head = 3
target = 'usb_bom.xlsx'
allbom = 'all_bom.xlsx'
finalbom = 'fianl.xls'
R = ['R0201','R0402','R0603']
C = ['C0201','C0402','C0603']
#处理list里面的重复值函数
def f8(seq):
    seen = set()
    return [x for x in seq if x not in seen and not seen.add(x)]
#处理target bom，先把top和bottom元件分开，并把bottom元件加上（），然后合并value相同的位号,返回一个list
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
   # print(len(temp1))
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
#处理电阻和电容的值
    for i in R+C:
        for j in range(0,len(temp1)):
            if i in temp1[j][-2]:
                temp1[j][-2]=temp1[j][-2].split('_')
                #切片，去掉R C封装名称的首字母
                temp1[j][-2][-1]=temp1[j][-2][-1][1:]
                #处理电阻的精度问题
                if i in R:
                    if temp1[j][-2][-2]=='1%':
                        temp1[j][-2][-2]='F'
                    elif temp1[j][-2][-2]=='5%':
                        temp1[j][-2][-2]='J'
                    else:
                        print('erro!!!!!!!!!!!!!!!!')
                        print('please check name of R')
                    temp1[j][-2][0]+='Ω'
                    #调整电阻value顺序要和allbom一致
                    data=temp1[j][-2].pop(2)
                    temp1[j][-2].insert(0,data)
                else:
                    temp1[j][-2].reverse()#电容value倒序以和allbom一致
    for i in range(len(temp1)):
        print(temp1[i])
    return temp1

def compare_bom(target_bom,all_bom):
    target_list=merge_bom(target_bom)
    workbook = xlrd.open_workbook(all_bom)
    sheet0 = workbook.sheet_by_index(0)
    sheet0_list=[]
    for i in range(0,sheet0.nrows):
        sheet0_list.append(sheet0.row_values(i))
    #删除Excel的头尾标题
    target_head = 1
    target_tail = 0
    while target_head > 0:
        sheet0_list.pop(0)
        target_head-=1
    while target_tail > 0:
        sheet0_list.pop()
        target_tail-=1
    for i in range(len(sheet0_list)):
        print(sheet0_list[i])

def main():
    compare_bom(target,allbom)
    print('ok!')

if __name__ == '__main__':
    main()
