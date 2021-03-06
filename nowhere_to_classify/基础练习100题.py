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
'''''
class Person:
    name = 'Person'     # define class parameter name
    def __init__(self, name=None):
        self.name = name

    def eat(self):
        print('%s 想抓Jerry吃。' % self.name)

Jerry = Person('Jerry')
print('%s name is %s' % (Person.name, Jerry.name))
Tom = Person()
Tom.name = 'Tom'
Tom.eat()
'''

# 26.定义一个可以计算两个数之和的函数。
# 提示：定义一个带有两个数字作为参数的函数。可以在函数中计算和并返回值。
'''略'''

# 27.定义一个可以将整数转换为字符串并在控制台中打印的函数。
# 提示：使用 str () 将数字转换为字符串。
'''''
def printValue(n):
    print(str(n))
printValue(3)
'''

# 28.定义一个可以将字符串中的数字进行相加的函数。
# 提示：使用 int () 将字符串转换为数字。
'''
def sum_str(str1):
    len1 = len(str1)
    sum = n = 0
    for i in range(len1):
        if 49 <= ord(str1[i]) <= 57:        # 判断字符ASCII码是否在数字范围内。
            n = int(str1[i]) + n
        else:
            sum = n + sum
            n = 0
    print(sum)
str1 = input('输入要计算的字符串：')
sum_str(str1)
'''

# 29.定义一个函数，它可以接收两个字符串形式的整数并计算它们的和，然后在控制台中输出。
# 提示：使用 int () 将字符串转换为整数。
'''print(int(s1) + int(s2))这句就行了'''

# 30.定义一个函数，它可以接受两个字符串作为输入，并将它们连接起来，然后在控制台中输出。
# 提示：使用 + 连接字符串
'''print(s1 + s2)'''    # +：加号，字符串连接。

# 31.定义一个函数，它可以接受两个字符串作为输入，并在控制台中以最大长度打印字符串。如果两个字符串长度相同，则函数应逐行打印所有字符串。
# 提示：使用 len () 函数获取字符串的长度。
'''if len(s1) > len(s2) 
elif len(s1) < len(s2)
else 
'''

# 32.定义一个函数，它可以接受一个整数作为输入，如果这个数字是偶数，则输出 “它是偶数”，否则输出 “它是奇数”。
# 提示：使用 % 运算符检查一个数字是偶数还是奇数。
'''if n % 2 == 0: print('他是一个偶数。')'''


# 33.：定义一个函数，它可以打印一个字典，其中键是 1 到 3 之间的数字 (包括在内)，值是键的平方。
# 提示：使用 dict [key]=value 模式将条目放入字典中。 使用 ** 运算符得到一个数字的幂。
'''''
def printDict():
    d = dict()
    d[1] = 1
    d[2] = 2 ** 2
    d[3] = 3 ** 3
    print(d)
printDict()
'''

# 34.定义一个函数，它可以打印一个字典，其中键是 1 到 20 之间的数字 (包括在内)，值是键的平方。
# 提示：使用 dict [key]=value 模式将条目放入字典中。使用 ** 操作符获取一个数的幂。对循环使用 range ()
'''''
def printDiict():
    d = dict()
    for i in range(1, 21):
        d[i] = i ** 2
    print(d)
printDiict()
'''


# 35.定义一个函数，它可以生成一个字典，其中键是 1 到 20 之间的数字 (包括在内)，值是键的平方。函数只输出值即可。
# 提示：使用 dict [key]=value 模式将条目放入字典中。使用 ** 操作符获取一个数的幂。
# 对于循环使用 range ()。使用 keys () 迭代字典中的键。我们还可以使用 item () 来获取键 / 值对
'''''
def printDiict():
    d = dict()
    for i in range(1, 21):
        d[i] = i ** 2
    for (k, v) in d.items():
        print(v)
printDiict()
'''

# 36.定义一个函数，它可以生成一个字典，其中键是 1 到 20 之间的数字 (包括在内)，值是键的平方。函数只打印键即可；
# 提示：使用 dict [key]=value 模式将条目放入字典中。使用 ** 运算符得到一个数字的幂，对循环使用 range ()，使用 keys () 迭代字典中的键，我们还可以使用 item () 来获取键 / 值对。
'''''
def printList():
    l = list()
    for i in range(1, 21):
        d[i] = i ** 2
    for k in d.keys():
        print(k)
printDiict()
'''

# 37.定义一个函数，它可以生成和打印一个列表，其中的值是 1 到 20 之间的数的平方 (包括这两个数)。
# 提示：使用 ** 运算符得到一个数字的幂，对于循环使用 range ()，使用 list.append () 向列表中添加值。
'''''
def printList():
    l = list()
    for i in range(1, 21):
        l.append(i ** 2)
    print(l)
printList()
'''

# 38.定义一个函数，它可以生成一个列表，其中的值是 1 到 20 之间的数的平方 (包括这两个数)，然后函数需要打印列表中的前 5 个元素。
# 提示：使用 ** 运算符得到一个数字的幂。对循环使用 range ()，使用 list.append () 向列表中添加值，使用 [n1:n2] 对列表进行切片；
'''''
def printList():
    l = list()
    for i in range(1, 21):
        l.append(i ** 2)
    print(l[:5])
printList()
'''

# 39.定义一个函数，它可以生成一个列表，其中的值是 1 到 20 之间的数的平方 (包括这两个数)。然后函数需要打印列表中的最后 5 个元素
# 提示：使用 ** 运算符得到一个数字的幂。对循环使用 range ()。使用 list.append () 向列表中添加值。使用 [n1:n2] 对列表进行切片。
'''''
def printList():
    l = list()
    for i in range(1, 21):
        l.append(i ** 2)
    print(l[-5:])
printList()
'''

# 40.定义一个函数，它可以生成一个列表，其中的值是 1 到 20 之间的数的平方 (包括这两个数)。然后，该函数需要打印列表中除前 5 个元素外的所有值。
# 提示：使用 ** 运算符得到一个数字的幂。对循环使用 range ()。使用 list.append () 向列表中添加值。使用 [n1:n2] 对列表进行切片；
'''''
def printList():
    l = list()
    for i in range(1, 21):
        l.append(i ** 2)
    print(l[5:])
printList()
'''

# 41.问题：定义一个函数，它可以生成并打印一个元组，其中的值是 1 到 20 之间的数的平方 (包括这两个数)。
# 提示：使用 ** 运算符得到一个数字的幂。对循环使用 range ()。使用 list.append () 向列表中添加值。使用 tuple () 从列表中获取一个元组。
'''''
def printTuple():
    l = list()
    for i in range(1, 21):
        l.append(i ** 2)
    print(tuple(l))
printTuple()
'''

# 42.问题：对于给定的元组 (1,2,3,4,5,6,7,8,9,10)，编写一个程序，在一行中输出前半部分值，在一行中输出后半部分值。
# 提示：使用 [n1:n2] 表示法从元组中获取切片。
'''略'''

# 43.问题：编写程序生成并输出另一个元组，其值是给定元组 (1,2,3,4,5,6,7,8,9,10) 中的偶数。
# 提示：使用 “for” 来迭代元组，使用 tuple () 从列表中生成一个 tuple。
'''''
tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
li = list()
for i in range(len(tuple1)):
    if tuple1[i] % 2 == 0:
        li.append(tuple1[i])
tuple2 = tuple(li)
print(tuple2)
'''

# 44.问题：写一个程序，接受一个字符串作为输入，如果字符串是 “yes” 或 “YES” 或 “Yes”，否则打印 “No”。
# 提示：使用 if 语句判断条件。
'''if s == "yes" or s == "YES" or s == "Yes":print("Yes")'''

# 45.问题：编写一个程序，可以使用过滤函数过滤列表中的偶数。列表是:[1,2,3,4,5,6,7,8,9,10]。
# 提示：使用 filter () 过滤列表中的一些元素。使用 lambda 定义匿名函数。
'''
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evenNumber = filter(lambda x: x % 2 == 0, li)
for even in evenNumber:
    print(even)
'''

# 46.问题：编写一个程序，可以使用 map () 构造一个列表，其中的元素是 [1,2,3,4,5,6,7,8,9,10] 中元素的平方。
# 提示：使用 map () 生成列表。使用 lambda 定义匿名函数。
'''
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squaredNumbers = map(lambda x: x ** 2, li)
print(squaredNumbers)
'''

# 47.问题：编写一个程序，它可以 map () 和 filter () 生成一个列表，其中的元素是 [1,2,3,4,5,6,7,8,9,101 中的偶数的平方。
# 提示：使用 map () 生成列表。使用 filter () 来过滤列表中的元素。使用 lambda 定义匿名函数。
'''
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squaredNumbers = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, li))
print(squaredNumbers)
for j in squaredNumbers:
    print(j)
'''

# 48.问题：编写一个程序，它可以 filter () 生成一个列表，其中的元素是 1 到 20 之间的偶数 (包括两个元素)。
# 提示：使用 filter () 来过滤列表中的元素。使用 lambda 定义匿名函数。
'''
evenNumbers = filter(lambda x: x % 2 == 0, range(1, 21))
for even in evenNumbers:
    print(even)
'''


# 49.问题：编写一个程序，它可以使用 map () 生成一个列表，其中的元素是 1 到 20 之间的数的平方 (包括两个数)。
# 提示：使用 map () 生成列表。使用 lambda 定义匿名函数。
'''
squaredNumbers = map(lambda x: x ** 2, range(1, 21))
for even in squaredNumbers:
    print(even)
'''

# 50.问题：定义一个名为 American 的类，它有一个名为 printNationality 的静态方法。
# 提示：使用 @staticmethod 装饰器来定义类的静态方法。
'''
class American(object):
    @staticmethod
    def printNationality():
        print("America")
anAmerican = American()
anAmerican.printNationality()
American.printNationality()
'''

# 51.问题：定义一个名为 American 的类及其子类 NewYorker。
# 提示：使用类子类 (ParentClass) 来定义子类。
'''''
class American():
    pass
class NewYorker(American):
    pass
anAmerican = American()
aNewYorker = NewYorker()
print(anAmerican)
print(aNewYorker)
'''


# 52.问题：定义一个名为 Circle 的类，可以用半径来构造。Circle 类有一个可以计算面积的方法。
# 提示：使用 def methodName (self) 定义一个方法。
'''''
class Circle(object):
    def __init__(self, r):
        self.radius = r
    def area(self):
        return self.radius ** 2 * 3.14159
aCircle = Circle(4)
print(aCircle.area())
'''

# 53.问题：定义一个名为 Rectangle 的类，它可以由长度和宽度构造。矩形类有一个方法可以计算面积。
# 提示：使用 def methodName (self) 定义一个方法。
'''''
class Rectangle(object):
    def __init__(self, width, length):
        self.width = width
        self.length = length
    def area(self):
        return self.width * self.length
aRectangle = Rectangle(5, 6)
print(aRectangle.area())
'''

# 54.问题：定义一个名为 Shape 的类及其子类 Square。Square 类有一个 init 函数，它以长度作为参数。
# 这两个类都有一个 area 函数，可以打印形状的区域，形状的区域默认为 0。
# 提示：要覆盖父类中的方法，可以在父类中定义一个同名的方法。
''''
class Shape(object):
    def __init__(self):
        pass
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, l):
        self.length = l
    def area(self):
        return self.length ** 2
aSquare = Square(6)
print(aSquare.area())
'''


# 55.问题：请引发 RuntimeError 异常。
# 提示：使用 raise () 引发异常。
'''raise RuntimeError("something wrong")'''

# 56.问题：编写一个函数来计算 5/0，并使用 try/except 来捕获异常。
# 提示：使用 try/exexception 捕获异常。
'''''
def throwError():
    return 5 / 0
try:
    throwError()
except ZeroDivisionError:
    print("division by zero!")
except Exception:
    print('caught an exception.')
finally:
    print("in finally block for cleanup.")
'''


# 57.问题：定义一个自定义异常类，它将字符串消息作为属性。
# 提示：要定义一个自定义异常，我们需要定义一个继承自 exception 的类。
'''
class MyError(Exception):
    """My own exception class.
    Attributes:
        msg -- explanation of the error"""
    def __init__(self, msg):
        self.msg = msg
error = MyError("something wrong")
print(error)
'''''

# 58.问题：假设我们有一些’username@companyname.com ' 格式的电子邮件地址，请编写程序打印给定电子邮件地址的用户名，用户名和公司名都只由字母组成。
# 示例：如果下面的电子邮件地址作为程序的输入：john@google.com. 那么，程序的输出应该是：john 在向问题提供输入数据的情况下，应该假定它是控制台输入。
# 提示：使用 \w 来匹配字母。
'''
import re
emailAddress = input()
pattern = "(\w+)@(\w+)\.(com)"
r = re.match(pattern, emailAddress)
print(r.group(1))       # r.group(N):返回第N个括号匹配到的内容。
print(r.group(2))
'''

# 59.问题：假设我们有一些 “username@companyname.com” 格式的电子邮件地址，请编写程序打印给定的电子邮件地址的公司名称；用户名和公司名都只由字母组成。
# 示例：如果下面的电子邮件地址作为程序的输入：john@google.com 那么，程序的输出应该是：google 在向问题提供输入数据的情况下，应该假定它是控制台输入。
# 提示：使用 \w 来匹配字母。
'''同上。'''

# 60.问题：编写一个程序，接收一个由空格分隔的单词序列作为输入，打印只由数字组成的单词。
# 示例：如果下面的单词作为程序的输入：2 cats and 3 dogs； 那么，程序的输出应该是：[‘2’, ‘3’] 在向问题提供输入数据的情况下，应该假定它是控制台输入。
# 提示：使用 re.findall () 使用正则表达式查找所有子字符串。
'''
import re
str = input()
print(re.findall("\d+", str))
'''

# 61.问题：打印 unicode 字符串 “hello world”。
# 提示：使用 u’strings’格式来定义 unicode 字符串；
'''
unicodeString = u"Hello World."
print(unicodeString)
print(type(unicodeString))
'''

# 62.问题：python 中的解码与编码；
# 提示：使用 encode () 与 decode () 函数进行转换。
'''
s = 'CSDN，成就一亿技术人'
enc = s.encode('utf-8')
dec = enc.decode('utf-8')
print(enc)
print(dec)
'''

# 63.问题：编写一个特殊注释来表明 Python 源代码文件是 unicode 格式的。
# -*- encoding: utf-8 -*-
# ---------------------------------#

# 64.问题：写一个程序来计算 1/2+2/3+3/4+…+n/(n+1)。 示例：如果下面的 n 作为程序的输入：5； 那么，程序的输出应该是：3.55；
# 提示：使用 float () 将整数转换为浮点数。
'''
n = int(input('输入一个数'))
sum = 0.0
for i in range(1, n+1):
    sum += float(float(i) / (i+1))
print(sum)
'''

# 65.问题：编写程序计算：当 n>0 和 F (0)=1 时，F (n)=F (n-1)+100 通过控制台输入一个给定的 n (n>0)。
# 示例：如果下面的 n 作为程序的输入：5， 那么，程序的输出应该是：500；
# 提示：我们可以在 Python 中定义递归函数。
'''
def f(n):
    if n == 0:
        return 0
    else:
        return f(n - 1) + 100
n = int(input())
print(f(n))
'''

# 66.问题：斐波那契数列的计算公式如下：如果 n=0，f (n)=0；如果 n=1，f (n)=1；如果 n>1，f (n)=f (n-1)+f (n-2)；
# 请编写一个程序，在控制台输入给定 n 的情况下计算 f (n) 的值。 示例：如果下面的 n 作为程序的输入：7； 那么，程序的输出应该是：13；
'''
def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return f(n - 1) + f(n - 2)
n = int(input())
print(f(n))
'''

# 67.问题：斐波那契数列的计算公式如下：如果 n=0，f (n)=0；如果 n=1，f (n)=1；如果 n>1，f (n)=f (n-1)+f (n-2)；
# 请编写一个程序使用列表理解输出逗号分隔的 Fibonacci 序列，并通过控制台输入给定的 n。
# 示例：如果下面的 n 作为程序的输入：7； 那么，程序的输出应该是：0,1,1,2,3,5,8,13；
# 提示：我们可以在 Python 中定义递归函数。使用列表理解从现有列表生成列表。使用 string.join () 连接字符串列表。
'''
def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return f(n - 1) + f(n - 2)
n = int(input())
values = [str(f(x)) for x in range(0, n+1)]     # range左闭右开，斐波那契n0到n
print(','.join(values))
'''

# 68.问题：请使用 generator 编写一个程序，当 n 由控制台输入时，以逗号分隔的形式输出 0 和 n 之间的偶数；
# 示例：如果下面的 n 作为程序的输入 10； 那么，程序的输出应该是：0,2,4,6,8,10
# 提示：使用 yield 生成生成器中的下一个值。
'''
def evenGenerator(n):
    i = 0
    while i <= n:
        if i % 2 == 0:
            yield i
        i += 1
n = int(input())
values = []
for even in evenGenerator(n):
    values.append(str(even))
print(','.join(values))
'''

# 69.问题：请编写一个生成器程序，以逗号分隔的形式输出 0 到 n 之间可以被 5 和 7 整除的数字，而 n 是通过控制台输入的。
# 示例：如果下面的 n 作为程序的输入：100； 那么，程序的输出应该是：0,35,70；
# 提示：使用 yield 生成生成器中的下一个值。
'''
def numGenerator(n):
    for i in range(n + 1):
        if i % 5 == 0 and i % 7 == 0:
            yield i
n = int(input())
values = []
for i in numGenerator(n):
    values.append(str(i))
print(','.join(values))
'''


# 70.问题：请写 assert 语句来验证列表 [2,4,6,8] 中的每个数字都是偶数。
# 提示：使用 “断言表达式” 进行断言。
'''
li = [2, 4, 6, 8, 9]
for i in li:
    assert i % 2 == 0, '数据错误'       # 循环执行到li[] = 9时报AssertionError退出。
    print(i)
'''

# 71.问题：请编写一个程序，从控制台接收基本数学表达式，并输出计算结果。 示例：如果下面的字符串作为程序的输入：35 + 3； 那么，程序的输出应该是：38；
# 提示：使用 eval () 计算表达式。
'''
expression = input()
print(eval(expression))
'''

# 72.问题：请编写一个二分搜索函数，搜索排序列表中的项。函数应该返回要在列表中搜索的元素的索引。
# 提示：使用 if/elif 来处理条件。
'''
import math
def binary_search(list, element):
    bottom = 0
    top = len(list) - 1
    index = -1
    while top >= bottom and index == -1:
        mid = int(math.floor((top + bottom) / 2.0))
        if list[mid] == element:
            index = mid
        elif list[mid] > element:
            top = mid - 1
        else:
            bottom = mid + 1
    return index
li = [2, 5, 7, 9, 11, 17, 22, 222]
print(binary_search(li, 11))
print(binary_search(li, 17))
'''

# 73.问题：随机生成 1,100 内的一个整数；
# 提示：random.randint ()
'''
import random
print(random.randint(a=1, b=100))   # 1 100内的整数
print(random.random() * 100)    # 10 100内的浮点数
print(random.random() * 100 - 5)     # 5-95之间的随机浮点数
'''


# 76.问题：请编写一个程序输出 O 和 10 之间的随机偶数使用随机模块和列表理解。
# 提示：对列表中的随机元素使用 random.choice ()。
'''
import random
print(random.choice([x for x in range(11) if x % 2 == 0]))
print(random.choice([i for i in range(201) if i % 5 ==0 and i % 7 == 0]))
print(random.sample([i for i in range(100, 201) if i % 2 == 0], 5))     # 生成一个包含100到200之间的5个随机偶数的列表
print(random.sample([i for i in range(201) if i % 5 == 0 and i % 7 == 0], 5))   # 1-1000中取5个被5和7整除的随机数组成列表
print(random.randrange(7, 16))      # 随机打印一个 7 到 15 之间的整数 (包括 15)
'''

# 82.问题：请编写一个程序来压缩和解压字符串 "hello world!hello world!hello world!hello world!"。
# 提示：使用 zlib.compress () 和 zlib.decompress () 来压缩和解压缩字符串。
'''
import zlib
s = b'hello world!hello world!hello world!hello world!'
t = zlib.compress(s)
print(t)
print(zlib.decompress(t))
'''

# 83.问题：请编写一个程序打印 100 次 “1+1” 执行的运行时间。
# 提示：使用 timeit () 函数测量运行时间。
'''
from timeit import Timer
t = Timer('for i in range(100): 1 + 1')
print(t.timeit())
'''


# 84.问题：请编写一个程序洗牌和打印列表 [3,6,7,8]。
# 提示：使用 shuffle () 函数洗牌列表。
'''
from random import shuffle
li = [3, 6, 7, 8]
shuffle(li)
print(li)
'''

# 86.问题：请编写一个程序，生成主语在 [“I”, “You”]，动词在 [“Play”, “Love”] 中，对象在 [“Hockey”,“Football”] 中的所有句子.
# 提示：使用 list [index] 表示法从列表中获取元素。
'''
subjects = ['I', 'You']
verbs = ['Play', 'Love']
objects = ['Hockey', 'Football']
for i in range(len(subjects)):
    for j in range(len(verbs)):
        for k in range(len(objects)):
            sentences = "%s %s %s." % (subjects[i], verbs[j], objects[k])
            print(sentences)
'''

# 87.问题：请写一个程序打印列表，删除后删除偶数 [5,6,77,45,22,12,24]。
# 提示：使用列表理解从列表中删除一组元素。
'''
li = [5, 6, 77, 45, 22, 12, 24]
li = [x for x in li if x % 2 != 0]
print(li)
'''

# 88.问题：使用列表理解，请编写程序，删除 [12,24,35,70,88,120,155] 中可被 5 和 7 整除的删除数后，打印列表。
# 提示：使用列表理解从列表中删除一组元素。
'li = [x for x in li if x % 5 == 0 and x % 7 == 0]'

# 89.问题：使用列表理解法，请编写一个程序，去掉 [12,24,35,70,88,120,155] 中的第 0,2,4,6 位置上的元素后打印列表。
# 提示：使用列表理解从列表中删除一组元素。使用 enumerate () 来获取 (索引，值) 元组。
'''
li = [12, 24, 35, 70, 88, 120, 155]
li = [x for (i, x) in enumerate(li) if i % 2 != 0]
print(li)
'''

# 90.问题：使用列表理解，编写一个程序生成一个 358 三维数组，每个元素为 0。
# 提示：使用列表理解来创建数组。
'''
array = [[[0 for col in range(8)] for col in range(5)] for col in range(3)]
print(array)
'''

# 91.问题：利用列表理解，请编写一个程序，去掉 [12,24,35,70,88,120,155] 中的第 0，第 4，第 5 个数字后，将列表打印出来。
# 提示：使用列表理解从列表中删除一组元素。使用 enumerate () 来获取 (index, value) 元组。
'''
li = [12, 24, 35, 70, 88, 120, 155]
li = [x for (i, x) in enumerate(li) if i not in (0, 4, 5)]
print(li)
'''

# 92.问题：通过使用列表理解，请编写一个程序，在 [12,24,35,24,88,120,155] 中删除值 24 后打印列表。
# 提示：使用列表的 remove 方法删除一个值。

# 93.问题：对于两个已知链表 [1,3,6,78,35,55] 和 [12,24,35,24,88,120,155]，编写一个程序来生成一个元素为上述两个链表交集的链表。
# 提示：使用 set () 和 "&=" 进行集合相交操作。
'''
set1 = set([1, 3, 6, 78, 35, 55])
set2 = set([12, 24, 35, 24, 88, 120, 155])
set1 &= set2
li = list(set1)
print(li)
'''

# 94.问题：对于给定的列表 [12,24,35,24,88,120,155,88,120,155]，编写一个程序来打印这个列表 - 删除所有重复的值与原始顺序保留。
# 提示：使用 set () 来存储一些没有重复的值。
'''
def removeDuplicate(li):
    newli = []
    seen = set()
    for item in li:
        if item not in seen:
            seen.add(item)
            newli.append(item)
    return newli
li = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
print(removeDuplicate(li))
'''

# 95.问题：定义一个类 Person 和它的两个子类：Male 和 Female。所有的类都有一个方法 “getGender”，它可以打印 “Male” 为男性类，“Female” 为女性类
# 提示：使用子类 (Parentclass) 来定义子类。
'''
class Person(object):
    def getGender(self):
        return "unkonwn"
class Male(Person):
    def getGender(self):
        return "Male"
class Female(Person):
    def getGender(self):
        return "Female"
'''

# 96.问题：请编写一个程序，计算并打印由控制台输入的字符串中的每个字符的数量。
# 示例：如果下面的字符串作为程序的输入：abcdefgab； 那么，程序的输出应该是：a,2 c,2 b,2 e,1 d,1 g,1 f,1；
# 提示：使用 dict 存储键 / 值对。使用 dict.get () 方法查找具有默认值的键。
'''
dict1 = {}
s = input()
for s in s:
    dict1[s] = dict1.get(s, 0) + 1
print('\n'.join(['%s,%s' % (k, v) for k, v in dict1.items()]))
'''

# 97.问题：请编写一个程序，从控制台接收一个字符串，并以相反的顺序打印出来。
# 示例：如果下面的字符串作为程序的输入：rise to vote sir； 那么，程序的输出应该是:ris etov ot esir；
# 提示：使用 list [::-1] 以相反的顺序迭代一个列表。
'''
s = input()
s = s[::-1]
print(s)
'''

# 98..问题：请编写一个程序，从控制台接收一个字符串，并打印具有偶数索引的字符；
# 示例：如果下面的字符串作为程序的输入：H1e2l3l4o5w6o7r8l9d 那么，程序的输出应该是：Helloworld；
# 提示：使用 list [:2] 来迭代第 2 步中的列表。
'''s = s[::2]'''

# 99.问题：请写一个程序，打印 [1,2,3] 的所有排列；
# 提示：使用 itertools.permutations) 得到 list 的排列。
# 能直接用就别去造轮子。。。。
'''
import itertools
print(list(itertools.permutations([1, 2, 3])))
'''

# 100.写一个程序来解决一个中国古代的经典难题：我们数农场里的鸡和兔子中有 35 个头和 94 条腿。我们有多少只兔子和多少只鸡？
# 提示：使用 for 循环来迭代所有可能的解决方案。
'''
def solve(numheads, numlegs):
    ns = "No Solution!"
    for i in range(numheads + 1):
        j = numheads - i
        if 2 * i + 4 * j == numlegs:
            return i, j
    return ns, ns
numheads = 35
numlegs = 94
solution = solve(35, 94)
print(solution)
'''
