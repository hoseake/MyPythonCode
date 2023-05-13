"""学生类"""


class Stu:
    def __init__(self, stuID=2017001, name="博士", sex="男", Chinese=98, Math=100, English=90):  # 带默认参数
        self.stuID = stuID
        self.name = name
        self.sex = sex
        self.Chinese = Chinese
        self.Math = Math
        self.English = English

    def sum(self):
        self.sumScore = self.Chinese + self.Math + self.English
        print("{}总分为：{}".format(self.name, self.sumScore))

    def avg(self):
        self.avgScore = self.sumScore / 3.0
        print("{}平均分为：{}".format(self.name, self.avgScore))

    def pn(self):
        scoreList = []
        pnNum = 0
        scoreList.append(self.Chinese)
        scoreList.append(self.Math)
        scoreList.append(self.English)
        for s in scoreList:
            if (s >= 60):
                pnNum += 1
        print("{}及格门数为：{}".format(self.name, pnNum))


# 第一个对象
student1 = Stu(1, "张三", "男", 50, 60, 70)
student1.sum()
student1.avg()
student1.pn()
# 第二个对象
student2 = Stu()
student2.sum()
student2.avg()
student2.pn()
