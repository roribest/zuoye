









class Chinese:
    def speak(self):
        print("我是中国学生,使用中文发言")
        
class English:
    def speak(self):
        print("我是英国学生,使用英语发言")
        
class Japanese:
    def speak(self):
        print("我是日本学生,使用日语发言")
    

def ask(stu):
    stu.speak()

s1 = Chinese()
s2 = English()
s3 = Japanese()


s1.speak()
s2.speak()
s3.speak()