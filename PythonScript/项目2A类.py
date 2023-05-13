"""查询与统计"""
# with open("python23成绩10-25-2021.csv","r",encoding="utf-8") as f:
#     ls1 = f.readlines()
# stuNameorID = input()
# sum = 0.0
# stuNameInfo = []
# stuIdInfo =[]
# stuAllInfo = []
# posList = []
# def searchByName():
#     try:
#         return stuNameInfo.index(stuNameorID)
#     except:
#         # print("查无此人")
#         return None
#
# def searchById():
#     try:
#         return stuIdInfo.index(stuNameorID)
#     except:
#         print("查无此人")
#         return None
#
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
#         return numbers[int(len(numbers)/2)]
#
# for l in ls1[1:]:
#     line1 = l.strip("\n")
#     line1 = line1.replace(",x", ",-0.01")  # 未测试的标记是x，打分为-0.01
#     line1 = line1.replace(",,,,,", ",-0.02,-0.02,-0.02,-0.02,-0.02")  # 未加入课程的，打分为-0.02
#     stu1 = line1.split(",")
#     stu1[4] = str(eval(stu1[4]) / 2.0)
#     stuAllInfo.append(stu1)
#     stuIdInfo.append(stu1[0])
#     stuNameInfo.append(stu1[1])
#
# if(searchByName() != None):
#     score = list(map(lambda x: float(x), stuAllInfo[searchByName()][3:8]))
#     for s in score:
#         sum += s
#     avgScore = sum / 5.0
#
#     sdev = 0.0
#     for num in score:
#         # num.replace(" ","")
#         sdev = sdev + (float(num) - avgScore) ** 2
#     fangchaScore = pow(sdev / (len(score) - 1), 0.5)
#     mScore = median(score)
#     if (stuNameorID == "袁满"):
#         print("学号:{},五次成绩:{:.2f},{:.2f},{:.2f},{:.2f},{:.2f};平均成绩={:.2f}，方差={:.2f}，中位数={:.2f}。".format(
#             stuAllInfo[searchByName()][0],
#             eval(stuAllInfo[searchByName()][3]),
#             eval(stuAllInfo[searchByName()][4]),
#             eval(stuAllInfo[searchByName()][5]),
#             eval(stuAllInfo[searchByName()][6]),
#             eval(stuAllInfo[searchByName()][7]),
#             avgScore,
#             fangchaScore,
#             mScore))
#     else:
#         print("五次成绩:{:.2f},{:.2f},{:.2f},{:.2f},{:.2f};平均成绩={:.2f}，方差={:.2f}，中位数={:.2f}。".format(
#             eval(stuAllInfo[searchByName()][3]),
#             eval(stuAllInfo[searchByName()][4]),
#             eval(stuAllInfo[searchByName()][5]),
#             eval(stuAllInfo[searchByName()][6]),
#             eval(stuAllInfo[searchByName()][7]),
#             avgScore,
#             fangchaScore,
#             mScore))
#
#
#
#     if(stuNameorID == "袁满"):
#         sum = 0
#         score = list(map(lambda x: float(x), stuAllInfo[198][3:8]))
#         for s in score:
#             sum += s
#         avgScore = sum / 5.0
#
#         sdev = 0.0
#         for num in score:
#             # num.replace(" ","")
#             sdev = sdev + (float(num) - avgScore) ** 2
#         fangchaScore = pow(sdev / (len(score) - 1), 0.5)
#         mScore = median(score)
#         print("学号:{},五次成绩:{:.2f},{:.2f},{:.2f},{:.2f},{:.2f};平均成绩={:.2f}，方差={:.2f}，中位数={:.2f}。".format(
#             stuAllInfo[198][0],
#             eval(stuAllInfo[198][3]),
#             eval(stuAllInfo[198][4]),
#             eval(stuAllInfo[198][5]),
#             eval(stuAllInfo[198][6]),
#             eval(stuAllInfo[198][7]),
#             avgScore,
#             fangchaScore,
#             mScore))
#
# elif(searchById() != None):
#     score = list(map(lambda x: float(x), stuAllInfo[searchById()][3:8]))
#     for s in score:
#         sum += s
#     avgScore = sum/5.0
#
#     sdev = 0.0
#     for num in score:
#         # num.replace(" ","")
#         sdev = sdev + (float(num) - avgScore) ** 2
#     fangchaScore = pow(sdev / (len(score) - 1), 0.5)
#     mScore = median(score)
#
#     print("五次成绩:{:.2f},{:.2f},{:.2f},{:.2f},{:.2f};平均成绩={:.2f}，方差={:.2f}，中位数={:.2f}。".format(
#         eval(stuAllInfo[searchById()][3]),
#         eval(stuAllInfo[searchById()][4]),
#         eval(stuAllInfo[searchById()][5]),
#         eval(stuAllInfo[searchById()][6]),
#         eval(stuAllInfo[searchById()][7]),
#         avgScore,
#         fangchaScore,
#         mScore))

"""词频统计"""
# with open("python23成绩10-25-2021.csv","r",encoding="utf-8") as f:
#     ls1 = f.readlines()
# dic1 = {}
# for l in ls1[1:]:
#     line1 = l.strip("\n")
#     stu1 = line1.split(",")
#     for word in stu1[3:8]:
#         dic1[word] = dic1.get(word,0)+1
# ls1 = list(dic1.items())
# ls1.sort(key=lambda x:x[1],reverse=True)
# # print(ls1[0:5])
# for p in ls1[0:5]:
#     print("{}:{}".format(p[0],p[1]))

"""重名判断（判断学生姓名是否有重复的）"""
# with open("python23成绩10-25-2021.csv","r",encoding="utf-8") as f:
#     ls1 = f.readlines()
# dic1 = {}
# for l in ls1[1:]:
#     line1 = l.strip("\n")
#     stu1 = line1.split(",")
#     # print(stu1)
#     dic1[stu1[1]] = dic1.get(stu1[1],0)+1
# # ls1 = list(dic1.items())
# # ls1.sort(key=lambda x:x[1],reverse=True)
# name = ""
# for d in dic1:
#     if(dic1.get(d) != 1):
#         name = d
# if(name == ""):
#     print("没有重名的学生姓名")
# else:
#     print("有重名的学生姓名：")
#     print(name)

"""单次测验统计（统计一次测验的平均值、方差与中位数等）"""
from math import sqrt
with open("python23成绩10-25-2021.csv","r",encoding="utf-8") as f:
    ls1 = f.readlines()
className = input()
courseName = input()
courseList =["all"]
stuAllInfo = []
scoreListByClass = []
scoreListByClassAndCourse = []
all_0_mean_list = []
for l in ls1[1:]:
    line1 = l.strip("\n")
    line1 = line1.replace(",x", ",-0.01")  # 未测试的标记是x，打分为-0.01
    line1 = line1.replace(",,,,,", ",-0.02,-0.02,-0.02,-0.02,-0.02")  # 未加入课程的，打分为-0.02
    stu1 = line1.split(",")
    stu1[4] = str(eval(stu1[4]) / 2.0)
    stuAllInfo.append(stu1)
    courseList.append(stu1[2])

def mean(numbers):  #计算平均值
    s = 0.0
    for num in numbers:
        s = s + float(num)
    return s / len(numbers)

def dev(numbers, mean): #计算方差
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (float(num) - mean)**2
    return sqrt(sdev / (len(numbers)-1))

def median(numbers):    #计算中位数
    # numbers = sorted(numbers)
    numbers.sort(key=lambda numbers:eval(numbers)) # 原有的排序不能去除元素两边的引号
    size = len(numbers)
    if size % 2 == 0:
        med = (numbers[size//2-1] + numbers[size//2])/2
    else:
        med = numbers[size//2]
    return med

if(className not in set(courseList)):
    print("班级名错误(其中all表示所有班级)")
    exit(0) # 输入错误就退出，暴力方法
else:
    for s in stuAllInfo:
        if(className == s[2]):
            scoreListByClass.append(s[3:8])
if(className == "all"):
    for s in stuAllInfo:
            scoreListByClass.append(s[3:8])
# print(scoreListByClass)

if(eval(courseName)>=0 and eval(courseName) <= 5):
    if(eval(courseName) != 0):
        for s in scoreListByClass:
            scoreListByClassAndCourse.append(s[eval(courseName) - 1])
        # print(scoreListByClassAndCourse)
        meanNum = mean(scoreListByClassAndCourse)
        devNum = dev(scoreListByClassAndCourse, meanNum)
        medianNum = median(scoreListByClassAndCourse)
        print("{}班级的测验{}成绩的平均成绩={:.2f}，方差={:.2f}，中位数={:.2f}。".format(className,courseName,meanNum,devNum,float(medianNum)))
        # print(meanNum,devNum,medianNum)
    if(eval(courseName) == 0):
        course1 = [];course2 = [];course3 = [];course4 = [];course5 = []
        courseAvg = []
        for s in scoreListByClass:
                scoreListByClassAndCourse.append(s)
        for s1 in scoreListByClassAndCourse:
            meanNum = mean(s1)
            all_0_mean_list.append(str(meanNum))
        meanNum = mean(all_0_mean_list)
        devNum = dev(all_0_mean_list, meanNum)
        medianNum = median(all_0_mean_list)
        print("{}班级的测验{}(平均成绩)成绩的平均成绩={:.2f}，方差={:.2f}，中位数={:.2f}。".format(className,courseName,meanNum,devNum,float(medianNum)))
else:
    print("测验号错误(应该0~5,0表示所有测验的平均值)")
