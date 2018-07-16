# -*- coding: utf-8 -*-
import xlrd
import xlwt


numbers = [1,4,5]
position = 0
while position < len(numbers):
    number=numbers[position]
    if number%2 == 0:
        print('found even number',number)
        break
    position += 1
else:
    print('no even number found')
