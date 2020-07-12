import xlwings as xw
with open('/Users/jiangdiantao/myfile/17py/txt/NYSE.txt') as f:
    BasicData = f.readlines()

creat_data = [ data.split(',') for data in BasicData ]
final_data = [ [ i[0], float(i[5]), int(i[6].strip()) ] for i in creat_data ]

def closeing(i):
    return i[1]

final_data.sort(key=closeing)

##写入excel##
app = xw.App()
wb = app.books.add()
#把内容写入表格….options(transpose=True)按照列的方式写入
sht = wb.sheets[0]
sht.range('A1').value = final_data
wb.save('/Users/jiangdiantao/myfile/17py/txt/nyse_list.xlsx')
app.quit()