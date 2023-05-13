# 1.导入模块
from bs4 import BeautifulSoup
# 2.准备文本文档
html = """<html>
     <head>
            <title>The Dormouse's story</title>
     </head>
     <body>
            <p class="title">
                 <b>The Dormouse's story</b>
            </p>
             <p class="story">Once upon a time there were three little sisters; and their names were
                    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
                    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>and
                     <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
                     and they lived at the bottom of a well.
              </p>
               <p class="story">...</p>
"""
# 3.创建BeautifulSoup对象
soup = BeautifulSoup(html,'lxml')
# 4.查找title标签
title = soup.find('title')
print(title)
# 5.查找a标签
a = soup.find('a')
print(a)
#------------------------查找所有的a标签
all_a = soup.find_all('a')
print(a)


# -----------------------根据属性查找
#方式1：通过命名参数进行指定
id_link1 = soup.find(id='link1')
print(id_link1)
#方式2：使用attrs来指定属性字典，进行查找
attrs = soup.find(attrs={'id':'link1'})
print(attrs)
# -----------------------根据文本内容进行查找
text = soup.find(text='Elsie')
print(text)

#Tag对象
print(type(a))
print(type(id_link1))
print(type(attrs))
print(type(text))
print('标签名',a.name)
print('标签所有属性',a.attrs)
print('标签文本内容',a.text)
