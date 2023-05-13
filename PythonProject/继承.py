"""2022,3,17""" """2022,3,21"""
# 父类A
class A(object):
    def __init__(self):
        self.num = 10086
    def info_print(self):
        print(self.num)

class C(object):
    def __init__(self):
        self.num = 10010
    def print(self):
        print("10010")

# 子类B
class B(A,C): #多继承，B子类同时继承A父类和C父类,最先继承左边的类
    pass

test = B()
# test.info_print()
# test.print()

# 子类重写父类同名属性和方法
class fa0(object):
    def __init__(self):
        self.num = 10086
    def info_print(self):
        print(self.num)

class fa1(object):
    def __init__(self):
        self.num = 10010
    def info_print(self):
        print(self.num)

class son0(fa0,fa1):
    def __init__(self):
        self.num = 10000
    def info_print(self):
        print(self.num)
test0 = son0()
# test0.info_print()
# 结论：当子类里属性和方法和父类一样时，由子类创建的对象优先使用子类的属性和方法
print(son0.__mro__) #查看继承关系
# 子类调用父类同名属性和方法（也调用子类属性和方法）
class son1(fa0,fa1):
    def __init__(self):
        self.num = 10000
    def info_print(self):
        self.__init__() # 防止先调用父类属性时，父类属性覆盖子类属性
        print(self.num)
    def fa0(self):
        fa0.__init__(self) # 调用父类属性和方法时，属性在init初始化位置，所以需要再次调用init
        fa0.info_print(self) # 需要位置参数self
    def fa1(self):
        fa1.__init__(self)
        fa1.info_print(self)
test1 = son1()
# 如果先调用父类属性和方法，父类属性会覆盖子类属性，所以先调用子类的初始化
test1.fa0() # 调用父类fa0的属性和方法
test1.info_print() # 调用子类的属性和方法
test1.fa1() # 调用父类fa1的属性和方法