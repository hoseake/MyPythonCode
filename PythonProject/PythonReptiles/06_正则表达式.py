import re #导入正则表达式模块

#字符匹配
rs = re.findall('abc','abc') #第一个参数为正则表达式，第二个为要查询的字符串
rs = re.findall('a.c','abc') # . 可以匹配出换行符之外的所有字符
rs = re.findall('a\.c','a.c') #要匹配 .  就要在前面加上\
rs = re.findall('a[bc]d','abd') #abd,acd中的b c都在表达式中，所以都能匹配
print(rs)

#预定义字符集
rs = re.findall('\d','123') #只能匹配数字
rs = re.findall('\w','Az123_中文') #只能匹配大小写字母 数字 下划线 中文
print(rs)

#数量词
rs = re.findall('\d*','123') # * 表示匹配前一个字符出现0次或无数次
rs = re.findall('\d+','123') # + 表示匹配前一个字符出现1次或无数次
print(rs)