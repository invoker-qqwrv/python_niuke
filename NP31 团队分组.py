'''创建一个列表group_list，其中依次包含字符串 'Tom', 'Allen', 'Jane', 'William', 'Tony'
表示这个小组成员的名字。现有三项任务需要他们去完成，根据不同任务的繁琐度和实际情况需要分别派2人、
3人、2人来完成，他们决定通过对列表分片来分配任务。
使用print()语句和切片来打印列表group_list的前两个元素表示去做第一个任务的人的名字，
再使用print()语句和切片来打印列表group_list的中间三个元素表示去做第二个任务的人的名字，
再使用print()语句和切片来打印列表group_list的后两个元素表示去做第三个任务的人的名字。'''
group_list=[ 'Tom', 'Allen', 'Jane', 'William', 'Tony' ]
#用print（f’)格式化字符串
print(f"{group_list[:2]}\n{group_list[1:4]}\n{group_list[-2:]}\n")
#tom allen
#allen jane william
#william