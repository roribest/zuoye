#函数为处理输入进来的    名和姓   字符串,并且转换成列表
def name(n):
    name_ok = []
    for n in n.readlines():
        n = n.lstrip().replace('\n','').replace('、','')#删除字符串 左侧 端空格.剔除\n
        n.split('、')
        name_ok.extend(n)
    return name_ok

#整理,修改,姓
def first(fn):
    first_ok = []
    for a in fn.readlines():
        a = a.replace('\n','')
        a = a.split(' ')
        first_ok.extend(a)
    return first_ok


