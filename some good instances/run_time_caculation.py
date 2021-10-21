from timeit import timeit, repeat


# 看执行1000000次x=1的时间：
print(timeit('x=1'))

# 看x=1的执行时间，执行1次(number可以省略，默认值为1000000)：
print(timeit('x=1', number=1))

# 看一个列表生成器的执行时间,执行1次：
print(timeit('[i for i in range(10000)]', number=1))

# 看一个列表生成器的执行时间,执行10000次：
print(timeit('[i for i in range(100) if i%2==0]', number=10000))


# 测试一个函数的执行时间
def func():
    s = 0
    for i in range(1000):
        s += i
    # print(s)


# timeit(函数名_字符串，运行环境_字符串，number=运行次数)
t = timeit('func()', 'from __main__ import func', number=1000)
t1 = repeat('func()', 'from __main__ import func', number=100, repeat=5)
print(t)
print(t1)
print(min(t1))

# 由于电脑永远都有其他程序也在占用着资源，你的程序不可能最高效的执行。所以一般都会进行多次试验，取最少的执行时间为真正的执行时间。
# repeat和timeit用法相似，多了一个repeat参数，表示重复测试的次数(可以不写，默认值为3.)，返回值为一个时间的列表
