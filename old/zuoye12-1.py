import random

def my_shuffle(list):
    i = 0
    while i < 100:
        i += 1
        x = random.randint( 0,len(list)-1 )#x,y随机生成一个数,作为下标
        y = random.randint( 0,len(list)-1 )
        list[x], list[y] = list[y], list[x]#交换数值
    return list

if __name__ == '__main__':
    a = [1,2,3,4,5,6]
    print(my_shuffle(a))
