#根据文件导入进来的,随机生成男女名字
import name_tool
from random import sample, randint
##############################读取文件:姓,男女名###############################################
first = open('/Users/jiangdiantao/myfile/17py/txt/xing.txt')
girl = open('/Users/jiangdiantao/myfile/17py/txt/girl.txt')
boy = open('/Users/jiangdiantao/myfile/17py/txt/boy.txt')

first_list = name_tool.first(first)#生成 姓 的列表
girl_list = name_tool.name(girl)#生成 女名 列表
boy_list = name_tool.name(boy)#生成 男名 列表

first.close()
girl.close()
boy.close()
##########################################################################
input_name = input('输入你要想随机生成的男或女的姓名:(输入男或者女)')
if input_name == '女':
    i = 0
    girl_name_list = ''
    while i < 1000:
        ran_girl_name = ''.join(sample(first_list,1) + sample(girl_list,randint(1,2)))
        girl_name_list = ran_girl_name + ' ' + girl_name_list 
        i += 1
    print(f"随机生成的女名为:\n{girl_name_list}")

elif input_name == '男':
    i = 0
    boy_name_list = ''
    while i < 1000:
        ran_boy_name = ''.join(sample(first_list,1) + sample(boy_list,randint(1,2)))
        boy_name_list = ran_boy_name + ' ' + boy_name_list 
        i += 1
    print(f"随机生成的名为:\n{boy_name_list}")

else:
    print('请输入男或者女.程序结束,请重新执行')