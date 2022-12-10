'''NP94 函数求差
请定义一个函数cal()，该函数返回两个参数相减的差。
输入第一个数字记录在变量x中，输入第二个数字记录在变量y中，将其转换成数字后调用函数计算cal(x, y)，再交换位置计算cal(y, x)。
输入描述：
输入两个整数。
输出描述：
根据题目描述输出两个差，每个数字单独一行'''
# def cal(a,b):
#     return a-b
# x=int(input())
# y=int(input())
# print(cal(x,y))
# print(cal(y,x))

'''NP95 兔子的数量
兔子的数量以这样的方式增长：每个月的兔子数量等于它前一个月的兔子数量加它前两个月的兔子数量，
即f(n)=f(n-1)+f(n-2)。假设第1个月的兔子有2只，第2个月的兔子有3只，你能使用递归的方法求得第n个月的兔子有多少只吗？
输入描述：
输入正整数n，n<10。
输出描述：
输出第n个月的兔子数量。'''
# def f(n):
#     if n==1:
#         return 2
#     if n==2:
#         return 3
#     return f(n-1)+f(n-2)
# n=int(input())
# print(f(n))
'''NP96 球的表面积
球的表面积公式为V=4\pi r^2V=4πr 
 ，请写一个函数，输入球的半径，返回球的表面积。
 球的半径如下：[1, 2, 4, 9, 10, 13]，请输出这些半径下的表面积，π取math库的math.pi。
输入描述：
无
输出描述：
每行输出一个表面积，保留两位小数'''
# import math
# def v(r):
#     return 4*math.pi*r*r#pi*(r**2)
#
# list1=[1, 2, 4, 9, 10, 13]
# for i in list1:
#     print(round(v(i),2))

'''NP97 班级管理
牛牛的Python老师为了更好地管理班级，利用一个类Student来管理学生，
这个类包含了学生姓名（str）、学号（str）、分数（int）、每次作业等级（list[str]）等信息。
请你帮助牛牛的老师实现这样一个类，并定义构造方法实现初始化，定义打印函数实现打印学生的姓名、学号、分数、提交作业的次数、每次作业的等级。
输入描述：
第一行输入字符串表示学生姓名。
第二行输入字符串表示学生学号。
第三行输入整数表示学生得分。
第四行输入多个大写字母表示每次作业等级，用空格间隔。
输出描述：
用一句话输出学生的姓名、学号、分数、提交作业的次数、每次作业的等级，可以参考输出样例。'''
# n object oriented programming, it is known as a constructor.
# The __init__ method can be called when an object is created from
# the class, and access is required to initialize the attributes of the class
class Student():#建立student类并进行初始化与信息打印
    def __init__(self,name,number,grade,level):
        self.name = name
        self.number = number
        self.grade = grade
        self.level = level
        self.times = len(level.split(' '))#这个是干嘛的
        pass

    # __str__方法用于返回对象的描述信息，如果不使用__str__方法，直接print，或者return，返回的是对象的内存地址。
    def p(self):
        return "{}'s student number is {}, and his grade is {}. He submitted {} assignments, each with a grade of {}".format(self.name,self.number,self.grade,self.times,self.level)

name = input()
number = input()
grade = int(input())
level = input()
student = Student(name, number, grade, level)
print(student.p())