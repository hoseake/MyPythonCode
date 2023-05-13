"""创建Car类的对象，引用属性和方法"""
# class Car:
#     madeby='中国'
#     def __init__(self,newbrand,newcolor):                                       #1 定义构造方法
#         self.brand = newbrand                        #2 给实例变量 brand 赋值
#         self.color = newcolor                        #3 给实例变量 color 赋值
#     def stat(self):
#         print('{}品牌的{}汽车'.format(self.brand,self.color))    #4 显示实例变量brand，color
#     def run(self):
#         self.stat()                                      #5 引用stat方法
#         print("汽车准许在{}境内行驶".format(self.madeby))  #6 显示类变量 madeby
# bmw=Car("华晨宝马","火焰蓝色")                        #7 创建对象bmw，华晨宝马,火焰蓝色
# benz = Car("奔驰","银灰色")                        #8 创建对象benz，奔驰,银灰色
# Car.madeby='美国'
# bmw.run()
# print("{}的{}汽车由{}制造".format(bmw.color,bmw.brand,bmw.madeby))  #9 显示bmw对象的变量 color , brand, madeby
# benz.color = "雪山白色"                        #10 重置benz对象的color属性为'雪山白色'
# benz.stat()                        #11 引用benz对象的stat方法

"""类的继承"""


# 例9-3-1  继承
class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make  # 牌子
        self.model = model
        self.year = year
        self.odometer = 0  # 里程

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        '''读取里程数'''
        return self.odometer

    def set_odometer(self, meter):
        '''设置里程数'''
        if meter > self.odometer:
            self.odometer = meter

    def increment_odometer(self, mileage):
        '''增加里程数'''
        self.odometer += mileage


# ElectricCar继承了Car。
# 1. 类名ElectricCar之后括号内的Car，表示用作父类。
# 2. 子类的构造方法中，要调用父类的构造方法。
# 这里补充代码：定义子类（先去掉所有下划线、再填写代码，并注意缩进）
class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year, battery_size):
        """初始化父类和子类的属性"""
        # 这里补充代码：初始化父类的属性（先去掉所有下划线、再填写代码，并注意缩进）
        super().__init__(make, model,year)
        # Car.__init__(self,make, model,year)
        # 这里补充代码：初始化子类类的属性（先去掉所有下划线、再填写代码，并注意缩进）
        self.battery_size = battery_size

    def get_battery_size(self):  # 子类的方法
        return self.battery_size


my_tesla = ElectricCar('tesla', 'model s', 2016, 70)
# 继承使得子类拥有了父类定义的属性
my_tesla.set_odometer(200)
my_tesla.increment_odometer(400)

print(my_tesla.get_descriptive_name())
print(my_tesla.read_odometer())
print(my_tesla.get_battery_size())

