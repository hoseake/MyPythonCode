"""
2021,10,26
Debug
Function
"""
"""
name = 'HK'
print(name)
schoolName = '成都东软学院'
print(schoolName)
"""
#先定义函数
def prints(select):
    """说明文档仅在函数第一行书写。这是一个输入1返回一个字符串的函数"""
    if select == 1:
        name = 'HuangKe'
        return name
#再调用函数
print(prints(1))
help(prints)#仅放函数名
#打印横线
def print_line(num):
    print('-' * num)
print_line(100)
"""2021,10,27"""
a = 100
def testA():
    print(a)
def testB():
    global a   #声明a是全局变量，如未声明则是局部变量
    a = 200
    print(a)
testA()
testB()
print("全局变量a为：%s"%a)
def return_num():    #函数返回多个返回值
    #return 1,2,3     #返回的是一个元组形式
    #return后面还可以直接书写 元组 列表 字典，返多个值
    #return [1,2,3,4]#返回一个列表
    return {'name':'Python','age':'100'}
result = return_num()
print(result)
"""
2021,10,31
"""
def info(name,age,gender='男'):   #gender为缺省参数（默认值）
    print(name,age,gender)
info('黄科',20)   #如果没有传入参数，有默认值则使用默认值
def args(*args):     #*args是不定长位置参数（包裹位置传递）,可以多个，也可为空，但都会变成一个元组
    print(args)
args('黄科',20)
def kwargs(**kwargs):   #**kwargs是不定长关键字参数（包裹关键字传递），会变成一个字典
    print(kwargs)
kwargs(name='黄科',age=20,gender='男')
"""***************************元组拆包**********************************"""
def return_num():
    return 100,200#返回一个元组
num1,num2=return_num()
print(num1)
print(num2)
"""***************************字典拆包**********************************"""
dic1={'name':'黄科','age':20}
a,b=dic1
print(a,b)
print(dic1[a],dic1[b])