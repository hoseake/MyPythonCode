import matplotlib.pyplot as plt

# 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
# 图标描述
labels = ['确诊病例', '疑似病例', '治愈病例', '死亡病例']
# 对应变量
values = [10, 20, 30, 40]
print(values)

# 图表题目
plt.title("上海市软件测试薪资分布", fontsize=12, pad=15)

# 各项属性
plt.tick_params(axis='both', which='major', labelsize=10)

plt.xlabel('薪资水平')  # 横轴标签
plt.ylabel('公司（个）')  # 纵轴标签

plt.bar(labels, values, width=0.5, bottom=1, color="SkyBlue")

# 在柱状图上显示具体数值，ha参数控制水平对齐方式，va控制垂直对齐方式
for x, y in enumerate(values):
    plt.text(x, y + 1, '%s' % y, ha='center', va='bottom', color='blue')

# 显示图片
plt.show()
