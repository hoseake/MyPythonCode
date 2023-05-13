"""2021,11,2----2021,11,4"""
"""Take 2 Hours"""
"""Students Manage System"""
"""不允许学员学号相同"""
print("------------------Welcome To Students Manage System!------------------")
print("*                             1.添加学员                               *")
print("*                             2.删除学院                               *")
print("*                             3.修改学员                               *")
print("*                             4.查询学员                               *")
print("*                             5.显示所有学员                            *")
print("*                             6.退出系统                               *")
listStu = [] #学员列表，全局变量
def addStu():
    global listStu
    dicStu = {}    #每次创一个新字典存新的学员
    newName = input("请输入姓名：")
    newId = input("请输入学号：")
    for i in listStu:
        while newId == i['学号']:
            print("学号重复！")
            newId = input("请重新输入学号：")
    newTel = input("请输入手机号：")
    dicStu['名字'] = newName
    dicStu['学号'] = newId
    dicStu['手机号'] = newTel
    listStu.append(dicStu)
def searchStu():
    global listStu
    searchName = input("请输入要查找学员的姓名：")
    for i in listStu:
        if searchName == i['名字']:
            print(i)
            return
    else:print("查无此人！")
def deleteStu():
    global listStu
    deleteName = input("请输入要删除学员的姓名：")
    for i in listStu:
        if deleteName == i['名字']:
            print(i)
            check = input("是否删除此学员？Yy or Nn")
            if check == 'Y' or 'y':
                listStu.remove(i)
                print("删除成功！")
                break
            elif check == 'N' or 'n':return
        else:
            print("查无此人！")
def modifyStu():
    global listStu
    modifyName = input("请输入要修改学员的姓名：")
    for i in listStu:
        if modifyName == i['名字']:
            print(i)
            which = input("请输入修改学员的哪条信息：1.名字 2.学号 3.手机号 4.全部信息")
            if which == '1':
                i['名字'] = input("请输入新名字：")
            elif which == '2':
                i['学号'] = input("请输入新学号：")
            elif which == '3':
                i['手机号'] = input("请输入新手机号：")
            elif which == '4':
                i['名字'] = input("请输入新名字：")
                i['学号'] = input("请输入新学号：")
                i['手机号'] = input("请输入新手机号：")
                break
            print("修改成功！")
            return
    else:
        print("查无此人！")
def printStu():
    print("姓名\t学号\t手机号")
    for i in listStu:
        print(f"{i['名字']},{i['学号']},{i['手机号']}")#格式化字符串，花括号里放表达式
while 1:
    select = input("请输入选项序号：")
    if select == '1':
        print("添加学员")
        addStu()
    elif select == '2':
        print("删除学员")
        deleteStu()
    elif select == '3':
        print("修改学员")
        modifyStu()
    elif select == '4':
        print("查询学员")
        searchStu()
    elif select == '5':
        print("显示所有学员")
        printStu()
    elif select == '6':
        print("退出系统")
        exitCheck = input("确定要退出？Yy or Nn ")
        if exitCheck == 'Y' or 'y':
            break
    else:
        print("输入有误，请重新输入！")

