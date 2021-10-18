'''
重温基础内容，一步步走不好高骛远，一个个代码敲不cv。
'''


# 1.以逗号分隔打印在屏幕上：join()的使用方法
'''
n_list = []
for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        n_list.append(str(i))
print('，'.join(n_list))
'''

# 2.input()得到的输入用int转换类型;dict类型赋值
'''
n = int(input("请输入一个整数："))
d = dict()
for i in range(1, n+1):
    d[i] = i * i
print(d)
'''


# 3.编写一个可以计算给定数阶乘的程序，结果以逗号分隔，打印在一行上； 假设向程序输入8，则输出40320；
# 迭代的写法
'''
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)
x = int(input("请输入要计算阶乘的数："))
print(fact(x))
'''


# 4.编写一个程序，该程序接收控制台以逗号分隔的数字序列，并生成包含每个数字的列表和元组；
# 没有转换类型，所以列表和元组里都是字符类型的（‘’括起来的）
'''
import re
values = input("请输入一组数字："))
l = values.split(',')
pattern = re.compile(r'[0-9]+')     # 复杂re表达式建议先编译 方便复用。简单的直接写进去就行。
k = re.findall(pattern, values)
t = tuple(k)
print(k)
print(t)
'''

# 5.定义一个至少有两个方法的类: 一、getString：从控制台输入获取字符串；二、printString：打印大写字母的字符串，并写出简单的测试函数来测试类方法
# 类定义的写法。upper() lower()方法
'''
class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        print("请输入字符串：")
        self.s = input()

    def printString(self):
        print(self.s.upper())       # upper()转换字母为大写

strObj = InputOutString()
strObj.getString()
strObj.printString()
'''

# 6.编写一个程序，根据给定的公式计算并打印值:[公式]。其中，假设 C=50。H=30。D 是一个变量，它的值应该以逗号分隔的序列输入到程序中。
# 程序的输入序列为（以逗号分隔）：100，150，180； 则程序输出为：18，22，24；
# 如果输出是小数，则应四舍五入到其最近的值（例输出是 26.0，则应打印为 26)。
'''
import math
c = 50
h = 30
value = []
print("请输入一组数据：")
items = [x for x in input().split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2 * c * float(d) / h)))))
print(','.join(value))
'''

# 7.编写一个程序，X,Y 作为输入，生成一个二维数组，数组的第 i 行和第 j 列的元素值应该是 i×j。
# 注意：i= 0,1 . .,X - 1; j = 0, 1, Y-1。 假设，程序输入 3, 5；则程序输出为：[[0,0,0,0,0],[0,1,2,3,4],[0,2,4,6,8]]；
# 提示：如果要为问题提供输入数据，应该假设它是一个控制台输入，以逗号分隔。
'''
print("请输入两个数字:")
input_str = input()
dimensions = [int(x) for x in input_str.split(',')]
rowNum = dimensions[0]
colNum = dimensions[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
for row in range( rowNum):
    for col in range(colNum):
        multilist[row][col] = row * col
print(multilist)
'''


# 8.问题：编写一个程序，以逗号分隔的单词序列作为输入，按照字母顺序对每个单词进行排序，并通过逗号分隔的序列来打印单词。
# 假设向程序输入：without,hello,bag,world； 则输出为：bag,hello,without,world；
# 提示：在为问题提供输入数据的情况下，应该假设它是控制台输入。
'''
print("请输入一个单词序列，以逗号分隔单词：")
items = [x for x in input().split(',')]
items.sort()
print(','.join(items))
'''

# 9.问题：编写一个程序，接收一行序列作为输入，并在将句子中的所有字符大写后打印行。
# 假设向程序依次输入：Hello world；Practice makes perfect； 则输出为：HELLO WORLD；PRACTICE MAKES PERFECT；
# 提示：在为问题提供输入数据的情况下，应该假设它是控制台输入。
'''
lines = []
while True:
    s = input()
    if s:
        lines.append(s.upper())
    else:
        break
for sentence in lines:
    print(sentence)
'''

# 10.问题：编写一个程序，以一系列空格分隔的单词作为输入，并在删除所有重复的单词后，按字母顺序排序后打印这些单词.
# 假设向程序输入：hello world and practice makes perfect and hello world again 则输出为：again and hello makes perfect practice world
# 提示：我们使用 set 容器自动删除重复的数据，然后使用 sort () 对数据进行排序。
'''
print("请输入一组字符串：")
s = input()
words = [word for word in s.split(" ")]
print(','.join(sorted(set(words))))
'''

# 11.问题：编写一个程序，接收一系列以逗号分隔的 4 位二进制数作为输入，然后检查它们是否可被 5 整除， 可被 5 整除的数字将以逗号分隔的顺序打印。
# 例：0100,0011,1010,1001 那么输出应该是：1010
# 提示：如果输入数据被提供给问题，则应该假定它是控制台输入。
'''
value = []
print("请输入逗号分隔的4位二进制数：")
items = [x for x in input().split(',')]
for p in items:
    intp = int(p, 2)
    if not intp % 5:
        value.append(p)
print(','.join(value))
'''

# 12.问题：编写一个程序，找到 1000 到 3000 之间并且所有位数均为偶数的所有数字，比如 2000，2002 等；获得的数字都以逗号分隔的顺序，打印在一行上
# 提示：如果输入数据被提供给问题，则应该假定它是控制台输入。
# ——所有位数均为偶数，那么那一位的数必定能被2整除，问题就在提取出每一位的数以此判断。——把数转换成str，按顺序逐个读str的值，转换成int后判断整除。
'''
values = []
for i in range(2000, 3001):
    str1 = str(i)
    if (int(str1[0]) % 2 == 0) and (int(str1[1]) % 2 == 0) and (int(str1[2]) % 2 == 0) and(int(str1[3]) % 2 == 0):
        values.append(str1)
print(','.join(values))
'''

# 13.问题：编写一个接受句子并计算字母和数字的程序。 假设程序输入：Hello world! 123 则输出应该是：字母 10 数字 3
# 提示：如果输入数据被提供给问题，则应该假定它是控制台输入。
'''
string1 = input("请输入：")
dict1 = {'numbers': 0, 'letters': 0}
for count in string1:
    if count.isdigit():
        dict1['numbers'] += 1
    elif count.isalpha():
        dict1['letters'] += 1
    else:
        pass
print('字母：', dict1['letters'])
print('数字', dict1['numbers'])
'''

# 14.问题：编写一个接收句子的程序，并计算大写字母和小写字母的数量。
# 假设为程序提供了以下输入：Hello world! 则输出应该是：UPPER CASE 1；LOWER CASE 9
# 提示：如果输入数据被提供给问题，则应该假定它是控制台输入。
''' print("跟上一题一毛一样！区别在于函数是判断大小写的：isupper()和islower()")  '''

# 15.问题：编写一个程序，计算 a + aa + aaa + aaaa 的值，给定的数字作为 a 的值。 假设为程序提供了以下输入：9；输出应该是：11106
# 提示：如果输入数据被提供给问题，则应该假定它是控制台输入。
# 我的思路：两次类型转换——int转str得到aaaa的形式，str转int求和
'''
a = input("请输入一个数字：")
value = 0
a_str_list = []
a_num_list =[]
for i in range(1, 5):
    a_str_list.append(str(a) * i)
    a_num_list.append(int(a_str_list[i - 1]))
    value += a_num_list[i - 1]
print(value)
'''

# 16.问题：使用列表推导输出列表中的每个奇数，该列表由一系列逗号分隔的数字输入。
# 假设程序输入：1,2,3,4,5,6,7,8,9 输出应该是：1,3,5,7,9
''''
values = input('请输入一串数字：')
numbers = [x for x in values.split(',') if int(x) % 2 != 0]
print(','.join(numbers))
'''

# 17.问题：编写一个程序，根据控制台输入的事务日志计算银行帐户的净金额。 事务日志格式如下所示： D 100 W 200 D 表示存款，而 W 表示提款。
# 假设向程序依次输入：D 300；D 300；W 200；D 100； 则输出应该为：500 提示：如果输入数据被提供给问题，则应该假定它是控制台输入。
''''
netAmount = 0
while True:
    print('输入：')
    s = input()
    if not s:
        break
    values = s.split(' ')
    operation = values[0]
    amount = int(values[1])
    if operation == 'D':
        netAmount += amount
    elif operation == 'W':
        netAmount -= amount
    else:
        pass
print(netAmount)
'''

# 18.问题：网站要求用户输入用户名和密码进行注册。编写程序以检查用户输入的密码有效性。
# 以下是检查密码的标准： 1 [a-z] 之间至少有 1 个字母    2 [0-9] 之间至少有 1 个数字
# 3 [A-Z] 之间至少有一个字母   4 [$＃@] 中至少有 1 个字符    5 最短交易密码长度：6   6 交易密码的最大长度：12
# 您的程序接收一系列逗号分隔的密码，并将根据上述标准进行检查，将打印符合条件的密码，每个密码用逗号分隔。
# 例：如果以下密码作为程序的输入：ABd1234@1,a F1#,2w3E*,2We3345 则程序的输出应该是：ABd1234@1
'''
import re
value = []
print('请输入：')
items = [x for x in input().split(',')]
for p in items:
    if len(p) < 6 or len(p) > 12:
        continue
    else:
        pass
    if not re.search('[a-z]', p):
        continue
    elif not re.search('[0-9]', p):
        continue
    elif not re.search('[A-Z]', p):
        continue
    elif not re.search('[$#@]', p):
        continue
    elif re.search('\s', p):
        continue
    else:
        pass
    value.append(p)
print(','.join(value))
'''

# 19.问题：您需要编写一个程序，按升序对（名称，年龄，高度）元组进行排序，其中 name 是字符串，age 和 height 是数字， 元组由控制台输入。
# 排序标准是：根据名称排序；然后根据年龄排序； 然后按分数排序。优先级是 name > age > 得分。
# 如果给出以下元组作为程序的输入： Tom,19,80；John,20,90；Jony,17,91；Jony,17,93；Json,21,85    然后，程序的输出应该是：
# [（‘John’，‘20’，‘90’），（‘Jony’，‘17’，‘91’），（‘Jony’，‘17’，‘93’），（‘Json’，'21 '，‘85’），（‘Tom’，‘19’，‘80’）]
# 提示：使用 itemgetter 来启用多个排序键。
''''
from operator import itemgetter
l = []
print('请输入：')
while True:
    s = input()
    if not s:
        break
    l.append(tuple(s.split(',')))
print(sorted(l, key=itemgetter(0, 1, 2)))
'''

# 20.问题：使用生成器定义一个类，该生成器可以在给定范围 0 和 n 之间迭代可被 7 整除的数字。
# 提示：考虑使用 yield。
'''''
def putNumbers(n):
    i = 0
    while i < n:
        j = i
        i = i + 1   # 自增的一步 必不可少
        if j % 7 == 0:
            yield j
for i in putNumbers(100):
    print(i)
'''

# 21.问题：机器人从原点（0,0）开始在平面中移动，机器人可以通过给定的步骤向上，向下，向左和向右移动。
# 机器人运动的痕迹如下所示： UP 5；DOWN 3；LETF 3；RIGHT 2；方向之后的数字是步骤。
# 请编写一个程序，计算一系列运动和原点之后距当前位置的距离。如果距离是浮点数，则只打印最接近的整数。
# 例：如果程序输入：UP 5；DOWN 3；LETF 3；RIGHT 2 则程序的输出应该是：2
# 提示：如果输入数据被提供给问题，则应该假定它是控制台输入。
'''''
import math
pos = [0, 0]
print('请输入运动轨迹')
while True:
    s = input()
    if not s:
        break
    movement = s.split(' ')
    direction = movement[0]
    steps = int(movement[1])
    if direction == 'UP':
        pos[1] += steps
    elif direction == 'DOWN':
        pos[1] -= steps
    elif direction == 'LEFT':
        pos[0] -= steps
    elif direction == 'RIGHT':
        pos[0] += steps
    else:
        pass
print(int(round(math.sqrt(pos[0] ** 2 + pos[1] ** 2))))
'''

# 22.问题：编写一个程序，来计算每个单词出现的频率，按字母顺序对键进行排序后输出。
# 假设程序输入： New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# 则输出应该是： 2:2 3.:1 3?:1 New:1 Python:5 Read:1 and:1 between:1 choosing:1 or:2 to:1
'''''
freq = {}
print('请输入：')
line = input()
for word in line.split():
    freq[word] = freq.get(word, 0) + 1
words = sorted(freq.keys())     # 按key值对字典排序
for w in words:
    print('%s:%d' % (w, freq[w]))
'''

# 23.写一个可以计算数字平方值的方法。
# 提示：使用 ** 运算符
'''略'''

# 24.Python 有许多内置函数，请编写一个程序来打印一些 Python 内置函数文档，例如 abs ()，int ()，input ()，并为您自己的功能添加文档；
# 提示：内置文档方法是__doc__；
'''
print(abs.__doc__)
print(int.__doc__)
print( input.__doc__)
def square(num) :
    Return the square value of the input number.The input number must be integer 
    return num ** 2
print (square(2))
print(square.__doc__)
'''

# 25.定义一个类，它具有类参数并具有相同的实例参数.
# 提示：定义一个实例参数，需要在__init__方法中添加它。您可以使用构造参数初始化对象，也可以稍后设置该值

























