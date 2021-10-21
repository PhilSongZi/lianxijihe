# Markdown基本语法
---

## Markdown标题语法 ##
* “#”的数量代表了标题的级别，几个#好就是几级。
* 可选语法：在文本下方添加任意数量的==号来标识一级标题，或者---号来标识二级标题。

## Markdown段落语法 ##
* 要创建段落，使用空白行将一行或多行文本进行分隔。
* 不用空格或者tab缩进段落。

## MarkDown换行（LineBreak）语法 ##
* 在一行的末尾添加两个或多个空格，然后按回车键，即可创建一个换行。
* 空格不好看到，所以，在行尾加上HTML中使用的<br>标签来实现换行。

## Markdown强调语法 ##
* 粗体（Bold）：在单词**前后**加上两个 “*” 或者 “_”。 
* 如需加粗一个单词或短语的中间部分用以表示强调的话，请在要加粗部分的两侧各添加两个星号（asterisks）。
* 斜体（Italic）：要用斜体显示文本，在单词或短语前后添加一个星号（asterisk）或下划线（underscore）。要斜体突出单词的中间部分，请在字母前后各添加一个星号，中间不要带空格。
* 要同时用粗体和斜体突出显示文本，在单词或短语的前后各添加三个星号或下划线。
* 要加粗并用斜体显示单词或短语的中间部分，请在要突出显示的部分前后各添加三个星号，中间不要带空格

## Markdown引用语法 ##
* 创建引用块：在段落前添加一个“>”号。
>这是一个引用的示例。

* 多个段落的块引用：为段落之间的空白行添加一个“>”号。
>引用段落1
>
>引用段落2

* 块引用的嵌套：在要嵌套的段落前一个“>>”符号。
>yinyong 111
>
>>引用的引用2222

* 带有其他元素的块引用：块引用可以包含其他 Markdown 格式的元素。实验一下哪些元素可以使用这个。示例如下：
> #### The quarterly results look great!
>
> - Revenue was off the chart.
> - Profits were higher than ever.
>
>  *Everything* is going according to **plan**.

## Markdown列表语法 ##
* 有序列表：在每个列表项前面加上数字并紧跟一个英文句号。（数字必以1起始，但不必按数字顺序排列。）示例：

>1. 首先

>2. 其次

>3. 然后

* 无序列表：在每个列表项前面加上破折号（-）、星号（*）或者加号（+）。缩进一个或多个列表项可创建嵌套列表。示例：
>+ 小子松
>+ 摸鱼儿
>+ 月巴虎
>+ Aseity
	+ 马飞飞
	+ 虎子
>+ 秦喵喵

* 在列表中嵌套其他元素：要在保留列表连续性的同时在列表中添加另一种元素，请将该元素缩进四个空格或一个制表符。
* 示例如下：

1.**段落：**

*   This is the first list item.
*   Here's the second list item.

    I need to add another paragraph below the second list item.

*   And here's the third list item.

2.**引用块：**

*   This is the first list item.
*   Here's the second list item.

  > A blockquote would look great below the second list item.

*   And here's the third list item.

3.**代码块：**代码块通常采用**四个空格或一个制表符缩进**。当它们被放在列表中时，将它们缩进八个空格或两个制表符。

1.  Open the file.
2.  Find the following code block on line 21:

        <html>
          <head>
            <title>Test</title>
          </head>

3.  Update the title to match the name of your website.

4.**图片：**插入图片最基本的格式：
**注意——**插本地图片用 ***相对路径（绝对路径不支持！！）***，同时图片或者路径名字不要有空格！


 > ![Alternative text](link "optional title") 

    Alternative text：图片的 Alternative 文本，用来描述图片的关键词，可以不写。最初的本意是当图片因为某种原因不能被显示时而出现的替代文字，后来又被用于 SEO，可以方便搜索引擎根据 Alt text 里面的关键词搜索到图片。 

    link：可以是图片的本地地址、网址。

    "optional title"：鼠标悬置于图片上会出现的标题文字，可以不写。

   使用 base64 图片编码时格式：

    ![Alternative text][base64 label]  // 都是中括号 []

   base64 label: 图片 Base64 编码的标签名。

> 示例1(本地图片)：！[测试图片](".\\SolidWorks练习\\草图练习2.png")

> 示例2（网络图片）：

> ![CSDN图标](https://csdnimg.cn/cdn/content-toolbar/csdn-logo_.png?v=20190924.1 "CSDN图标")

> 示例3（base64图片转码）：
> CSDN 图片，转码为 Base64：Base64 编码统一放于文档末尾，方便管理
> 
> ![csdn图片Base64][csdn]

另一个坑：不能有空格！ 包括可替换文本；资源标签，也就是 Base64 编码的，例如上面的‘csdn 图片 Base64’,'csdn'。

## Markdown代码语法 ##
* 要将单词或短语表示为代码，请将其包裹在反引号 (`) 中。
* 转义反引号：代码或单词中包含一个或多个反引号，将单词或短语包裹在双反引号（``）中。

> ``use `code` in your note.``

* 代码块： 要创建代码块，将代码块的每一行缩进至少四个空格或一个制表符。

>     <html>
>       <head>
>       </head>
>     </html>

## Markdown分隔线语法 ##
* 在单独一行上使用三个或多个星号、破折号、下划线，并且不能有其他内容。
* 为了兼容性，在分割线的前后都加上空白行。
> try to put a blank line before...

>---

> ...and after a horizontal rule.


## Markdown链接语法 ##
* 链接文本放在中括号内，链接地址放在后面的括号里，链接title可选。
* 超链接语法代码：[超链接显示名](超链接地址  “超链接title”)。对应的HTML代码：<a href="超链接地址" title="超链接title">超链接显示名</a>。

> 这是一个链接： [Markdown语法](https://markdown.com.cn)。

* 给链接增加title：
> [Markdown语法](https://markdown.com.cn "最好的Markdown教程")

* 网址和email地址：尖括号括起来即可。
> <https://markdown.com.cn>
> <greensun.h@gmail.com>

* 带格式化的链接：强调链接，在链接语法前后加星号。要将链接表示为代码，在方括号中加反引号。

> I love fishing on site **[bilibil](https://bilibili.com "冲浪急先锋之家")**

> see the section on [`code`](#code).

* 引用类型链接：是一种特殊的链接，它使 URL 在 Markdown 中更易于显示和阅读。参考样式链接分为两部分：与文本保持内联的部分以及存储在文件中其他位置的部分，以使文本易于阅读。
* 第一部分格式：第一组方括号内为链接的文本，第二组方括号内显示一个标签，指向存在文档其他位置的链接（相当于索引了）。

> [hobbit-hole][1]

* 第二部分格式：方括号中的标签其后紧跟一个冒号和至少一个空格（例如 [label]:）；链接的 URL，可以选择将其括在尖括号中；链接的可选标题，可以将其括在双引号，单引号或括号中。
* 可以把第二部分放在文档的任何地方，比如段落下方，文档末尾。
* 不同Markdown程序处理空格方式不一，用%20代替空格。

> [link](https://www.example.com/my%20great%20page)

> [1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle
> [1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle "Hobbit lifestyles"
> [1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle 'Hobbit lifestyles'
> [1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle (Hobbit lifestyles)
> [1]: <https://en.wikipedia.org/wiki/Hobbit#Lifestyle> "Hobbit lifestyles"
> [1]: <https://en.wikipedia.org/wiki/Hobbit#Lifestyle> 'Hobbit lifestyles'
> [1]: <https://en.wikipedia.org/wiki/Hobbit#Lifestyle> (Hobbit lifestyles)

## Markdown图片语法 ##
* 语法：![图片A](图片链接or图片本路径 "图片title")

> ![this is a picture](./SolidWorks练习/草图练习2.png "加一张图")

* 给图片加链接，则：把图片括在方括号内，再把链接加在圆括号里。

> [![沙漠中的岩石图片](/assets/img/shiprock.jpg "Shiprock")](https://markdown.com.cn)

## Markdown转义字符语法 ##
* 对要转义的字符，前面加上一个反斜杠字符即可。
* 可转义字符：**查表就完事了，记个锤子。**
* 特殊字符自动转义：Markdown允许直接使用&和<符号，而在HTML中需要转义才可用。
* 使用 & 符号的作为 HTML 实体的一部分时，它不会被转换，而在其它情况下，它会被转换成 &amp; 。
* Markdown支持行内 HTML ，如果你使用 < 符号作为 HTML 标签的分隔符，那 Markdown 也不会对它做任何转换。
* 在 Markdown 的块级元素和内联元素中， < 和 & 两个符号都会被自动转换成 HTML 实体.
* 示例：1.插入一个著作权符号；2.&被转义了；3.

> &copy;

> AT&T；

> 4 < 5

## Markdown内嵌HTML标签
* 添加HTML标签打Markdown文本内就可以直接使用HTML本身。

* 行级内联标签：如`<span>`、`<cite>`、`<del>`不受限制，可在Markdown的段落、列表或者标题中任意使用。在内联标签的范围内，Markdown的语法是可以解析的。

> This **word** is bold. This <em>word<em> is italic.

* 区块标签:区块元素比如`<div>` `<table>` `<pre>` `<p>`等标签，必须在前后加入空行，以便于内容区分。这些元素的开始与结尾标签，不能用tab或者空白来缩进。

> This is a regular paragraph.

> <table>
>	  <tr>
>		  <td>Foo</td>
>	  </tr>
> </table>

> This is another regular paragraph.



# Markdown扩展语法 #
---

## Markdown表格

## Markdown围栏代码块

## Markdown脚注

## Markdown标题编号

## Markdown定义列表

## Markdown删除线

## Markdown任务列表语法

## Markdown使用emoji表情

## 自动网址链接
* Markdown处理器一般会自动把URL转换为链接，要禁止自动链接，用反引号把URL标识为代码即可。

> `https://www.example/com`















[csdn]:data:image/png;base64,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


