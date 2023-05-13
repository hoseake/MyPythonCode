import os
file = open("C:\\Users\\86177\\Desktop\\在校生名单.txt",encoding="UTF-8") # 避免转义
stuList = file.readlines()
countFirstName = {}
for count in stuList:
    stuName = count.replace(count[0:11],'').strip()
    stuFirstName = stuName[0]
    # 判断结果写入字典
    if stuFirstName not in countFirstName:
        countFirstName[stuFirstName] = 1
    else:
        countFirstName[stuFirstName] += 1
# print(countFirstName)
# for disFirstName in countFirstName:
#     print(f"姓 {disFirstName} 的人有 {countFirstName[disFirstName]} 个")
disFirstNameBySort = sorted(countFirstName.items(),key=lambda x:x[1],reverse=True) # 排序
print("姓氏按人数降序排列")
for disFirstName in disFirstNameBySort:
    print(f"姓 {disFirstName[0]} 的人有 {disFirstName[1]} 个")
print("姓氏按人数降序排列")
print(f"出现最多的姓氏是 {disFirstNameBySort[0][0]} , 共有 {disFirstNameBySort[0][1]} 人")
file.close()