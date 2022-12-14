'''
NP101 正则查找网址
牛牛最近正在研究网址，他发现好像很多网址的开头都是'https://www'，
他想知道任意一个网址都是这样开头吗。于是牛牛向你输入一个网址（字符串形式），
你能使用正则函数re.match在起始位置帮他匹配一下有多少位是相同的吗？（区分大小写）
输入描述：
输入一行字符串表示网址。
输出描述：
输出网址从开头匹配到第一位不匹配的范围。
示例1
'''
# import re
# a=input()
# result=re.match("https://www",a,re.I)
# print(type(result))
# print(result.span())#返回匹配值的下标。多少位到多少位是相同的
# print(result.group())#这里要print一下
#re.match 从字符串起始位置匹配一个规则，成功就返回match对象。否则返回none。可以用group获取匹配成功的字符串
#re.match() 语法: re.match(pattern,string,[flags])
# 参数说明：
# pattern: 模式字符串   string:要匹配的字符串   flags:可选参数,比如re.I（大写的 i ） 不区分大小写。这里也可以是空的
#最后可以用group方法获取匹配的字符串


'''NP102 提取数字电话'
牛牛翻看以前记录朋友信息的电话薄，电话号码几位数字之间使用-间隔，
后面还接了一下不太清楚什么意思的英文字母，你能使用正则匹配re.sub将除了数字以外的其他字符去掉，提取一个全数字电话号码吗？
输入描述：
输入一行字符串，字符包括数字、大小写字母和-
输出描述：
输出该字符串提取后的全数字信息。
'''
# import re
# str1=input()
# str2=re.sub('\D','',str1)
# #\D:非数字，  re.sub为替换，这句意思是把非数字替换为无，这样就只剩下纯数字
# str2=(''.join(re.findall('\d+',str1)))
# #\d:纯数字， 把所有数字找出来然后合并到一起
# print(str2)
'''NP103 截断电话号码
牛牛记录电话号码时，习惯间隔几位就加一个-间隔，方便记忆，
同时他还会在电话后面接多条#引导的注释信息。拨打电话时，-可以被手机正常识别，
#引导的注释信息就必须要去掉了，你能使用正则匹配re.match将前面的数字及-信息提取出来吗，去掉后面的注释信息。
输入描述：
输入一行字符串，包括数字、大小写字母、#、-及空格。
输出描述：
输出提取的仅包含数字和-的电话号码
'''
import re
s = input()
r = re.match('[0-9-]+',s)
print(r.group())