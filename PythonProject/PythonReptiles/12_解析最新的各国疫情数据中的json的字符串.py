import requests
from bs4 import BeautifulSoup
import re
import json
response = requests.get('https://ncov.dxy.cn/ncovh5/view/pneumonia')
home_page = response.content.decode()
# print(home_page)
soup = BeautifulSoup(home_page,'lxml')
script = soup.find(id='getListByCountryTypeService2true')
text = script.text
# print(text)

json_str = re.findall(r'\[.+\]',text)[0]# 中括号有特殊含义，要匹配字符串时要先转义
# findall方法默认返回的是一个列表,在函数后面加上[0]就变成了标准的json字符串
# print(json_str)
lastDay_CoronaVirus = json.loads(json_str)
print(lastDay_CoronaVirus)