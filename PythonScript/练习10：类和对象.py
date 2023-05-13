"""Echo类"""
# class Echo:
#     EchoClassAttribute = "EchoClassAttribute" # 类属性
#     def __init__(self): # 实例属性
#         self.EchoInstanceAttribute = "EchoInstanceAttribute"
#     def EchoInstanceMethod(self): # 实例方法
#         return "EchoInstanceMethod"
#     @classmethod
#     def EchoClassMethod(cls): # 类方法
#         return "EchoClassMethod"
# e = Echo()
# print(Echo.EchoClassAttribute)
# print(Echo.EchoClassMethod())
# print(e.EchoInstanceAttribute)
# print(e.EchoInstanceMethod())
"""Python最小类"""
# class LeastClass:
#     @classmethod
#     def __doc__(cls):
#         return "这是一个最小类"
# print(LeastClass.__doc__())
"""创建医生类"""
# class Doctor:
#     hospital = "广东医附院"
#     salary=8000
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
#     def checkIn(self):
#         print("上班打卡已完成")
#     def getSalary(self):
#         self.checkIn()
#         print("{}医生{}本月的工资是{}元".format(Doctor.hospital,self.name,self.salary))
# surgeon=Doctor("张三",10000) # 外科医生
# print(Doctor.salary,surgeon.salary)
# surgeon.getSalary()
"""类的继承与多态"""
#例9-3-2  重写父类方法 --继承与多态
#鸭子父类
class Yazi():
    def __init__(self, type, height):
        self.type = type
        self.height = height

    def jiaosheng(self):
        print(type(self),"在基类(父类)","中叫:嘎嘎")
#橡皮鸭
class Xiangpiya(Yazi):
    def __init__(self, type, height):#这里补充代码（先去掉所有下划线、再填写代码，并注意缩进）
        super().__init__(type, height)
    #重写了Yazi父类的jiaosheng方法:这里补充代码（先去掉所有下划线、再填写代码，并注意缩进）
    def jiaosheng(self):
        print("派生类(子类)橡皮鸭叫:唧唧")
#水鸭
class Shuiya(Yazi):
    #继承了Yazi父类的jiaosheng方法
    def __init__(self, type, height):
        super().__init__(type, height)

baseYazi = Yazi("父类鸭子",1)
baseYazi.jiaosheng()

xpy = Xiangpiya("橡皮鸭", 3)
xpy.jiaosheng()

sy = Shuiya("水鸭", 0.5)
sy.jiaosheng()

class Monkey:
    def jiaosheng(self):
        print("猴子哭:哇哇哇哇")

def jiaosheng_twice(yazi):
    print("jiaosheng_twice(yazi) function:")
    yazi.jiaosheng()
    yazi.jiaosheng()

jiaosheng_twice(baseYazi)
jiaosheng_twice(xpy)
monkey1 = Monkey()
monkey1.jiaosheng()
jiaosheng_twice(monkey1)