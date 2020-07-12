import xlwings as xw
import def_pailie
import random

app = xw.App()
wb = app.books.open('/Users/jiangdiantao/myfile/17py/xing.xlsx')
names = wb.sheets['Sheet1'].range('b3:d657').value

names.sort(key=def_pailie.pailie)
for i in names:
    print(i)

sht = wb.sheets['Sheet1']
sht.range('B3').value = names
wb.save()
wb.close()
app.quit()