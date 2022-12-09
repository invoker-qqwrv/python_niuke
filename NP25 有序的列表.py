'''创建一个依次包含字符串'P'、'y'、't'、'h'、'o'和'n'的列表my_list，
先使用sorted函数对列表my_list进行临时排序，第一行输出排序后的完整列表，
第二行输出原始的列表。再使用sort函数对列表my_list进行降序排序，第三行输出排序后完整的列表'''

lst=['p','y','t','h','o','n']
lst_sorted=sorted(lst)#临时排序，默认的升序排列吗
print(lst_sorted)
print(lst)

lst.sort(reverse=True)#这里注意大写.降序排列
print(lst)
