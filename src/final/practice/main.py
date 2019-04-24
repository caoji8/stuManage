#coding:utf-8
from src.final.practice.msgPrint import MsgPrint
from src.final.practice.login import login
from src.final.practice.student import Student
if __name__=="__main__":
#     测试
    # printtest.studentManageMenu() 用户输入信息系统

    while True:
        print("*************欢迎使用学生成绩管理系统*************\n\
                      1、登录\n\
                      2、注册\n\
                    请输入编号进入相应菜单")
        choose_main = input(">")
        choose_main = int(choose_main)
        if choose_main == 1:
            #这里要改给 login传入的值
            student_input = input("请输入用户名,密码").split(",")
            try:
                student_input_judge = login(student_input[0],student_input[1])
            except IndexError:
                print("输入错误")
                student_input_judge = False
            if(student_input_judge):
                #实例化
                # printtest = MsgPrint(key=[{"name":"张三","no":1234567890,"major":"物联网","grade":"一年级","score":90},{"name":"张三","no":1234567890,"major":"物联网","grade":"一年级","score":90}])
                #登录通过菜单主界面页面
                printtest = MsgPrint()
                printtest.mainMenu()
        elif choose_main == 2:
            pass
        else:
            print("Error Choose")
#     基本流程
# 登陆
# 成功登陆主菜单
# 选择编号进入相应子菜单
    