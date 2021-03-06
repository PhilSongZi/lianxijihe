## The Zen of Python, by Tim Peters
> just remember and do as thee.  

Beautiful is better than ugly.  
Explicit is better than implicit.   
Simple is better than complex.       
Complex is better than complicated.     
Flat is better than nested.     
Sparse is better than dense.    
Readability counts.     
Special cases aren't special enough to break the rules.     
Although practicality beats purity.     
Errors should never pass silently.  
Unless explicitly silenced.     
In the face of ambiguity, refuse the temptation to guess.      
There should be one-- and preferably only one --obvious way to do it.   
Although that way may not be obvious at first unless you're Dutch.      
Now is better than never.   
Although never is often better than *right* now.    
If the implementation is hard to explain, it's a bad idea.  
If the implementation is easy to explain, it may be a good idea.    
Namespaces are one honking great idea -- let's do more of those!    

---

## 重看的查漏补缺：
1. PEP-8：多单词下划线连接，受保护的实例属性用单个下划线开头，私有的实例属性以双下划线开头。另外，命名做到见名知意。PEP8要求标识符的名字用全小写多个单词用下划线连接，但是部分程序员和公司更倾向于使用驼峰命名法(驼峰标识)。
2. 练习1：1.判断一个数是否是素数。2.求输入两个正数的最小公倍数和最大公约数。
3. 练习2:1.水仙花数。2.百钱百鸡问题。3.CRAPR赌博游戏。4.生成斐波那契数列的前20个数。5.找出10000以内的完美数。6.找出100以内的所有素数。7.判断回文。8.判断回文素数。
4. 变量作用域：Python 查找一个变量时会按照 “局部作用域”、“嵌套作用域”、“全局作用域” 和 “内置作用域” 的顺序进行搜索，前三者我们在上面的代码中已经看到了，所谓的 “内置作用域” 就是 Python 内置的那些标识符，我们之前用过的 input、print、int 等都属于内置作用域。
5. 生成式和生成器：
   1. f = [x ** 2 for x in range(1, 1000)]——用列表的生成表达式语法创建列表容器，用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间。
   2. f = (x ** 2 for x in range(1, 1000))——创建的不是一个列表而是一个生成器对象，通过生成器可以获取到数据但它不占用额外的空间存储数据，每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)。
   3. Python中另外一种定义生成器的方式，就是通过yield关键字将一个普通函数改造成生成器函数。
6. 创建集合的推导式语法(推导式也可以用于推导集合)：set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
7. 面向对象：把一组数据结构和处理它们的方法组成对象（object），把相同行为的对象归纳为类（class），通过类的封装（encapsulation）隐藏内部细节，通过继承（inheritance）实现类的特化（specialization）和泛化（generalization），通过多态（polymorphism）实现基于对象类型的动态分派。
8. 列表嵌套：列表容器实际上是对对象的引用，并非在堆中真正创建了对象，所以在对嵌套列表进行操作时，时刻谨记这点。
程序中可以使用的内存从逻辑上可以为五个部分，按照地址从高到低依次是：栈（stack）、堆（heap）、数据段（data segment）、只读数据段（static area）和代码段（code segment）。
其中，栈用来存储局部、临时变量，以及函数调用时保存现场和恢复现场需要用到的数据，这部分内存在代码块开始执行时自动分配，代码块执行结束时自动释放，通常由编译器自动管理；堆的大小不固定，可以动态的分配和回收，因此如果程序中有大量的数据需要处理，这些数据通常都放在堆上，如果堆空间没有正确的被释放会引发内存泄露的问题，而像Python、Java等编程语言都使用了垃圾回收机制来实现自动化的内存管理（自动回收不再使用的堆空间）。
所以下面的代码中，变量a并不是真正的对象，它是对象的引用，相当于记录了对象在堆空间的地址，通过这个地址我们可以访问到对应的对象；同理，变量b是列表容器的引用，它引用了堆空间上的列表容器，而列表容器中并没有保存真正的对象，它保存的也仅仅是对象的引用。
>a = object()
> 
>b = ['apple', 'pitaya', 'grape']
9. 文件操作：参数列表：{r:读取（默认），w:写入(会截断以前的内容)，x:写入（如果文件已经存在会产生异常），a:追加（将内容写入到已有文件的末尾），b:二进制模式，t:文本模式（默认），+:更新（既可以读又可以写）}。
10. json 模块主要有四个比较重要的函数，分别是：
    1. dump - 将 Python 对象按照 JSON 格式序列化到文件中
    2. dumps - 将 Python 对象处理成 JSON 格式的字符串
    3. load - 将文件中的 JSON 数据反序列化成对象
    4. loads - 将字符串的内容反序列化成 Python 对象

## 学好学精之一：正则表达式
1. 处理字符串时，有查找符合某些复杂规则的字符串的需要。正则表达式就是用于描述这些规则的工具。换句话说，正则表达式就是记录文本规则的代码。
2. 元字符（metacharacter）
   1. >表1.常用的元字符
       代码	说明
       .	匹配除换行符以外的任意字符
       \w	匹配字母或数字或下划线或汉字
       \s	匹配任意的空白符
       \d	匹配数字
       \b	匹配单词的开始或结束
       ^	匹配字符串的开始
       $	匹配字符串的结束
   2. >表2.常用的限定符
       代码/语法	说明* 重复零次或更多次    + 重复一次或更多次      ?	重复零次或一次     {n}	重复n次      {n,}	重复n次或更多次     {n,m}	重复n到m次
   3. > 1.字符转义：要匹配元字符时对元字符转义。 2.分支：符号（|）——分隔几种满足规则的表达式。注意：匹配分支时从左到右匹配，一旦满足之后就不再查找后面的规则。 3.
   4. > 反义：表3.常用的反义代码
        代码/语法	说明
   \W	匹配任意不是字母，数字，下划线，汉字的字符
\S	匹配任意不是空白符的字符
\D	匹配任意非数字的字符
\B	匹配不是单词开头或结束的位置
[^x]	匹配除了x以外的任意字符
[^aeiou]	匹配除了aeiou这几个字母以外的任意字符
   5. > 处理选项：表6.常用的处理选项
名称	说明
IgnoreCase(忽略大小写)	匹配时不区分大小写。
Multiline(多行模式)	更改^和$的含义，使它们分别在任意一行的行首和行尾匹配，而不仅仅在整个字符串的开头和结尾匹配。(在此模式下,$的精确含意是:匹配\n之前的位置以及字符串结束前的位置.)
Singleline(单行模式)	更改.的含义，使它与每一个字符匹配（包括换行符\n）。
IgnorePatternWhitespace(忽略空白)	忽略表达式中的非转义空白并启用由#标记的注释。
ExplicitCapture(显式捕获)	仅捕获已被显式命名的组。
3. 进阶：
    1. 平衡组、递归匹配（看不懂，略）
    2. 其他语法。
4. Python中的正则表达：
   1. 
   
## corepoint1：spider
1. 技术清单：
    1. 下载数据 - urllib / requests / aiohttp / httpx。
    2. 解析数据 - re / lxml / beautifulsoup4 / pyquery。
    3. 缓存和持久化 - mysqlclient / sqlalchemy / peewee / redis / pymongo。
    4. 生成数字签名 - hashlib。
    5. 序列化和压缩 - pickle / json / zlib。
    6. 调度器 - multiprocessing / threading / concurrent.futures。
2. 







