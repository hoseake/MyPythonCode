"""传感器日志光照统计"""
# file = open("sensor-data-1k.txt","r")
# f = file.readlines()
# sum = 0.0
# time = 0
# for l in f:
#     list1 = l.split(" ")
#     sum += float(list1[4])
#     time += 1
# print("{:.2f}".format(sum/time))

"""古诗读入"""
# file = open("chunxiao.txt","r",encoding="utf-8")
# f = file.readlines()
# newList=[]
# for i in f:
#     if "\n" in i:
#         newList.append(i.replace("\n", ""))
#     else:
#         newList.append(i)
# print(newList[0])
# print(str(newList[1])+str(newList[2]))
# print(str(newList[3])+str(newList[4]))

"""CSV格式数据清洗"""
# file = open("data.csv","r",encoding="utf-8")
# f = file.readlines()
# newList=[]
# for i in f:
#     if " " in i:
#         newList.append(i.replace(" ",""))
#     else:
#         newList.append(i)
# for p in newList:
#     print(p.strip("\n"))

# """CSV数据文件修改操作"""
# file = open("d2.csv","r",encoding="utf-8")
# f = file.readlines()
# ss = ""
# newList=[]
# for i in f:
#     if "\n" in i:
#         newList.append(i.replace("\n",""))
#     else:
#         newList.append(i)
# for item in newList:
#     item = item + "\t"
#     ss += item.replace(",","\t")
#     ss += "\n"
# print(ss)

# #AutoTraceDraw.py
# import turtle as t
# t.title('自动轨迹绘制')
# t.setup(800, 600, 0, 0)
# t.pencolor("red")
# t.pensize(5)
# #数据读取
# datals = []
# f = open("data1.txt")
# for line in f:
#     line = line.replace("\n","")
#     datals.append(list(map(eval, line.split(","))))
# f.close()
# #自动绘制
# for i in range(len(datals)):
#     t.pencolor(datals[i][3],datals[i][4],datals[i][5])
#     t.fd(datals[i][0])
#     if datals[i][1]:
#         t.right(datals[i][2])
#     else:
#         t.left(datals[i][2])
# t.mainloop()

"""图形打印"""
# import turtle as t
# t.title("图形打印")
# t.color("blue")
# t.pensize(5)
# t.speed(1)
# file = open("图形.txt", "r")
# f = file.readlines()
# newList=[]
# for i in f:
#     if "\n" in i:
#         newList.append(i.replace("\n",""))
#     else:
#         newList.append(i)
# file.close()
# for l in newList:
#     # print(l.split(","))
#     t.right(eval(l.split(",")[0]))
#     t.forward(eval(l.split(",")[1]))
# t.hideturtle()
# t.mainloop()
