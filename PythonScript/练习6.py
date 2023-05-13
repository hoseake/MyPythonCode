"""基本统计值计算"""
# def getNum():
#     num1 = input().replace(" ","").split(",")
#     return num1
# # 获取用户不定长度的输入
# def mean(numbers):  # 计算平均值
#     sum = 0.0
#     for i in numbers:
#         #i.replace(" ","")
#         sum += float(i)
#     return sum/len(numbers)
# def dev(numbers, mean):  # 计算标准差
#     sdev = 0.0
#     for num in numbers:
#         #num.replace(" ","")
#         sdev = sdev + (float(num) - mean) ** 2
#     return pow(sdev / (len(numbers) - 1), 0.5)
# def median(numbers):# 计算中位数
#     # numbers1 = []
#     # for n in numbers:
#     #     n.replace(" ","")
#     #     numbers1.append(n)
#     numbers.sort()
#     # print(numbers)
#     if(len(numbers)%2 == 0):
#         avg = float(numbers[int(len(numbers)/2-1)])+ float(numbers[int(len(numbers)/2)])
#         return avg / 2
#     else:
#         return eval(numbers[int(len(numbers)/2)])
# n = getNum()  # 主体函数
# m = mean(n)
# o = median(n)
# p = dev(n,m)
# print("平均值:{:.2f},标准差:{:.2f},中位数:{}".format(m,p,o))
"""集合去重"""
# s = '''双儿 洪七公 赵敏 赵敏 逍遥子 鳌拜 殷天正 金轮法王 乔峰 杨过 洪七公 郭靖
#        杨逍 鳌拜 殷天正 段誉 杨逍 慕容复 阿紫 慕容复 郭芙 乔峰 令狐冲 郭芙
#        金轮法王 小龙女 杨过 慕容复 梅超风 李莫愁 洪七公 张无忌 梅超风 杨逍
#        鳌拜 岳不群 黄药师 黄蓉 段誉 金轮法王 忽必烈 忽必烈 张三丰 乔峰 乔峰
#        阿紫 乔峰 金轮法王 袁冠南 张无忌 郭襄 黄蓉 李莫愁 赵敏 赵敏 郭芙 张三丰
#        乔峰 赵敏 梅超风 双儿 鳌拜 陈家洛 袁冠南 郭芙 郭芙 杨逍 赵敏 金轮法王
#        忽必烈 慕容复 张三丰 杨逍 令狐冲 黄药师 袁冠南 杨逍 完颜洪烈 殷天正
#        李莫愁 阿紫 逍遥子 乔峰 逍遥子 完颜洪烈 郭芙 杨逍 张无忌 杨过 慕容复
#        逍遥子 虚竹 双儿 乔峰 郭芙 黄蓉 李莫愁 陈家洛 杨过 忽必烈 鳌拜 王语嫣
#        洪七公 韦小宝 阿朱 梅超风 段誉 岳灵珊 完颜洪烈 乔峰 段誉 杨过 杨过 慕容复
#        黄蓉 杨过 阿紫 杨逍 张三丰 张三丰 赵敏 张三丰 杨逍 黄蓉 金轮法王 郭襄
#        张三丰 令狐冲 郭芙 韦小宝 黄药师 阿紫 韦小宝 金轮法王 杨逍 令狐冲 阿紫
#        洪七公 袁冠南 双儿 郭靖 鳌拜 谢逊 阿紫 郭襄 梅超风 张无忌 段誉 忽必烈
#        完颜洪烈 双儿 逍遥子 谢逊 完颜洪烈 殷天正 金轮法王 张三丰 双儿 郭襄 阿朱
#        郭襄 双儿 李莫愁 郭襄 忽必烈 金轮法王 张无忌 鳌拜 忽必烈 郭襄 令狐冲
#        谢逊 梅超风 殷天正 段誉 袁冠南 张三丰 王语嫣 阿紫 谢逊 杨过 郭靖 黄蓉
#        双儿 灭绝师太 段誉 张无忌 陈家洛 黄蓉 鳌拜 黄药师 逍遥子 忽必烈 赵敏
#        逍遥子 完颜洪烈 金轮法王 双儿 鳌拜 洪七公 郭芙 郭襄'''
# ls = s.split()
# ss = set(ls)
# print(len(ss))

"""字符串中出现最多的3个单词的统计"""
# str1 = '''I am John and I am 20, and I live in Chengdu.I knew you from my friend Tom.
# Tom is fond of traveling around the world.He said you help him last year.
# I heard a lot of things about you from him. I want to meet you and Tom.Tom agreed this.
# How about you? '''
# str1 = str1.replace("."," ")
# str1 = str1.replace("?"," ")
# str1 = str1.replace(","," ")
# list1 = str1.split()
# dic1 = {}
# for word in list1:
#     dic1[word] = dic1.get(word,0)+1
# list2 = list(dic1.items())
# list2.sort(key=lambda x:x[1],reverse=True)
# for i in range(3):
#     print(f"{list2[i][0]}:{list2[i][1]}")
"""查电话号码"""
# dic1 = {"mayun":"13309283335",
#     "zhaolong":"18989227822",
#     "zhangmin":"13382398921",
#     "Gorge":"19833824743",
#     "Jordan":"18807317878",
#     "Curry":"15093488129",
#     "Wade":"19282937665"
# }
# name = input()
# if(name not in dic1):
#     print("not found")
# print(dic1[name])
# """人名最多数统计"""
# s = '''双儿 洪七公 赵敏 赵敏 逍遥子 鳌拜 殷天正 金轮法王 乔峰 杨过 洪七公 郭靖
#        杨逍 鳌拜 殷天正 段誉 杨逍 慕容复 阿紫 慕容复 郭芙 乔峰 令狐冲 郭芙
#        金轮法王 小龙女 杨过 慕容复 梅超风 李莫愁 洪七公 张无忌 梅超风 杨逍
#        鳌拜 岳不群 黄药师 黄蓉 段誉 金轮法王 忽必烈 忽必烈 张三丰 乔峰 乔峰
#        阿紫 乔峰 金轮法王 袁冠南 张无忌 郭襄 黄蓉 李莫愁 赵敏 赵敏 郭芙 张三丰
#        乔峰 赵敏 梅超风 双儿 鳌拜 陈家洛 袁冠南 郭芙 郭芙 杨逍 赵敏 金轮法王
#        忽必烈 慕容复 张三丰 赵敏 杨逍 令狐冲 黄药师 袁冠南 杨逍 完颜洪烈 殷天正
#        李莫愁 阿紫 逍遥子 乔峰 逍遥子 完颜洪烈 郭芙 杨逍 张无忌 杨过 慕容复
#        逍遥子 虚竹 双儿 乔峰 郭芙 黄蓉 李莫愁 陈家洛 杨过 忽必烈 鳌拜 王语嫣
#        洪七公 韦小宝 阿朱 梅超风 段誉 岳灵珊 完颜洪烈 乔峰 段誉 杨过 杨过 慕容复
#        黄蓉 杨过 阿紫 杨逍 张三丰 张三丰 赵敏 张三丰 杨逍 黄蓉 金轮法王 郭襄
#        张三丰 令狐冲 赵敏 郭芙 韦小宝 黄药师 阿紫 韦小宝 金轮法王 杨逍 令狐冲 阿紫
#        洪七公 袁冠南 双儿 郭靖 鳌拜 谢逊 阿紫 郭襄 梅超风 张无忌 段誉 忽必烈
#        完颜洪烈 双儿 逍遥子 谢逊 完颜洪烈 殷天正 金轮法王 张三丰 双儿 郭襄 阿朱
#        郭襄 双儿 李莫愁 郭襄 忽必烈 金轮法王 张无忌 鳌拜 忽必烈 郭襄 令狐冲
#        谢逊 梅超风 殷天正 段誉 袁冠南 张三丰 王语嫣 阿紫 谢逊 杨过 郭靖 黄蓉
#        双儿 灭绝师太 段誉 张无忌 陈家洛 黄蓉 鳌拜 黄药师 逍遥子 忽必烈 赵敏
#        逍遥子 完颜洪烈 金轮法王 双儿 鳌拜 洪七公 郭芙 郭襄 赵敏'''
# ls = s.split()
# dic1 = {}
# for word in ls:
#     dic1[word] = dic1.get(word,0)+1
# ls1 = list(dic1.items())
# ls1.sort(key=lambda x:x[1],reverse=True)
# print(ls1[0][0])
"""数字不同数之和"""
# N = input()
# dic1 = {}
# sum1 = 0
# for word in N:
#     dic1[word] = dic1.get(word,0)+1
# for n in dic1.keys():
#     sum1 += int(n)
# print(sum1)
