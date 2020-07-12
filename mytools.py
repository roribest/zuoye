from decimal import Decimal

def sqr(x):
    if isinstance(x,int):
        return sqr_int(x)
    elif isinstance(x,float):
        return sqr_float(x)
    elif isinstance(x,list):
        return sqr_list(x)        


def sqr_int(x):
    result = x*x
    return result

def sqr_float(x):
    s = Decimal(str(x))
    result = s*s
    return result
    
def sqr_list(x):
    result = []
    for i in x:
        result.append(i*i)
    return result



''''
def sqr(x):
    result = ''

    if isinstance(x,int):
        result = x ** 2

    elif isinstance(x,float):
        s = Decimal(str(x))
        result = s*s

    elif isinstance(x,list):
        result = []
        for i in x:
            result.append(i*i)
    return result
'''