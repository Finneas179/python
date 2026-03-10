student = []
print("*"*10,"学生姓名管理系统","*"*10)
#\t相当于tab键
print("1.添加学生姓名 \t2.查看所有学生姓名")
print("3.修改学生姓名 \t4.删除学生姓名")
print("5.退出系统")
print("*"*35)
while True:
    choice = input("请输入操作: ")
    if choice in ["1","添加学生姓名"] :
        print("进行操作1")
        while True:
            newname=input("请输入学生的姓名: /终止请说no :")
            if newname.lower() == "no":
                print("添加完毕")
                print(student)
                print("退出学生系统")
                break
            student.append(newname)
            print(f"{newname}已经添加到学生名单中")
    elif choice in ["2","查看所有学生姓名"]:
        print("进行操作2")
        if not student:
            print("请先添加学生")
            continue
        for i in range(0,len(student)):
            print(f"{i+1}.学生姓名: {student[i]}")
    elif choice in ["3","修改学生姓名"]:
        print("进行操作3")
        #直接student[i]=value就好
        if not student:
            print("学生名单为空，先来添加学生")
            continue
        name = input("请输入你要修改的学生姓名")
        if name not in student:
            print("不存在，请重新操作")
            continue
        index = student.index(name)
        student[index]=input("请输入修改后的名字")
    elif choice in ["4","删除学生姓名"]:
        print("进行操作4")
        #del如果你打错就会直接删除整个变量
        #pop必须知道索引
        #remove根据value值然后进行删除

    elif choice in ["5","退出系统"]:
        print("进行操作5")
    else:
        print("请重新输入")