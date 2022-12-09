# a=input().split()
#del 方式删除
# a.__delitem__(0)
# print(a)

#pop方式删除
# a.pop(0)
# print(a)

#remove 方式删除
# a.remove('asd')#只删除了第一个
# print(a)

a=input().split()
b=input()
a.remove(b)
print(a)