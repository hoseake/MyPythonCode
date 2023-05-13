"""2021,12,6"""
# 需求：洗衣机   功能：洗衣服
# 1.定义洗衣机类
"""
class 类名():
      代码
"""
class Washer():
    def wash(self):
        print("洗衣服")
    def print_info(self):
        # 类里面获取实例属性
        print(f'宽度是{self.width}')
        print(f'高度是{self.height}')
    def dry(self):
        print("烘干")
        print(self)   # 验证self是什么
# 2.创建对象
# 对象名 = 类名()
hier = Washer()
hi = Washer()
# 3.验证成果
# 打印hier对象
print(hier) # 打印出的地址是对象的内存地址
print(hi)   # 不同的对象，地址也不相同
#使用wash功能------实例方法，对象方法
hier.wash()
hier.dry()
hi.dry()
# --------------self-------------
# 可见打印对象和打印self得到的内存地址相同，所以self指的是调用该函数的的对象
# --------------------------添加和获取对象属性
# -----------类外面添加属性
hier.width = 500
hier.height = 400
print(hier.height,hier.width) # 获取对象属性
# -----------类里面获取属性
hier.print_info() # 第11行

