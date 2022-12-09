stack = [1, 2, 3, 4, 5]
a=int(input())
for i in range(3):
    if i<2:
        stack.pop(-1)
        print(stack)
        pass
    else:
        stack.append(a)
        print(stack)
        