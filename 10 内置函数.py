# jiayou
'''NP76 列表的最值运算
牛牛给了牛妹一个一串无规则的数字，牛妹将其转换成列表后，使用max和min函数快速的找到了这些数字的最值，你能用Python代码实现一下吗？
输入描述：
输入一行多个整数，数字之间以空格间隔。
输出描述：
输出这些数字的zui zhi'''

# 易错点：默认的输入是字符串类型，需要转化成整形在进行内置函数的使用
# 比如我下面就犯了这个错误
# a=input().split()
# print(max(a))
# print(min(a))

# lst=[int(i) for i in input().split()]
# print(max(lst))
# print(min(lst))
'''NP77朋友的年龄和
牛牛想知道自己小组内的同事们的年龄和都有多少，他输入一串年龄序列，请将其转换成列表，并使用sum函数直接获取列表的和。
输入描述：
一行输入多个正整数，以空格间隔。
输出描述：
输出求和'''
# lst=[int(i) for i in input().split()]
# print(sum(lst))

'''NP78 正数输出器
牛牛想要这样一个程序，只要是输入一个整数，不管正负，它一定转换为正数，即获取该数字的绝对值，你能用abs函数实现吗？
输入描述：
输入一个非零整数。
输出描述：
输出该数字的绝对值。'''
# A=int(input())
# print(abs(A))# 区分大小写
'''NP79 字母转数字
牛牛刚学习了ASCII码，他知道计算机中的字母很多用的都是这个编码方式，现在输入一个字母，你能使用ord函数将其转换为ASCII码对应的数字吗？
输入描述：
输入一个字符，仅包含大小写字母。
输出描述：
输出该字母在ASCII中对应的数字。'''

# print(ord(input()))

'''NP80 数字的十六进制
描述
牛妹刚学习进制转换，对这方面掌控还不太熟练，她想请你帮她写一个十进制到十六进制的进制转换器，你能使用hex函数帮助她完成这个任务吗？
输入描述：
输入一个正整数。
输出描述：
输出该正整数的十六进制'''
# 知识点
# 2进制bin；八进制oct；十进制int；十六进制hex
# 把其他进制转换为十进制的方法int(要转换的数字，16)--表示把要转换的16进制转化为十进制；因为int无法直接将带字母的进制进行转化
# num_int = int(input())
# print(hex(num_int))

'''
NP81 数字的二进制表示
计算机内部都由二进制组成，但是早就习惯使用十进制的牛牛根本不知道这个数字的二进制是什么，你能使用bin函数帮助他将十进制数字转换成二进制吗？
输入描述：
输入一个十进制正整数。
输出描述：
输出该数字的二进制形式。'''
# num_int = int(input())
# print(bin(num_int))
'''NP 82数学幂运算
描述
在Python中，除了使用两个乘号相连外，还能使用pow函数表示幂运算。
现牛牛输入正整数x与y，请你使用两种方法分别计算xy与yx。
输入描述：
一行输入两个正整数，以空格间隔。
输出描述：
分别两行输出计算xy与yx'''
# 一下两种方法都行
# x,y=[int(i) for i in input().split()]
# # x,y = list(map(int,input().split()))
# print(pow(x,y))
# print(pow(y,x))
'''
NP83 错误出现的次数
在牛客网内部使用1标记正确回答的题，使用0表示回答错误的题。牛牛拿到自己的作答记录是一串01序列，
他想知道自己一共答错了多少次，你能将这串序列转换为列表，使用count函数帮助牛牛统计一下吗？
输入描述：
输入一行数组序列，数字只包含0和1，以空格间隔。
输出描述：
输出0出现的次数。
'''
# list=input().split(' ')
# list=input().split()#好像没区别
#
# print(list.count('0'))

'''NP84 列表中第一次出现的位置
描述
牛客网有一个打卡系统，记录了每个人这一个星期上班打卡的记录（以名字的形式）。
牛牛想知道自己在这一个星期是第几个打卡的人，你用将这份名字记录转换为列表，然后使用index函数找到'NiuNiu'的位置吗？
输入描述：
输入一行字符串表示打卡人的姓名，以空格间隔，字符串中必定有'NiuNiu'。
输出描述：
输出'NiuNiu'第一次打卡是第几个，从0开始计数。
'''
# list=input().split()
# for i in list:
#     if i=='NiuNiu':
#         print(list.index(i))
#
# list=input().split()
# print(list.index('NiuNiu'))
'''NP85 字符的类型比较
Python有内置函数isalpha、isdigit、isspace可以分别判断字符串
是否只包含字母、数字、空格，现在输入一个字符串，请分别输出这三个函数的判断结果。
输入描述：
输入一个字符串。
输出描述：
分三行依次输出上述三个函数的判断结果。
'''
# s = input()
# print(s.isalpha())
# print(s.isdigit())
# print(s.isspace())

'''NP86 字符子串的查找
牛客网公布中奖信息了，中奖信息是一个很长的字符串，牛牛想知道自己的名字
（'NiuNiu'）有没有出现在其中，你能帮助他使用字符串的find函数查找一下吗？
输入描述：
输入一个长字符串long_str表示中奖信息。
输出描述：
输出'NiuNiu'在long_str中第一次出现的位置，没有则输出-1.
'''
# long_str=input()
# print(long_str.find('NiuNiu'))

#也可以用try的方式做这个题
# long_str=input()
# try:
#     print(long_str.index('NiuNiu'))
#     pass
# except ValueError:
#     print('-1')