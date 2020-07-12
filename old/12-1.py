import xlwings as xw
import def_pailie
import random

app = xw.App()
wb = app.books.open('学位名单.xlsx')
names = wb.sheets['Sheet1'].range('b3:c16').value
wb.close()
app.quit()

speaker = random.sample(names, 3)
print(speaker)

'''
new_names = sorted(names, key=def_pailie.degree_order)

#names.sort(key=def_pailie.degree_order)

for n in new_names:
    print(n)
print('>>>>>>>>>以下是原来的排序列表名单>>>>>>>>>>>')
print(names)
'''