# -*- coding: utf-8 -*-
import xlrd
import xlwt
from xlutils.copy import copy
from operator import itemgetter,attrgetter
workbook = xlrd.open_workbook('mtk.xlsx')
sheet0 = workbook.sheet_by_index(0)
sheet0_list=[]
for i in range(0,sheet0.nrows):
    print(sheet0.row_values(i))
    sheet0_list.append(sheet0.row_values(i))
for i in range(0,2):
    print(sheet0_list[i])
    del sheet0_list[i]
print(len(sheet0_list))
j=0
k=0
top_list=[]
bottom_list=[]
for i in range(0,len(sheet0_list)):
    if 'Top'==sheet0_list[i][2]:
        top_list.append(sheet0_list[i])
        j=j+1
    elif 'Bottom' == sheet0_list[i][2]:
        bottom_list.append(sheet0_list[i])
        k=k+1
    else:
        print(sheet0_list[i])
print(j,k)
top_list.sort()
for i in range(0,348):
    print(top_list)










