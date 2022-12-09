'''sdf
NP43 判断布尔值
输入描述：
输入0 或者 1。
输出描述：
输出"Hello World!"或者"Erros!"。
'''
# print('Hello World!' if int(input()) else 'Errors!')#输入如果是int 型，那就是hello world，不是int就输出errors

# s = int(input())
# if s:
#     print('Hello World!')
# else:
#     print('Erros!')
'''
NP44 判断列表是否为空
创建一个空列表my_list，如果列表为空，请使用print()语句一行输出字符串'my_list is empty!'，
否则使用print()语句一行输出字符串'my_list is not empty!'。'''

# my_list=[]
# my_list=input(int()).split()
# print('my_list is empty!'if len(my_list)==0 else 'my_list is not empty!')
#或者
# my_list=[]
# print('my_list is not empty!'if my_list else 'my_list is  empty!')
# if my_list代表否定

'''NP45 禁止重复注册
创建一个依次包含字符串'Niuniu'、'Niumei'、'GURR'和'LOLO'的列表current_users，
再创建一个依次包含字符串'GurR'、'Niu Ke Le'、'LoLo'和'Tuo Rui Chi'的列表new_users，
使用for循环遍历new_users，如果遍历到的新用户名在current_users中，
则使用print()语句一行输出类似字符串'The user name GurR has already been registered! Please change it and try again!'的语句，
否则使用print()语句一行输出类似字符串'Congratulations, the user name Niu Ke Le is available!'的语句。（注：用户名的比较不区分大小写）
'''
# current_users=['Niuniu','Niumei','GURR','LOLO']
# new_users=['GurR','Niu Ke Le','LoLo','Tuo Rui Chi']
# for i in new_users:
#     for j in new_users:
#         if i.upper()==j.upper():
#             print(f'The user name {i} has already been registered! Please change it and try again!')
#             break
#
#     else:
#         print(f'Congratulations, the user name {i} is available!')
# current_users=['Niuniu','Niumei','GURR','LOLO']
# new_users=['GurR','Niu Ke Le','LoLo','Tuo Rui Chi']
# #接下来就是i=gurr，然后和j里面的所有元素对比，所以会输出四次结果
# for i in new_users:
#     for j in current_users:
#         if i.upper()==j.upper():
#             print(f'The user name {i} has already been registered! Please change it and try again!')
#             pass
#
#         else:
#             print(f'Congratulations, the user name {i} is available!')
#如果if和else在相同的列。i==gurr，j=niuniu，输出else内内容，然后依次输出，知道i==j。

#下面是正确做法
#
# current_users=['Niuniu','Niumei','GURR','LOLO']
# new_users=['GurR','Niu Ke Le','LoLo','Tuo Rui Chi']
# #接下来就是i=gurr，然后和j里面的所有元素对比，所以会输出四次结果
# for i in new_users:
#     for j in current_users:
#         if i.upper()==j.upper():
#             print(f'The user name {i} has already been registered! Please change it and try again!')
#             break#到重复了就跳出程序
#
#     else:
#         print(f'Congratulations, the user name {i} is available!')
#如果取第一个i是gurr，那取到i==j的时候会break，然后从新取i。这时候i==niu ke le,i不是重复的，所以直接else输出。、
# 接下类i=lolo，能找到相同的，break。以此类推
'''NP46 菜品价格
牛客食堂今天准备了很多丰盛的午餐， 'pizza'：10块钱一份，'rice' ：2块钱一份，'yogurt'：5块钱一份，
剩下的其他菜品都是8块钱一份。牛牛在某窗口点餐，请你根据他输入的字符串，使用if-elif-else语句判断牛牛需要花费多少钱？
输入描述：
输入一个字符串表示菜品。
输出描述：
输出该菜品的价格。'''
# Cai={'pizza':10,'rice' :2,'yogurt':5,'others':8}
# x=input()
# if x not in Cai.keys():
#     x='others'
#     # print(Cai[x])
# for i in Cai.keys():
#     if i==x:
#         print(Cai[i])
#         break
'''NP47 牛牛的绩点
A 4.0
B 3.0
C 2.0
D 1.0
F 0
输入描述：
连续输入一行等级一行学分，遇到等级为False则结束输入。
输出描述：
均绩保留两位小数。
牛牛在门头沟大学学习，一学年过去了，需要根据他的成绩计算他的平均绩点，
假如绩点与等级的对应关系如下表所示。请根据输入的等级和学分数，计算牛牛的均绩
（每门课学分乘上单门课绩点，求和后对学分求均值）'''
# score=0
# xf=0
# global it
# while True:
#     x=input() # 等级
#     if x=="False":
#         break
#     else:
#         y=int(input())
#         if x=="A":
#             gpa=4.0
#         elif x=="B":
#             gpa=3.0
#         elif x=="C":
#             gpa=2.0
#         elif x=="D":
#             gpa=1.0
#         elif x=="F":
#             gpa=0
#         score=score+ gpa*y#为什么gpa not defined????
#         xf=xf+y
# print("%.2f"% (score/xf))
#while 1：表示无限循环。第一个循环时候，假如x=A，y表示牛牛成绩单中有几个这个等级。假如有一个a。
# 循环之后score=4   然后，xf=1.绩点就是 4/1=4。
# 接下来是第二轮，两个B。这时候score=4+2*3=10.  xf=1+2=3.绩点就是3.333

'''NP48
牛客网的登录系统需要验证用户名与密码，当二者都正确时才允许登录，其中管理员的用户名为'admis'，
密码为'Nowcoder666'。请你使用if-else语句，根据输入的用户名ID和密码，判断该用户等否登录。
输入描述：
第一行输入字符串表示用户名；
第二行输入字符串表示密码。
输出描述：
登录成功输出"Welcome!"，登录失败输出"user id or password is not correct!"'''
name = input()
passwd = input()
if name == 'admis' and passwd == 'Nowcoder666':
    print('Welcome!')
else:
    print('user id or password is not correct!')