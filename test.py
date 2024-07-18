import math
#打印
# str1="Hello World!"
# print(f"str1的内容为：{str1}")
#
# #输入
# user_name=input()
# user_type=input()
# print("你好：%s 您是尊贵的：%s" %(user_name,user_type))

# #布尔类型
# bool_1=1>2
# bool_2=2>1
# print(f"bool_1的类型为：{bool_1}"'\n'f"bool_2的类型为：{bool_2}")

#多条件判断
# num1=int(input("请输入一个数字: "))
# if num1>0:
#     print("输入大于0")
# elif num1<0:
#     print("输入小于0")
# else:
#     print("等于0")

# #列表
# shoping_list=["显示器","鼠标"]
# shoping_list.append("U盘")
# shoping_list.append("硬盘")
# print(shoping_list)
# shoping_list.remove("U盘")
# print(shoping_list)

# #字典
# contacts={"小明":"123",
#           ("张伟",23):"456",
#           ("张伟",34):"789"}
# print(contacts["小明"])
# print(contacts["张伟",23])

# # Fot循环
# temputure_list=[36.1,36.6,36.8,37,36.2,37.4,38]
# for temperture in temputure_list:
#     if temperture>37:
#         print(temperture)
#         print("完蛋")

#while循环
# sum=0
# count=0
# while (num :=input("请输入数字，按q结束:"))!='q': #:= 是海象运算符（walrus operator），它允许在表达式内部进行赋值操作。
#     try:    #try 语句块中的代码会被尝试执行。如果执行过程中发生了异常（错误），程序会跳到 except 块中执行相应的错误处理代码
#         num=float(num)
#         sum+=num
#         count+=1
#         result = sum / count
#     except ZeroDivisionError:   # 当尝试除以零时会引发 ZeroDivisionError 异常
#         print("除数不能为零")
#     except Exception as e:   # 捕获所有其他类型的异常
#         print(f"输入错误,错误类型:{e}")
# print(f'平均值为:{result:.2f}')

#函数
# def count_avg():
#     sum = 0
#     count = 0
#     while (num :=input("请输入数字，按q结束:"))!='q': #:= 是海象运算符（walrus operator），它允许在表达式内部进行赋值操作。
#         try:    #try 语句块中的代码会被尝试执行。如果执行过程中发生了异常（错误），程序会跳到 except 块中执行相应的错误处理代码
#             num=float(num)
#             sum+=num
#             count+=1
#             result = sum / count
#         except ZeroDivisionError:   # 当尝试除以零时会引发 ZeroDivisionError 异常
#             print("除数不能为零")
#         except Exception as e:   # 捕获所有其他类型的异常
#             print(f"输入错误,错误类型:{e}")
#     return result
# a=float(count_avg())
# print(f"{a:.2f}")

#面向对象的编程
class Student:
    def __init__(self,name,student_id):
        self.name=name
        self.student_id=student_id
        self.grades={"语文":0,"数学":0,"英语":0}
    def set_grade(self,course,grade):
        if course in self.grades:
            self.grades[course]=grade
    def print_grades(self):
        print(f"学生{self.name}(学号:{self.student_id})的成绩为：")
        for course in self.grades:
            print(f"{course}:{self.grades[course]}分")
chen=Student("小陈","1234")
chen.set_grade("语文",92)
chen.set_grade("数学",98)
chen.set_grade("英语",95)
chen.print_grades()



