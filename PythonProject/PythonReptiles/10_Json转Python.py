import json
# 1.把json字符串转化为python数据
# 1.1准备json字符串
json_str ="""[{"provinceName":"美国", "currentConfirmedCount":1179041,"confirmedCount":1643499},
  {"provinceName":"英国", "currentConfirmedCount":222227,"confirmedCount":259559}]"""
# 1.2转换
rs = json.loads(json_str)
print(rs)
print(type(rs))
print(type(rs[0]))

# 2.把json格式文件，转换为python类型的数据
# 2.1 构建指向该文件的文件对象
with open('test.json',encoding='utf-8') as fp:#上下文管理器，保证资源使用后关闭释放
    # 指定以utf-8格式打开才不会出现中文乱码
    python_list = json.load(fp)
    print(python_list)
    print(type(python_list))
    print(type(python_list[0]))
# 2.2 加载该文件对象，转化为python类型的对象
