# -*- coding: utf-8 -*-
import xlrd
import xlwt
from xlutils.copy import copy
from operator import itemgetter,attrgetter
workbook = xlrd.open_workbook('mtk.xlsx')
sheet0 = workbook.sheet_by_index(0)
sheet0_list=[]
for i in range(0,sheet0.nrows):
#    print(sheet0.row_values(i))
    sheet0_list.append(sheet0.row_values(i))
for i in range(0,2):
#    print(sheet0_list[i])
    del sheet0_list[i]
print(len(sheet0_list))
j=0
k=0
top_list=[]
bottom_list=[]
'''分开top和bottom的元件'''
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
top_list_4=[]
for i in range(0,len(top_list)):
    top_list_4.append(top_list[i][4])

#    print(top_list[i])
#find the same value in list
def f8(seq):
    seen = set()
    return [x for x in seq if x not in seen and not seen.add(x)]
f8_list=[]
f8_list=f8(top_list_4)
new=[]
for i in range(0,len(f8_list)):
    for j in range(0,len(top_list)):
        if f8_list[i]==top_list[j][4]:
            new.append(top_list[j])
for j in range(0,len(new)):
    list(new[j][0])
print("new list len =",len(new))
#for i in range(0,len(new)):
#    print(new[i])
neww=[]
for i in range(0,len(f8_list)):
    k=0
    for j in range(0,len(new)):
        if f8_list[i]==new[j][4]:
            if not k:
                k=j
            else:
                new[k][0]+=','+new[j][0]
    neww.append(new[k])
res=['R0201','R0402','R0603','R0805']
for i in range(0,len(neww)):
    #print(neww[i])
    if neww[i][1] in res:
        neww[i][4]=str(neww[i][4])
        neww[i][4]=neww[i][4].split('_')
        neww[i][4][0]+='Ω'
        if len(neww[i][4])==3:
            if neww[i][4][2]=='1%':
                neww[i][4][2]='F'
            else:
                neww[i][4][2]='J'
        print(neww[i][4])
for i in range(0,3):
    print('*************************************************************************************************')
#read from all_bom.xlsx
workbook = xlrd.open_workbook('all_bom.xlsx')
sheet0 = workbook.sheet_by_index(0)
sheet0_list=[]
for i in range(0,sheet0.nrows):
    sheet0_list.append(sheet0.row_values(i))
    #print(sheet0_list[i])
for i in range(0,3):
    print('*************************************************************************************************')
#将字符串转换为list
for i in range(0,len(sheet0_list)):
    print(sheet0_list[i])
    sheet0_list[i][2]=sheet0_list[i][2].split('_')
#检查子bom的值是否在总bom里存在，如果存在就打印出来
for i in range(0,len(neww)):
    if neww[i][1] in res:
        if len(neww[i][4])==3:
            for j in range(0,len(sheet0_list)):
                if neww[i][4][0] in sheet0_list[j][2] and neww[i][4][1] in sheet0_list[j][2] and neww[i][4][2] in sheet0_list[j][2]:
                    neww[i][4]=sheet0_list[j][2]
                    print('...................................')
                    print(neww[i][4])
                    neww[i][4]='_'.join(neww[i][4])
                    print(neww[i][4])



#save list to excel

wk = xlwt.Workbook()
wsh = wk.add_sheet('bom_test')
for i in range(0,len(neww)):
    for j in range(0,len(neww[0])):
        wsh.write(i,j,neww[i][j])
wk.save('bom.xls')




#test str split to list
