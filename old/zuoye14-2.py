a = [ '中国队', '美国队','英国队','加拿大队','法国队' ]


c = [ f"{i}的对手是{k}" for i in a for k in a if i!=k]
print(c)