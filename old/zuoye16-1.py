import xlwings as xw
#打开excel,读取文件
app = xw.App()
wb = app.books.open('/Users/jiangdiantao/myfile/17py/exl/erp.xlsx')
names = wb.sheets['Sheet1'].range('B2:D1002').value
#########处理表格的数据###############
name_list = [i[1]for i in names[1:]]
d = {i:name_list.count(i) for i in name_list}
#作业第一题###每位员工的登录次数
for x,y in d.items():#遍历字典,获得字典d中的名字和登录次数
    print(f"[{x}]登录了{y}")
print('>'*50)
####登录次数最多的员工及其登录次数；
maxNUM = max(d.values())
minNUM = min(d.values())
for name,num in d.items():
    if num == maxNUM:
        print(f"[{name}]登录最次最多为{num}")
    elif num ==minNUM:
        print(f"[{name}]登录最次最少为{num}")
        
wb.close()
app.quit()