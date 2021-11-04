### 常用
符号	 解释	     示例	    说明
.	匹配任意字符	b.t	可以匹配 bat /but/b#t /b1t 等
\w	匹配字母 / 数字 / 下划线	b\wt	可以匹配 bat /b1t /b_t 等
但不能匹配 b#t
\s	匹配空白字符（包括 \r、\n、\t 等）	love\syou	可以匹配 love you
\d	匹配数字	\d\d	可以匹配 01 / 23 / 99 等
\b	匹配单词的边界	\bThe\b	
^	匹配字符串的开始	^The	可以匹配 The 开头的字符串
$	匹配字符串的结束	.exe$	可以匹配.exe 结尾的字符串
\W	匹配非字母 / 数字 / 下划线	b\Wt	可以匹配 b#t /b@t 等
但不能匹配 but /b1t /b_t 等
\S	匹配非空白字符	love\Syou	可以匹配 love#you 等
但不能匹配 love you
\D	匹配非数字	\d\D	可以匹配 9a / 3# / 0F 等
\B	匹配非单词边界	\Bio\B	
[]	匹配来自字符集的任意单一字符	[aeiou]	可以匹配任一元音字母字符
[^]	匹配不在字符集中的任意单一字符	[^aeiou]	可以匹配任一非元音字母字符
*	匹配 0 次或多次	\w*	
+	匹配 1 次或多次	\w+	
?	匹配 0 次或 1 次	\w?	
{N}	匹配 N 次	\w{3}	
{M,}	匹配至少 M 次	\w{3,}	
{M,N}	匹配至少 M 次至多 N 次	\w{3,6}	
|	分支	foo|bar	可以匹配 foo 或者 bar
(?#)	注释		
(exp)	匹配 exp 并捕获到自动命名的组中		
(?<name>exp)	匹配 exp 并捕获到名为 name 的组中		
(?:exp)	匹配 exp 但是不捕获匹配的文本		
(?=exp)	匹配 exp 前面的位置	\b\w+(?=ing)	可以匹配 I'm dancing 中的 danc
(?<=exp)	匹配 exp 后面的位置	(?<=\bdanc)\w+\b	可以匹配 I love dancing and reading 中的第一个 ing
(?!exp)	匹配后面不是 exp 的位置		
(?<!exp)	匹配前面不是 exp 的位置		
*?	重复任意次，但尽可能少重复	a.*b
a.*?b	将正则表达式应用于 aabab，前者会匹配整个字符串 aabab，后者会匹配 aab 和 ab 两个字符串
+?	重复 1 次或多次，但尽可能少重复		
??	重复 0 次或 1 次，但尽可能少重复		
{M,N}?	重复 M 到 N 次，但尽可能少重复		
{M,}?	重复 M 次以上，但尽可能少重复	