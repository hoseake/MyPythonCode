import requests
from bs4 import BeautifulSoup
import os
# 浏览器请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6)"
                  "AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/85.0.4183.102 Safari/537.36"
}

# 图片下载模块
def download(path,data):
    #找到对应图片的li标签
    ul = data.find(class_="slist").find_all("li") #class会和python的保留关键字class冲突，所以换成class_
    #遍历li标签
    for li in ul:
        #用bs解析
        li_data = BeautifulSoup(str(li),"html.parser")
        #图片详情页url
        page_url = "http://pic.netbian.com/" + li_data.find("a")["href"]
        #图片名称
        picTitle = li_data.find("img")["alt"]
        #发送请求
        page_data = requests.get(url=page_url,headers=headers)
        #进一步解析详情页
        response_data = BeautifulSoup(page_data.text,"html.parser")
        #拼接详情页图片url

        pic_url = "http://pic.netbian.com" + response_data.find(class_="photo-pic").find("img")["src"]
        # 通过class值定位到相应div标签，进一步定位到img标签获取src属性也就是详情图片url
        # 看了网页源码，错误地把photo-pic换成了src，所以遇到了AttributeError: 'NoneType' object has no attribute 'find'
        # 因为并没有class值为src的div标签
        pic_res = requests.get(url=pic_url,headers=headers).content #使用二进制数据
        #保存图片
        with open(path + "/" + picTitle + ".jpg","wb") as f:
            print("正在保存图片："+picTitle)
            f.write(pic_res)

if __name__ == '__main__':
    picPath = "C:\\Users\\86177\\Desktop\\Test" #文件保存路径,路径中的斜杠会引起转义功能，所以用双斜杠避免转义
    if not os.path.exists(picPath):
        os.mkdir(picPath)
    for page in range(1,4): #爬取页数
        dataPath = picPath + "/" + str(page)
        if not os.path.exists(dataPath):
            os.mkdir(dataPath)
        #设置爬取页数
        #用为第一页图片url比较特殊，所以特殊处理
        if page == 1:
            url = "https://pic.netbian.com/4kqiche/index.html"
        else:
            url = "https://pic.netbian.com/4kqiche/index_"+str(page)+".html"
        #发送请求
        response = requests.get(url=url,headers=headers)
        response.encoding = 'GBK'
        data = BeautifulSoup(response.text,"html.parser")
        download(dataPath,data)