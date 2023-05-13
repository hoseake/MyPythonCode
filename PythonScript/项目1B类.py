"""激光样式"""
# count = 0
# def laser(num,state): # num代表第几个激光灯 state代表激光状态--1表示开 0表示关
#     global count
#     if (num == 30):  # 设定满足条件，当遍历到第三十盏灯时表示一种可能
#         count += 1
#     if (num > 30):  # 设定终止条件，因为目标是30盏灯，所以超过30就停止
#         return
#     if(state == 0):# 如果当前灯为关，那么下一盏灯可以为开或关
#         laser(num+1,0) #下一盏灯为关
#         laser(num+1,1) #下一盏灯为开
#     else:# 如果当前灯为开，那么下一盏灯肯定为关
#         laser(num+1,0) #下一盏灯为关
#
# # 开始第一盏灯的两种情况
# laser(1,0)
# laser(1,1)
# print(count)

"""杨辉三角"""
# N = eval(input())
# allList = [[1],[1,1]] # 第一层和第二层
# for i in range (2,500):# 先生成500层的杨辉三角
#     preList = allList[i - 1] # 定义逻辑上的上一层
#     newList = [1] # 每一层的第一个数都是1
#     for j in range(i - 1): # 使用循环为每层中间的几个数赋值
#         newList.append(preList[j] + preList[j+1]) # 中间的数等于上层左右两数之和
#     newList.append(1) #定义每层最后一个数
#     allList.append(newList) # 把当前层的数存入总的列表
# # print(allList)
# count = 1
# countList=[]
# for x in allList:
#     for num in x:
#         countList.append(num)
# for position in countList:
#     if (int(position) == N):
#         break
#     count += 1
# print(count)

"""求256MB可存放的多少个元素"""
# listInt = 4
# memorySpace = 256 * 1024 * 1024
# print(int(memorySpace/4))

"""换零钞"""
for x in range(1,200):
    for y in range(1,40):
        if( x*1 + 10*x*2 + 5*y == 200):
            print(x+10*x+y)

"""时间显示"""
# time1 = eval(input())
# time1 = time1/1000
# hour = int(time1/3600%24)
# minute = int(time1/60%60)
# second = int(time1%60)
# print("{0:0>2d}:{1:0>2d}:{2:0>2d}".format(hour,minute,second))
# # print("{列表索引:填充字符>2d}:{1:0>2d}:{2:0>2d}".format(hour,minute,second))
# # >表示向左填充     <表示向右填充      2d表示保留两个字符位

"""回文日期"""
# def judge(year, month, day):
#     # 判断日期的合理性
#     # 是否是闰年，闰年的二月比较特殊
#     if (year % 4 == 0 and year % 400 != 0) or year % 400 == 0:
#         if month == 2 and day > 29:
#             return False
#     else:
#         if month == 2 and day > 28:
#             return False
#     # 月份是否合理
#     if month > 12 or month <= 0:
#         return False
#     # 日期是否合理
#     if day > 31 and month in [1, 3, 5, 7, 8, 10, 12]:
#         return False
#     if day > 30 and month not in [1, 3, 5, 7, 8, 10, 12]:
#         return False
#     # 年月日都没问题返回True
#     return True
# n = input()
# year = n[:4]  # 取出输入日期的年份
# md = n[4:]  # 取出输入日期的月份和日期
# flag1 = True  # 回文但不是ABAB型的控制变量
# flag2 = True  # 回文并且是ABAB型的控制变量
# if int(year) > int(md[::-1]):
#     year1 = int(year)  # 防止将本年内还有可能回文的年份跳过去 如20200101，30300101
# else:
#     year1 = int(year) + 1  # 今年已经不可能再回文了，故跳过
# for i in range(year1, 10000):
#     # 这里采用改变年份，而不是改用月份或者日期，前者一次循环增加一年，后者增加的很不固定了
#     year2 = str(i)
#     md1 = str(i)[::-1]
#     if judge(int(year2), int(md1[:2]), int(md1[2:])
#         if flag1 == True:
#             print(year2, md1, sep='')
#             flag1 = False  # 找到第一个输出后就将flag1设为False，以后不在输出这种回文日期
#         if year2[:2] == year2[2:] and flag2 == True:
#             print(year2, md1, sep='')
#             flag2 = False  # 找到第一个输出后就将flag2设为False，以后不在输出这种回文日期
#     if flag1 == False and flag2 == False:
#         # 两种回文日期个输出一次，结束循环
#         break

"""砝码称重"""
# n=int(input())
# a=list(map(int,input().split()))
# sum=0
# for i in a:
#     sum+=i
# dp=[[0]*2*sum for i in range(n+1)]
# result=0
# for p in range(1,n+1):
#     for q in range(1,sum+1):
#         dp[p][q]=dp[p-1][q]
#         if dp[p][q] == 0:
#             if a[p-1]==q:
#                     dp[p][q]=1
#             if dp[p-1][a[p-1]+q]:
#                     dp[p][q]=1
#                     print(p,q)
#             if dp[p-1][abs(a[p-1]-q)]:
#                     dp[p][q]=1
# for i in dp[n]:
#     if i==1:
#         result+=1
# print(result)
