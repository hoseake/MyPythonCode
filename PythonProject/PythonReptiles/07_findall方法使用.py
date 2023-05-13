import re
# 1.findall方法，返回匹配的结果列表

rs = re.findall('\d+','py12thon34')
print(rs)
# 2.findall方法中，flag参数的作用
# rs = re.findall('a.bc','a\nbc') # . 号不能和换行符匹配,但可以和其他任何字符匹配
rs = re.findall('a.bc','a\nbc',re.DOTALL) # 加上DOTALL参数则可以包括换行符的所有字符匹配
print(rs)

# 3.findall方法中分组的使用
rs = re.findall('a.+bc','a\nbc',re.DOTALL)
print(rs)
rs = re.findall('a(.+)bc','a\nbc',re.DOTALL) # 只匹配括号内的表达式，括号外的表达式负责定位
print(rs)