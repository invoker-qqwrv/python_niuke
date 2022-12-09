'''牛牛有一个name = ['Niumei', 'YOLO', 'Niu Ke Le', 'Mona'] 记录了他最好的朋友们的名字，请创建一个二维列表friends，
使用append函数将name添加到friends的第一行。
假如Niumei最喜欢吃pizza，最喜欢数字3，YOLO最喜欢吃fish， 最喜欢数字6，Niu Ke Le最喜欢吃potato，
最喜欢数字0，Mona最喜欢吃beef，最喜欢数字3。
请再次创建一个列表food依次记录朋友们最喜欢吃的食物，并将创建好的列表使用append函数添加到friends的第二行；
然后再创建一个列表number依次记录朋友们最喜欢的颜色，并将创建好的列表使用append函数添加到friends的第三行。
这样friends就是一个二维list，使用print函数直接打印这个二维list。'''

#
friends=[]
name = ['Niumei', 'YOLO', 'Niu Ke Le', 'Mona']
food = ['pizza','fish','potato','beef']
num=['3','6','0','3']
for i in name,food,num:
    friends.append(i)
    pass
print(friends)


#或者之下的代码
# name = ['Niumei', 'YOLO', 'Niu Ke Le', 'Mona']
# food = ['pizza', 'fish', 'potato', 'beef']
# number = [3, 6, 0, 3]
# friend = [name, food, number]
# print(friend)