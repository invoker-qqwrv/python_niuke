# 某公司在面试结束后，创建了一个依次包含字符串 'Allen' 和 'Tom' 的列表offer_list，作为通过面试的名单。
# 请你依次对列表中的名字发送类似 'Allen, you have passed our interview and will soon become a member of our company.' 的句子。
# 但由于Tom有了其他的选择，没有确认这个offer，HR选择了正好能够确认这个offer的Andy，所以请把列表offer_list中 'Tom' 的名字换成 'Andy' ，
# 再依次发送类似 'Andy, welcome to join us!' 的句子。


#题目的要求是输出两次
offer_list=['Allen','Tom']
for i in range(len(offer_list)):#range 这里用于遍历
    print('{},you have past our interview and soon became a member of our country'.format(offer_list[i]))
for j in offer_list:
    if j=='Tom':
        print('Andy, welcome to join us!')
    else:
        print('{},welcome to join us'.format(j))
