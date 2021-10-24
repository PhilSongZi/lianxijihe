# -*- coding: utf-8 -*-
# some good instances of one line code of problems


# 1.字母词易位
from collections import Counter

s1 = 'below'
s2 = 'elbow'

print('anagram') if Counter(s1) == Counter(s2) else print('not an anagram')

# 2.进制转换：
decimal = int('1010', 2)
print(decimal)

# 3.斐波那契
fib = lambda x: x if x <= 1 else fib(x - 1) + fib(x - 2)
print(fib(20))


