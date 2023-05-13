import re
# 1.不使用r原串的时候，遇到转义字符怎么做
rs = re.findall('a\nbc','a\nbc')
print(rs)
rs = re.findall('a\\\\nbc','a\\nbc') # 匹配转义字符是
print(rs)

# r原串在正则中可以消除转义字符的影响
rs = re.findall(r'a\\nbc','a\\nbc') # 加入r原串参数
print(rs)

# 扩展 ：可以解决写正则的时候，不符合PEP 8规范问题
rs = re.findall(r'\d','a123') #如果不添加r原串参数，则会抛出不符合PEP 8规范警告
print(rs)