"""温度转换Ⅰ"""
# TemString = input()
# if(TemString[-1] == "f" or TemString[-1] == "F"):
#     printTemC = (float(TemString[0:-1])-32)/1.8
#     print("{:.2f}C".format(printTemC))
# elif(TemString[-1] == "c" or TemString[-1] == "C"):
#     printTemF = float(TemString[0:-1])*1.8+32
#     print("{:.2f}F".format(printTemF))
# else:
#     print("输入格式错误")
"""温度转换Ⅱ"""
# TemString = input()
# if(TemString[0] == "f" or TemString[0] == "F"):
#     printTemC = (float(TemString[1:])-32)/1.8
#     print("C{:.2f}".format(printTemC))
# elif(TemString[0] == "c" or TemString[0] == "C"):
#     printTemF = float(TemString[1:])*1.8+32
#     print("F{:.2f}".format(printTemF))
"""数字形式转换"""
# numDict={"1":"一","2":"二","3":"三","4":"四","5":"五","6":"六","7":"七","8":"八","9":"九","0":"零"}
# num = input()
# for n in num[0:]:
#     print(numDict[n],end="")
"""货币转换"""
# MoneyString = input()
# RMB = "RMB";USD = "USD"
# USDFlag=0;RMBFlag=0
# for str,i in zip(MoneyString[0:3],range(0,3)):
#     if(str == RMB[i]):
#         RMBFlag+=1
#     if(str == USD[i]):
#         USDFlag+=1
# if(RMBFlag == 3):
#     UsdMoney = float(MoneyString[3:])/6.78
#     print("USD{:.2f}".format(UsdMoney))
# if(USDFlag == 3):
#     RmbMoney = float(MoneyString[3:])*6.78
#     print("RMB{:.2f}".format(RmbMoney))
"""格式化输出"""
# a = input()
# b = input()
# c,d = input().split(',')
# str1,str2 = input().split()
# print(pow(int(a),2))
# print("{:.3f}".format(abs(float(b))))
# print("c+d= {:d}".format(int(c)+int(d)))
# print("str1+str2={:s}".format(str1+str2))
"""求和或者求差或者求积"""
# a = int(input())
# b = int(input())
# if(a > b):
#     print(a-b)
# elif(a == b):
#     print(a*b)
# else:
#     print(a+b)
"""判断是否是闰年"""
# year = int(input())
# if((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
#     print("闰年")
# else:
#     print("非闰年")
"""Hello World的条件输出"""
int1 = int(input())
str1 = "Hello World"
length = len(str1)
if(int1 == 0):
    print("Hello World")
elif(int1 > 0):
    for p in range(0,length,2):
        print(str1[p:(p+2)])
else:
    for i in str1:
        print(i)
"""数值运算"""
str1 = eval(input())
print("{:.2f}".format(str1))
