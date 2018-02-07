# coding=utf-8


# python之导入模块

# 要使用一个模块，我们必须首先导入该模块。Python使用import语句导入一个模块。例如，导入系统自带的模块 math：
# import math

# 你可以认为math就是一个指向已导入模块的变量，通过该变量，我们可以访问math模块中所定义的所有公开的函数、变量和类：
# >>> math.pow(2, 0.5) # pow是函数
# 1.4142135623730951
#
# >>> math.pi # pi是变量
# 3.141592653589793

# 如果我们只希望导入用到的math模块的某几个函数，而不是所有函数，可以用下面的语句：
# from math import pow, sin, log

# 这样，可以直接引用 pow, sin, log 这3个函数，但math的其他函数没有导入进来：
# >>> pow(2, 10)
# 1024.0
# >>> sin(3.14)
# 0.0015926529164868282



# 任务
# Python的os.path模块提供了 isdir() 和 isfile()函数，请导入该模块，并调用函数判断指定的目录和文件是否存在。

# 注意:
# 1. 由于运行环境是平台服务器，所以测试的也是服务器中的文件夹和文件，该服务器上有/data/webroot/resource/python文件夹和/data/webroot/resource/python/test.txt文件，大家可以测试下。
# 2. 当然，大家可以在本机上测试是否存在相应的文件夹和文件。
import os
print os.path.isdir(r'/data/webroot/resource/python')
print "true"