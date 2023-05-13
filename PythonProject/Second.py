"""2021,11,2"""
#-------------------引用之可变类型
aa = [10,20]
bb = aa
print(id(aa))
print(id(bb))
aa.append(30)
print(aa)
print(bb)  #列表是可变类型
#-------------------引用当作实参
def test(a):
    print(a)
    print(id(a))
    a += a
    print(a)
    print(id(a))
b = 100
test(b)

c = [100,200]
test(c)
#--------可变类型：
#               列表
#               字典
#               集合
#--------不可变类型：
#                整型
#                浮点型
#                字符串
#                元组
"""2021,11,14"""
#----------------递归----------------
def sumNum(num):    #1.函数内部调用自己
    if num == 1:    #2.递归必须要有出口
        return 1
    else:
        return num + sumNum(num-1)
print(sumNum(3))
#----------------Lambda表达式 （匿名函数）--------
#----------------适用于只有一个返回值
#------------Lambda 参数列表 : 返回值
def lam1():
    return 100
#print(lam)
print(lam1())

lam2 = lambda :200
print(lam2)   #打印出lambda内存地址
print(lam2())
"""2021,11,15"""
#------------Lambda 计算a + b
#------函数方式
def add(a,b):
    return a + b
print(add(1,2))
#------Lambda方式
adds = lambda a,b:a+b
print(adds(2,3))
#------------带判断的Lambda表达式
num = lambda a,b:a if a>b else b
print(num(100,101))
#------------列表内字典数据排序
student = [
    {'name':'TOM','age':20},
    {'name':'Alice','age':19},
    {'name':'BOb','age':18},
]
student.sort(key = lambda x:x['name'])   #按名字升序排序
print(student)
student.sort(key = lambda x:x['name'],reverse=1)   #按名字降序排序
print(student)
student.sort(key = lambda x:x['age'])    #按岁数升序排序
print(student)
student.sort(key = lambda x:x['age'],reverse=1)   #按岁数降序排序
print(student)
#-------------高阶函数
#-------------把一个函数作为参数传入
#-------------abs()函数求参数的绝对值
#-------------round()函数求参数的四舍五入值
print(abs(-10))
print(round(1.5654))
"""2021,11,16"""
#-------------高阶函数写法
def LLF(a,b):
    return abs(a) + abs(b)
print(LLF(-10,2))

def HLF(a,b,f):
    return f(a) + f(b)
print(HLF(-10,2,abs))  #高阶函数传入函数时仅传函数名
#-------------高阶函数--map,reduce,filter
#map(func,list) 将传入函数func作用于list列表的每一个函数
list1=[1,2,3,4,5,6]
def fun(x):
    return x**2
result = map(fun,list1)
print(result)  #会打印一串内存地址
print(list(result))  #list数据类型转换
#reduce(func,list) 将每次func计算的结果和列表下一个元素做累积计算，func必须要有两个参数，需导入functools函数库
import functools
def func(a,b):
    return a + b
result1 = functools.reduce(func,list1)
print(result1)
#filter(func,list) 用于过滤序列，过滤掉不符合条件的元素
list2 = [1,2,3,4,5,6,7,8,9,10]
def func1(x):
    return x % 2 == 0
result2 = filter(func1,list2)
print(result2)
print(list(result2))




















