"""2022,1,2"""
# -------魔法方法------- __init__()
# -------作用：设置初始化属性
class Washer(object):
    def __init__(self):
        # 添加实例属性
        self.width = 500
        self.height = 800
    def print_info(self):
        print(f'{self.width}')
        print(f'{self.height}')

haier = Washer()
haier.print_info()

# --------带参数__init__()
print("带参数__init__()")
class Washer1():
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def print_infos(self):
        print(f'{self.width}')
        print(f'{self.height}')
haier1 = Washer1(100,200)
haier1.print_infos()

haier2 = Washer1(300,400)
haier2.print_infos()
"""2022,3,14"""
# 魔法方法str，一般用于输出对象的状态或类的说明文字
class Washer2:
    def __init__(self):
        self.width = 500
    def __str__(self):
        return "这是一个对象"
        #如果没有这个__str__，则只会打印对象的内存地址
haier3 = Washer2()
print(haier3)
# 魔法方法del，进程结束时会被自动调用
class Washer3:
    def __init__(self):
        self.width = 500
    def __del__(self):# 当程序结束时，这里的所以语句都将被执行
        print("进程结束")
        print("对象已被删除")
hair4 = Washer3()