#1.导入模块
import requests
#2.发送请求，获取响应
response = requests.get('http://www.baidu.com')
print(response)
#3.获取响应数据
# print(response.encoding)   #编码方式
# response.encoding = 'utf8'
# print(response.encoding)
# print(response.text)       #将响应数据转化成str类型
print(response.content.decode()) #content获取二进制数据，
# decode进行解码 默认utf8解码    GBK解码：decode(encoding = 'gbk')

