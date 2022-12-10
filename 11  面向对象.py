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
# class Student():#建立student类并进行初始化与信息打印
#     def __init__(self,name,number,grade,level):
#         self.name = name
#         self.number = number
#         self.grade = grade
#         self.level = level
#         self.times = len(level.split(' '))#这个是干嘛的
#         pass
#
#     # __str__方法用于返回对象的描述信息，如果不使用__str__方法，直接print，或者return，返回的是对象的内存地址。
#     def p(self):
#         return "{}'s student number is {}, and his grade is {}. He submitted {} assignments, each with a grade of {}".format(self.name,self.number,self.grade,self.times,self.level)
#
# name = input()
# number = input()
# grade = int(input())
# level = input()
# student = Student(name, number, grade, level)
# print(student.p())

# https://zhuanlan.zhihu.com/p/30024792 类属性
# class Circle(object):  # 创建Circle类，Circle为类名
#    pass  # 此处可添加属性和方法
# 在定义 Circle 类时，可以为 Circle 类添加一个特殊的 __init__() 方法，当创建实例时，__init__() 方法被自动调用为创建的实例增加实例属性。
# class Circle(object):  # 创建Circle类
#    def __init__(self, r): # 初始化一个属性r（不要忘记self参数，他是类下面所有方法必须的参数）
#        self.r = r  # 表示给我们将要创建的实例赋予属性r赋值
# 注意：__init__() 方法的第一个参数必须是 self（self代表类的实例，可以用别的名字，但建议使用约定成俗的self），后续参数则可以自由指定，
# 和定义函数没有任何区别。
# circle1 = Circle(1)  # 创建实例时直接给定实例属性，self不算在内
# circle2 = Circle(2)
# print(circle1.r)  # 实例名.属性名 访问属性
# print(circle2.r)  # 我们调用实例属性的名称就统一了
# 注意：实例名.属性名 circle1.r 访问属性，是我们上面Circle类__init__() 方法中 self.r 的 r 这个实例属性名，
# 而不是__init__(self, r)方法中的 r 参数名，如下更加容易理解：

# class Circle(object):  # 创建Circle类
#    def __init__(self, R):  # 约定成俗这里应该使用r，它与self.r中的r同名
#        self.r = R

# circle1 = Circle(1)
# print(circle1.r)  #我们访问的是小写r
# 面试喜欢问的问题：创建类时，类方法中的self是什么？
# self 代表类的实例，是通过类创建的实例 (注意，在定义类时这个实例我们还没有创建，它表示的我们使用类时创建的那个实例)
# 实例属性每个实例各自拥有，互相独立，而类属性有且只有一份。实例属性访问优先级比类属性高，所以我们访问时优先访问实例属性，
# 它将屏蔽掉对类属性的访问。

'''NP98 修改属性1
请为牛客网的员工创建一个Employee类，包括属性有姓名（name）、（salary），并设置初始化。
同时该类包括一个方法printclass，用于输出类似'NiuNiu‘s salary is 4000, and his age is 22'的语句。
请根据输入的name与salary为该类创建实例e，并调用printclass方法输出信息，如果没有年龄信息则输出错误信息"Error! No age"。
根据输入的年龄为实例e直接添加属性age等于输入值，再次调用printclass方法输出信息。（printclass方法中建议使用try...except...结构）
输入描述：
三行分别输入姓名name、工资salary、年龄age，其中第一个为字符串，后两个为整型数字。
输出描述：
根据描述输出错误信息或是打印信息。
'''
# class Employee(object):
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#         pass
#     def printclass(self):
#         try:
#             print(f"{self.name}‘s salary is {self.salary}, and his age is {self.age}")
#             pass
#         except:
#             print("Error! No age")
# e = Employee(input(), input())#here print name and
# e.printclass()#输出printclass。检验是否报错
# e.age = input()#添加实例age
# e.printclass()

'''
NP99 修改属性2
请为牛客网的员工创建一个Employee类，包括属性有姓名（name）、（salary），并设置初始化。
同时该类包括一个方法printclass，用于输出类似'NiuNiu‘s salary is 4000, and his age is 22'的语句。
请根据输入的信息为Employee类创建一个实例e，调用hasattr方法检验实例有没有属性age，
如果存在属性age直接调用printclass输出，否则使用setattr函数为其添加属性age，并设置值为输入后，再调用printclass输出。
输入描述：
三行分别依次输入姓名name、工资salary、年龄age，其中第一行为字符串，后两行为整型数字。
输出描述：
第一行输出e有没有属性age，True或者False；
第二行输出printclass打印信息。'''

# class Employee(object):
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#         pass
#     def printclass(self):
#         print(f"{self.name}‘s salary is {self.salary}, and his age is {self.age}")
# # hasattr() 函数用于判断对象是否包含对应的属性。
# # getattr() 函数获取属性。
# # setattr() 函数用于设置属性值，若该属性不存在则创建新属性
# name=input()
# salary=input()
# age=int(input())
# e = Employee(name,salary)
# if hasattr(e,'age'):#e中是否有age，判断
#     print(True)
#     pass
# else:
#     setattr(e,'age',age)#设置属性和属性值
#     print(False)
#     pass
# e.printclass()
'''NP100 重载运算
请创建一个Coordinate类表示坐标系，属性有x和y表示横纵坐标，并为其创建初始化方法__init__。
请重载方法__str__为输出坐标'(x, y)'。
请重载方法__add__，更改Coordinate类的相加运算为横坐标与横坐标相加，纵坐标与纵坐标相加，返回结果也是Coordinate类。
现在输入两组横纵坐标x和y，请将其初始化为两个Coordinate类的实例c1和c2，并将坐标相加后输出结果。
输入描述：
第一行输入两个整数x1与y1，以空格间隔。
第二行输入两个整数x2与y2，以空格间隔。
输出描述：
输出相加后的坐标。
'''
# class Coordinate(object):
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
# #关于__str__
# # 当使用print输出对象的时候吗，默认输出内存地址
# # 如果定义了__str__方法，就会打印次用这个方法中return的数据。
# def __str__(self):
#     print(self.x,self.y)#returns a new object that represents the sum of two objects
#     pass
# def __add__(self,Coordinate1):
#     return Coordinate(self.x+Coordinate1.self.y+Coordinate1.y)
#     pass
# x1,y1=map(int,input().split())
# x2,y2=map(int,input().split())
# c1 = Coordinate(x1,y1)
# c2 = Coordinate(x2,y2)
# c3 = c1.__add__(c2)
# print(c3)


# class Coordinate():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         print((self.x, self.y))
#
#     def __add__(self):
#         self.x = x1 + x2
#         self.y = y1 + y2
#
#
# x1, y1 = map(int, input().split())  # 1.输入第一行两个数字
# x2, y2 = map(int, input().split())  # 1.输入第二行两个数字
#
# c1 = Coordinate(x1, y1)  # 2. 调用类
# c1.__add__()  # 3. 调用__add__()函数，实现两组数据分别对应相加
# c1.__str__()  # 4. 调用__str__()函数，打印(相加之后的x, 相加之后的y)


class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'({self.x}, {self.y})'
    def __add__(self,other):
        return Coordinate(self.x+other.x,self.y+other.y)


x1,y1 = list(map(int,input().split()))
x2,y2 = list(map(int,input().split()))
c1 = Coordinate(x1,y1)
c2 = Coordinate(x2,y2)
print(c1+c2)