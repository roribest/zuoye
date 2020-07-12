with open('/Users/jiangdiantao/myfile/17py/txt/erp.txt') as erp_file:
    f = erp_file.readlines()

erp_lst = [i.split(' ') for i in f]
nameLST = [ n[2] for n in erp_lst ]#得到名字列表
nameCount= [nameLST.count(s) for s in nameLST]

d = dict(zip(nameLST,nameCount))

print(d)

'''
########################excel############################
import xlwings as xw
#打开excel,读取文件
app = xw.App()
wb = app.books.add()
###########写入###############
sht = wb.sheets[0]
sht.range('A1').value = d
wb.save('/Users/jiangdiantao/myfile/17py/n.xlsx')
app.quit()

'''
