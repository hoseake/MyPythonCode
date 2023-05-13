try:
    print("Succeess") # 人为造成错误,打印未定义的S变量
except Exception as e:
    print(e) # 打印错误信息
else:
    print("没有异常")
finally:
    print("Finally") # 最后执行
