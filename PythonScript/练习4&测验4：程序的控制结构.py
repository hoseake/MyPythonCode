"""三位水仙花数"""
# num = []
# for i in range(100,1000):
#     a = eval(str(i)[0])
#     b = eval(str(i)[1])
#     c = eval(str(i)[2])
#     if(pow(a,3) + pow(b,3) + pow(c,3) == i):
#         num.append(str(i))
# print(",".join(num))
"""鸡兔同笼"""
# try:
#     h = int(input())
#     f = int(input())
#     '''if (type(eval(h)) != int or type(eval(f)) != int):
#         print("输入有误")
#         exit()
#     elif (h == None or f == None):
#         print("输入有误")
#         exit()
#     elif (' ' in h or ' ' in f):
#         print("输入有误")
#         exit()'''
# except:
#     print("输入有误")
#     exit()
# else:
#     flag = 0
#     for x in range(0,h+1):
#         y = h - x
#         if(2 * x + 4 * y == f):
#             flag = 1
#             break
#     if(flag == 1):
#         print("鸡有" + str(x) + "只\n兔有" + str(y) + "只")
#     else:
#         print("无解")
"""判断闰年"""
# year = input()
# try:
#     year = eval(year)
#     if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
#         print(str(year) + "年是闰年")
#     else:
#         print(str(year) + "年不是闰年")
# except:
#     print("输入错误")
#     exit()
"""四位玫瑰数"""
# for i in range(10000,999,-1):
#     a = eval(str(i)[0])
#     b = eval(str(i)[1])
#     c = eval(str(i)[2])
#     d = eval(str(i)[3])
#     if(pow(a,4) + pow(b,4) + pow(c,4) + pow(d,4)== i):
#         print(i)
"""60以内素数之和"""
# sum = 0
# for value in range(2,61):
#     for i in range(2,value):
#         if(value % i == 0):
#             break
#     else:
#         sum += value
# print(sum)



