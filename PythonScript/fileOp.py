import os
file = open("C:\\Users\\86177\\Desktop\\在校生名单.txt",encoding="UTF-8") # 避免转义
stu_list = file.readlines()
for p in stu_list:
    stu_id = p[0:11]
    stu_name = p.replace(stu_id,'').strip()
    os.makedirs("C:\\Users\\86177\\Desktop\\学生文件夹\\"+stu_id+'_'+stu_name)
file.close()
