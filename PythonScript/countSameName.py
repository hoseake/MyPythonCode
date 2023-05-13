import os
file = open("C:\\Users\\86177\\Desktop\\在校生名单.txt",encoding="UTF-8") # 避免转义
stuList = file.readlines()
# countFirstName = {}
countSameName = {}
for count in stuList:
    stuName = count.replace(count[0:11],'').strip()
    # stuFirstName = stuName[0]
    # 判断结果写入字典
    if stuName not in countSameName:
        countSameName[stuName] = 1
    else:
        countSameName[stuName] += 1
disSameNameBySort = sorted(countSameName.items(),key=lambda x:x[1],reverse=True) # 排序
# print(type(countSameName.items()))
for disSameName in disSameNameBySort:
    print(f"名字是 {disSameName[0]} 的人有 {disSameName[1]} 个")
file.close()