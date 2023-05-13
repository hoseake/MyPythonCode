import requests
response = requests.get('https://baidu.com/robots.txt')#发送get请求
print(response.content.decode())