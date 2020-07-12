a = 5

def f1(a):
    print(a)
    return

def f2(x):
    x += a
    return x

def f3(x):
    a = 2
    x += a
    return x

def f4(x):
    a= 4
    a = a + x
    print(a)
    return


if __name__ == '__main__':
    f1(3)  #3

    a = f2(3)#8
    print(a)

    b = f3(3)#5
    print(b)

    f4(3)#8