from random import sample, randint
import xlwings as xw

#随机创建20个随机姓名. 再写入excel文件中.
first_name = ['赵', '钱', '孙', '李']
last_name = ['慧', '志', '雅', '琳', '秋', '月', '宏', '云']
last_name = last_name * 2
name_list = []

i = 0  #计数器
while i < 20:
    name = ''.join(sample(first_name,1) + sample(last_name,randint(1,2)))

    if name not in  name_list:#判断创建出的随机姓名,是否包含在名单中.防止重名
        name_list.append(name)
        i += 1

print(name_list)

#打开excel,读取文件
app = xw.App()
wb = app.books.add()
#把内容写入表格
sht = wb.sheets[0]
sht.range('A1').options(transpose=True).value = name_list
wb.save('d://17py//exl//name_list.xlsx')
#wb.close()
app.quit()