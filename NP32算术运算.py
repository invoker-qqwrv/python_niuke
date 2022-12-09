'''输入描述：
分两行输入两个整数。
输出描述：
分两行输出加与减的结果。'''
#加法器
# x=int(input())
# y=int(input())
# print(x+y)
# print(x-y)
#NP33乘法与幂运算
'''输入描述：
分两行输入两个整数x与y。
输出描述：
第一行输出x * y，第二行输出xy '''
# x=int(input())
# y=int(input())
# print(x*y)
# print(x**y)

'''除法和取模运算
输入描述：
分两行输入两个整数x与y，其中y不为0.
输出描述：
第一行输出x除以y的商和余数；
第二行输出x除以y的非整除结果，保留两位小数。'''
# x=int(input())
# y=int(input())
# if y!=0:
#     a=x//y#
#     b=x%y
#     c=x/y
#     print(f'{a} {b}\n{c:.2f}')
#NP35判断是否相等
'''输入描述：
一行输入两个整数，以空格间隔。
输出描述：
直接输出比较结果（True或者False）'''
# x, y = input().split() #使用打包功能，一行输入两个整数并用空格隔开
# print(x == y)
'''
比较大小
输入描述：
一行输入两个整数，以空格间隔。
输出描述：
第一行输出第一个数字是否大于第二个数字，True 或者 False；
第二行输出第一个数字是否小于第二个数字，True 或者 False。'''
# x,y=input().split()
# print(f'{x>y}\n{x<y}')
'''
NP37输入描述：
一行输入三个正浮点数k、x、y，三个数字通过空格间隔。
输出描述：
第一行输出k是否不超过x，True或者False；
第二行输出k是否不低于y，True或者False。'''
# k,x,y=input().split()
# print(f'{float(k)<=float(x)}\n{float(k)>=float(y)}')
'''NP38逻辑运算
输入描述：
输入两个整数x和y，通过空格间隔。
输出描述：
每行分别直接输出x与y，x或y，非x，非y的值，前两个为数值，后两个为布尔值。'''
# x,y=int(input().split()) 不能直接int
# x,y=input().split()
# x=int(x)
# y=int(y)
# print(x and y,x or y,not x,not y,sep='\n')
'''输入描述：
两行输入两个字符串，其中字符仅包含大小写字母和数字。
输出描述：
第一行输出s1是否与s2相等的布尔值；
第二行输出s1.lower()是否与s2.lower()相等的布尔值。'''
# str1,str2=input().split()
# print(str1==str2)
# print(str1.lower()==str2.lower())
'''
NP40
输入描述：
第一行输入俱乐部的名单，以多个字符串的形式，字符串之间用空格间隔；
第二行输入要查询的名字name。
输出描述：
直接输出这个名字是否属于俱乐部名单的布尔值，True或者False。'''
# x=input().split()
# name=input()
# print(name in x)
'''np41
输入描述：
一行输入两个整数x、y，以空格间隔。是看x和y的位数是否相同吗
输出描述：
第一行输出x位与y；
第二行输出x位或y。'''
# x,y=map(int,input().split())
# print(x&y,x|y,sep='\n')

#先看下map函数的用法
# def func(a):
#     return len(a)
# x=map(func,('apple', 'banana', 'cherry'))#这里函数是计算len，所以输出也是计算len，如果函数是平方，那么输出也是平方
# print(x)
# #输出为一个list
# print(list(x))
'''公式计算器
输入描述：
一行输入四个整数，以空格间隔。
输出描述：
直接输出计算结果，结果一定是整数。'''
# NP 42 公式计算器
num=input().split()
x,y,z,k=map(int,num)#相当于对这几个数都进行int操作。

print((x+y)*(z-k))