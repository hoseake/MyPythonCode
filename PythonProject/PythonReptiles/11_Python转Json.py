import json
# 1.把python转换为json字符串
# 1.1python类型的数据
json_str ="""[{"provinceName":"美国", "currentConfirmedCount":1179041,"confirmedCount":1643499},
  {"provinceName":"英国", "currentConfirmedCount":222227,"confirmedCount":259559}]"""
rs = json.loads(json_str)
# 1.2把python转换为json字符串
json_strs = json.dumps(rs,ensure_ascii=False) #默认为ASCII码，显示中文需要改成False状态
print(json_strs)

# 2.把python以json格式存储到文件里
# 2.1构建要写入的文件对象
with open('test1.json','w') as fp:
    json.dump(rs,fp,ensure_ascii=False)
# 2.2把python以json格式存储到文件里