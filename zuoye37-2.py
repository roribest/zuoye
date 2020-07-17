class Cle:
    def __init__(self, r):
        self.r = r
    def get_perimeter(self):
        zhouchang = 3.14*2*self.r
        print(f"圆的周长是{zhouchang}")

    def get_area(self):#计算面积
        mianji = 3.14*self.r*self.r
        print(f"圆的面积是{mianji}")

class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_perimeter(self):#计算周长
        print(f"长方形周长等于{(self.a+self.b)*2}")

    def get_area(self):#计算面积
        print(f"长方形的面积等于{self.a*self.b}")

class  Suqre:
    def __init__(self, a):
        self.a = a
    def get_perimeter(self):
        print(f"正方形周长等于{self.a*4}")

    def get_area(self):
        print(f"正方形面积等于{self.a**2}")

def tools(shape):
    print(shape.get_perimeter())
    print(shape.get_area())

c1 = Cle(8)
r1 = Rect(4,3)
s1 = Suqre(2)

tools(c1)
tools(r1)
tools(s1)