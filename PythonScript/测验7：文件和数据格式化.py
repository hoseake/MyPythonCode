'''分数统计'''
# with open("grade2.txt","r",encoding="utf-8") as f:
#     ls1 = f.readlines()
# newList = []
# sum = 0
# for l in ls1:
#     newList.append(eval(l.strip("\n")))
# newList.sort(reverse=True)
# print(newList[0])
# newList.sort(reverse=False)
# print(newList[0])
# for n in newList:
#     sum += n
# print(round(sum/len(newList)))
'''CSV数据文件修改并多种输出操作'''
file = open("d2.csv","r",encoding="utf-8")
f = file.readlines()
joinSymbol = "\t"
newList=[]
finalList =[]
tmpList=[]
for i in f:
    if "\n" in i:
        newList.append(i.replace("\n",""))
    else:
        newList.append(i)
for l in newList:
    sum = 0
    tmpList = l.split(",")
    for n in l.split(","):
        sum += eval(n)
    tmpList.append(str(sum))
    # print(tmpList)
    finalList.append(tmpList)
# print(finalList)
for item in finalList:
    print(joinSymbol.join(item))
