"""寻找名字中有'国庆'的人"""
import os
from fnmatch import fnmatch
file = open("C:\\Users\\86177\\Desktop\\在校生名单.txt",encoding="UTF-8") # 避免转义
stuList = file.readlines()
countFirstName = {}
for count in stuList:
    stuName = count.replace(count[0:11],'').strip()
    if(fnmatch(stuName,'*国庆*')):
        print(stuName)
file.close()

# import os
# i = 1
# while (i<=1000):
#     os.makedirs("C:\\Users\\86177\\Desktop\\学生文件夹2\\"+str(i))
#     i+=1

# for i in range(1,10001):
#     if(i%3 == 0 and i%5 != 0):
#         print(i,end=";")

