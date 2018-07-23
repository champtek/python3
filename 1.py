# -*- coding: utf-8 -*-
import xlrd
import xlwt
import win32com.client as win32w
from xlutils.copy import copy
workbook = xlrd.open_workbook('1.xlsx')
#use xlutils.copy
workbookcopy = copy(workbook)
ws=workbookcopy.get_sheet(0)
workbookcopy.save('1cp.xls')

workbook = xlrd.open_workbook('1cp.xls')
sheng = workbook.sheet_by_index(0)
print('sheng.nrows=',sheng.nrows)
sheet_name = workbook.sheet_names()
for sheet_name in sheet_name:
    sheet2 = workbook.sheet_by_name(sheet_name)
    if 'Sheet1' == sheet2.name:
        print(sheet2.name,sheet2.row_values(3))
        print(sheet2.name,sheet2.col_values(1))
        row3 = sheet2.row_values(3)
        col0 = sheet2.col_values(0)
        lens_row3 = len(row3)
        for number in range(0,lens_row3):
            print(row3[number])
        lens_row3_4 = len(row3[4])
        print('lens_row3_4=',lens_row3_4)
        print(type(row3[4]))
        row3_4_list = row3[4].strip(',').split(',')
        print(col0)
#find 1.0
        for i in range(0,len(col0)):
            if 1==col0[i]:# -*- coding: utf-8 -*-
                num = i
#find ''
        for i in range(0,len(col0)):
            if ''==col0[i] and i > num:
                print("merge col_num=",(i-1),i)
                row_1 = sheet2.row_values(i-1)
                #change char to list
                row_1_4 = row_1[4].strip(',').split(',')
                row_2 = sheet2.row_values(i)
                row_2_4 = row_2[4].strip(',').split(',')
                print(row_1_4)
                print(row_2_4)
                row_1_4+=row_2_4
                print(row_1_4)
                print(type(row_1_4))
        for i in range(0,len(row_1_4)):
            row_1_4[i]='('+row_1_4[i]+')'
        print('row_1_4:',row_1_4)
                #charlist= ','.join(row_1_4)
                #workbookcopy = copy(workbook)
                #ws=workbookcopy.get_sheet(0)
                #ws.write(i-1,4,charlist)
                #workbookcopy.save('2cp.xls')
        #print(sheet2.col_values(0))

    else:
        pass

print(row_1)
row_1.insert(0,'yyyyyy')
print(row_1)
del row_1[0]
print(row_1)
a='0.1uF'


for i in range(0,len(row_1)):
    if a in str(row_1[i]):
        print(row_1[i])
        del row_1[i]
        break

#row_1.remove('0.1uF*')
print(row_1)
print(row_1.count(2.0))
row_1.count(2.0)
row_1.count(2.0)
#use xlwt
wbt = xlwt.Workbook()
sheet = wbt.add_sheet('sheet1')
wbt.save('wbt.xls')


