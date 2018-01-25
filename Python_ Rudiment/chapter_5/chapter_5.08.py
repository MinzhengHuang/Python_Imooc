# coding=utf-8
# Python之 多重循环

# 在循环内部，还可以嵌套循环，我们来看一个例子：
for x in ['A', 'B', 'C']:
    for y in ['1', '2', '3']:
        print x + y

# x 每循环一次，y 就会循环 3 次，这样，我们可以打印出一个全排列：
#
# A1
# A2
# A3
# B1
# B2
# B3
# C1
# C2
# C3

# 任务
# 对100以内的两位数，请使用一个两重循环打印出所有十位数数字比个位数数字小的数，例如，23（2 < 3）。
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    for y in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        if x < y:
            print x * 10 + y
