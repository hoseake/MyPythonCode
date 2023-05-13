"""2021,11,17"""
#---------------------------文件操作
#---------打开文件
# open(name,mode)   name为文件名（可包含路径）   mode为打开文件模式--只读，写入，追加
# f = open('text.txt','r')   #打开文件
# f.write('HuangKe123')      #写文件
# print(f.read())            #读文件
# f.close()                  #关闭文件
#---------访问模式特点
"""目标
1.访问模式对文件的影响
2.访问模式对write()的影响
3.访问模式是否可以省略
"""
#只读r
# f = open('text.txt','r')#文件不存在会报错
# f.write(BUG)
# f.close()

#写入w
# f = open('1.txt','w')   #若文件不存在会新建一个文件
# f.write('BUG')          #如果执行写入，会覆盖原有内容
# f.close()

#追加a
# f = open('2.txt','a')   #若文件不存在会新建一个文件
# f.write('Python')
# f.close()               #在原有内容基础上追加

# f = open('1.txt')       #访问模式可以省略，若省略表示访问模式为只读r
# f.close()
#---------读取函数read(num) num表示读取数据的长度（字节）
# f = open('text.txt','r')
# print(f.read())           #read里不写参数表示读取所有
# f.close()
#---------readlines() 按行读取数据
# f = open('text.txt','r')
# print(f.readlines())
# f.close()
#---------seek(偏移量,起始位置)函数用来移动文件指针 0开头 1当前 2结尾
f = open('text.txt','a+')
#f.seek(2,0)  #改变读取位置
f.seek(0,0)
print(f.read())