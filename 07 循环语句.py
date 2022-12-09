'''NP49 字符列表的长度
创建一个依次包含字符串'P'、'y'、't'、'h'、'o'和'n'的列表my_list，
使用print()语句一行打印字符串'Here is the original list:'，再直接使用print()语句把刚刚创建的列表my_list整个打印出来，
输出一个换行，再使用print()语句一行打印字符串'The number that my_list has is:'，
再使用len()函数获取列表my_list里面有多少个字符串，并使用print()函数一行打印该整数。
输入描述：
无
输出描述：
按题目描述进行输出即可（注意前后两个输出部分需以一个空行进行分隔）。
Here is the original list:
['P', 'y', 't', 'h', 'o', 'n']'''

# my_list=['P','y','t','h','o','n']
# print('Here is the original list:')
# print(my_list)
# print("\nThe number that my_list has is:")
# print(len(my_list))
'''#NP50
牛牛、牛妹和牛可乐都是Nowcoder的忠实用户，又到了一年一度的程序员节（10月24号），毫无疑问，他们都登录Nowcoder了，因为他们还没有刷完牛客题霸...
Nowcoder的管理员想对他们发送一些简单登录问候消息，并对他们表达了节日祝福。
请创建一个依次包含字符串 'Niuniu' 、'Niumei' 和 'Niu Ke Le' 的列表users_list，
请使用for循环遍历列表user_list，依次对列表users_list中的名字输出一行类似 'Hi, Niuniu! Welcome to Nowcoder!' 的字符串，
for循环结束后，最后输出一行字符串 "Happy Programmers' Day to everyone!"
输入描述：
无
输出描述：
按题目描述进行输出即可。
Hi, Niuniu! Welcome to Nowcoder!
Hi, Niumei! Welcome to Nowcoder!
Hi, Niu Ke Le! Welcome to Nowcoder!
Happy Programmers' Day to everyone!'''
# users_list=['Niuniu','Niumei','Niu Ke Le']
# for i in users_list:
#     # print(f'Hi, {i}! Welcome to Nowcoder!' )
#     print('Hi, {}! Welcome to Nowcoder!'.format(i))
#     # print('Hi, %i! Welcome to Nowcoder!'%i)#这里需要一个数字
# print( "Happy Programmers' Day to everyone!")

'''
NP51列表的最大和最小
牛牛刚学循环语句，你能教他使用for语句创建一个从10到50的数字列表吗？请输出完整列表，并输出列表的首尾元素检验是否是从10到50.
输入描述：
无
输出描述：
第一行输出完整列表。
第二行输出列表首元素和尾元素，空格间隔。'''
# lst=[]
# for i in range(10,51):
#     lst.append(i)
#     print(lst)#如果放这里会每次循环都输出一个。可以用这个方法尝试打印九九乘法表
# # print(lst)#放这里的话就只有循环结束之后才输出

#以下是这道题实际的答案
# lst=[i for i in range(10,51)]
# print(lst)
# print(lst[0],lst[-1])
'''
NP52累加数和平均值
牛牛有一个列表，记录了他和同事们的年龄，你能用for循环遍历链表的每一个元素，将其累加求得他们年龄的总和与平均数吗？
输入描述：
一行输入多个整数，以空格间隔。
输出描述：
输出年龄总和与平均数，平均数保留1位小数，两个数字以空格间隔。'''

# a=input().split()
# sum=0
#
# for i in a:
#     sum+=int(i)#保持一致的数据结构
#     pass
# print(f'{sum},{sum/len(a):.1f}')
# # print(f"{sum1} {sum1/len(Age_List):.1f}")
# print(s,'%.1f'%(s/len(a)))

'''
NP53 前十个偶数
通过给函数 range()指定第三个参数来创建一个列表my_list，其中包含 [0, 19]  
中的所有偶数；再使用一个 for 循环将这些数字都打印出来（每个数字独占一行）。'''
# my_list=[i for i in range(20) if i%2==0]
# for i in my_list:
#     print(i)

# 解法2：用步长的方法，更简单
# my_list=[i for i in range(0,20,2)]
# for i in my_list:
#     print(i)

'''
NP54被5 整除的数字
创建一个列表my_list，其中包括 [1, 50] 内全部能被5整除的数字；
再使用一个 for 循环将这个列表中的数字都打印出来（每个数字独占一行）。'''

# my_list=[i for i in range(1,51)]
# for i in my_list:
#     if i%5==0:
#         print(i)

'''NP55 2的n次方
在Python中， * 代表乘法运算， ** 代表次方运算。
请创建一个空列表my_list，使用for循环、range()函数和append()函数令列表
my_list包含底数2的 [1, 10] 次方，再使用一个 for 循环将这些次方数都打印出来（每个数字独占一行）。
'''
# my_list=[]
# for i in range(1,11):
#     my_list.append(2**i)
#     pass
# for j in my_list:
#     print(j)

'''NP 56 列表解析
Python支持的解析操作，可以根据某些元素创建列表。请你使用列表解析创建一个0-9的列表，并输出该列表'''
# lst=[i for i in range(0,10)]
# print(lst)
'''Np 57 格式化清单
牛妹有一个暑期想吃的东西的清单，你可以把它视作一个Python的list，
['apple', 'ice cream', 'watermelon', 'chips', 'hotdogs', 'hotpot']。
牛妹决定从清单最后一种食物开始往前吃，每次吃掉一种食物就把它从list中pop掉，请使用while循环依次打印牛妹每次吃掉一种食物后剩余的清单。
输入描述：
无
输出描述：
每次去除列表末尾元素后，打印整个列表，直到列表为空，每个列表之间换行。
最初的列表不打印，空列表要打印。'''
# lst=['apple', 'ice cream', 'watermelon', 'chips', 'hotdogs', 'hotpot']
# while len(lst)!=0:
#     lst.pop(-1)
#     print(lst)

#或者
# lst=['apple', 'ice cream', 'watermelon', 'chips', 'hotdogs', 'hotpot']
# while lst:
#     lst.pop(-1)
#     print(lst)
'''
NP58 找到HR
创建一个依次包含字符串'Niuniu'、'Niumei'、'HR'、'Niu Ke Le'、'GURR' 和 'LOLO' 的列表users_list，
使用for循环遍历users_list，如果遍历到的用户名是 'HR' ，则使用print()语句一行打印字符串
 'Hi, HR! Would you like to hire someone?'，否则使用print()语句一行打印类似字符串 'Hi, Niuniu! Welcome to Nowcoder!' 的语句。
输入描述：
无
输出描述：
按题目描述进行输出即可。
Hi, Niuniu! Welcome to Nowcoder!
Hi, Niumei! Welcome to Nowcoder!
Hi, HR! Would you like to hire someone?
Hi, Niu Ke Le! Welcome to Nowcoder!
Hi, GURR! Welcome to Nowcoder!
Hi, LOLO! Welcome to Nowcoder!'''
# users_list=['Niuniu','Niumei','HR','Niu Ke Le','GURR','LOLO' ]
# for i in users_list:
#     if i=='HR':
#         print('Hi, HR! Would you like to hire someone?')
#         pass
#     else:
#         print('Hi, {}! Welcome to Nowcoder!'.format(i))

'''NP59 提前结束的循环
牛牛在牛客网举行抽奖游戏，他准备了一个列表的元素[3, 45, 9, 8, 12, 89, 103, 42, 54, 79]，
打算依次输出这些元素。他让牛妹随便猜一个数字x，在输出的时候如果输出的元素等于牛妹猜的x，就不再继续输出。
请你使用Python的for循环模拟这个输出过程，并根据输入的x使用break语句提前结束循环。
输入描述：
输入整数x表示牛妹猜的数字。
输出描述：
输出到x的前一个数字，x不用输出，每个数字单独成行。'''
# x=input()
# lst=[3, 45, 9, 8, 12, 89, 103, 42, 54, 79]
# # i=0 #这里好像不用写i=0但是还是从0开始。
# for i in lst:
#     if int(x)==i:
#         break
#     else:
#         print(i)

'''
NP 60跳过列表的某个元素
牛客网在玩数数字游戏，员工一致认为13是一个“不详的数字”，请你使用for循环帮他们从1数到15，并使用continue语句跳过13。
输入描述：
无
输出描述：
输出数字1-15，跳过13，数字之间用空格间隔。'''

# for i in range(16):
#     if i==13:
#         continue#表示继续遍历，但是不会记录
#     print(i,end=' ')

'''NP 61 矩阵相加
牛牛正在做矩阵运算，他知道n个矩阵相加，就是将矩阵中每个位置的元素都乘上n。
现有矩阵[1,2,3 4,5,6 7,8,9]
请使用list记录该矩阵，对于牛牛输入的数字n，输出n个该矩阵相加的结果。
输入描述：
输入整数n，0<n<10
输出描述：
输出n个矩阵相加的结果，直接以二维列表的形式输出。
'''

# n=int(input())
# print([[x*n for x in i] for i in [[1,2,3],[4,5,6],[7,8,9]]])#这里最外围还有一个中括号把所有的都框起来了，这样表示矩阵运算吗
