# coding=utf-8
# Python之 if-elif-else

# 有的时候，一个 if ... else ... 还不够用。比如，根据年龄的划分：
# 条件1：18岁或以上：adult
# 条件2：6岁或以上：teenager
# 条件3：6岁以下：kid

# 我们可以用一个 if age >= 18 判断是否符合条件1，如果不符合，再通过一个 if 判断 age >= 6 来判断是否符合条件2，否则，执行条件3：
# if age >= 18:
#     print 'adult'
# else:
#     if age >= 6:
#         print 'teenager'
#     else:
#         print 'kid'

# 这样写出来，我们就得到了一个两层嵌套的 if ... else ... 语句。这个逻辑没有问题，但是，如果继续增加条件，比如3岁以下是 baby：
# if age >= 18:
#     print 'adult'
# else:
#     if age >= 6:
#         print 'teenager'
#     else:
#         if age >= 3:
#             print 'kid'
#         else:
#             print 'baby'
# 这种缩进只会越来越多，代码也会越来越难看。

# 要避免嵌套结构的 if ... else ...，我们可以用 if ... 多个elif ... else ... 的结构，一次写完所有的规则：
# if age >= 18:
#     print 'adult'
# elif age >= 6:
#     print 'teenager'
# elif age >= 3:
#     print 'kid'
# else:
#     print 'baby'

# elif 意思就是 else if。这样一来，我们就写出了结构非常清晰的一系列条件判断。
# 特别注意: 这一系列条件判断会从上到下依次判断，如果某个判断为 True，执行完对应的代码块，后面的条件判断就直接忽略，不再执行了。

score = 85
if score >= 90:
    print 'excellent'
elif score >= 80:
    print 'good'
elif score >= 60:
    print 'passed'
else:
    print 'failed'
