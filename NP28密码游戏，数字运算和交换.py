'''牛牛和牛妹一起玩密码游戏，牛牛作为发送方会发送一个4位数的整数给牛妹，牛妹接收后将对密码进行破解。
破解方案如下：每位数字都要加上3再除以9的余数代替该位数字，然后将第1位和第3位数字交换，第2位和第4位数字交换。
请输出牛妹破解后的密码。'''

lst=[]
num=input('请输入密码:')
for i in num:
    count=(int(i)+3)%9
    lst.append(count)
    pass
#接下来是1，3交换，2，4交换
lst[0],lst[2]=lst[2],lst[0]
lst[1],lst[3]=lst[3],lst[1]
# print(lst)#到这里输出的是一个列表

for item in lst:
    print(item,end='')