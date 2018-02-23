
var1 = 'Hello World!'
var2 = "Runoob"
print ("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:5])

var1 = 'Hello World!'
print ("已更新字符串 : ", var1[:6] + 'Runoob!')


print()
# [::2] 表示的是从头到尾，步长为2。第一个冒号两侧的数字是指截取字符串的范围,第二个冒号后面是指截取的步长。
L=['a','b','c','d','e','f','g']
print(L[::2]) 
# ['a', 'c', 'e', 'g']


'''
字符串的分割还有partition()这种方式。

partition(sep)  --> (head,sep,tail)
从左向右遇到分隔符把字符串分割成两部分，返回头、分割符、尾三部分的三元组。如果没有找到分割符，就返回头、尾两个空元素的三元组。
'''
print()
s1 = "I'm a good sutdent."
#以'good'为分割符，返回头、分割符、尾三部分。
s2 = s1.partition('good')
#没有找到分割符'abc'，返回头、尾两个空元素的元组。
s3 = s1.partition('abc')

print(s1)
print(s2)
print(s3)

#结果如下：

# I'm a good sutdent.
#("I'm a ", 'good', ' sutdent.')
#("I'm a good sutdent.", '', '')





'''
Python转义字符
在需要在字符中使用特殊字符时，python用反斜杠(\)转义字符。如下表：

转义字符	描述
\(在行尾时)	续行符
\\	反斜杠符号
\a	响铃
\b	退格(Backspace)
\e	转义
\000	空
\n	换行
\v	纵向制表符
\t	横向制表符
\r	回车
\f	换页
\oyy	八进制数，yy代表的字符，例如：\o12代表换行
'''
# \xyy	十六进制数，yy代表的字符，例如：\x0a代表换行
# \other	其它的字符以普通格式输出
# \'	单引号
# \"	双引号


print()

a = "Hello"
b = "Python"
print("a + b 输出结果：", a + b)
print("a * 2 输出结果：", a * 2)
print("a[1] 输出结果：", a[1])
print("a[1:4] 输出结果：", a[1:4])
if( "H" in a) :
    print("H 在变量 a 中")
else :
    print("H 不在变量 a 中")
if( "M" not in a) :
    print("M 不在变量 a 中")
else :
    print("M 在变量 a 中")
print (r'\n')
print (R'\n')

print ("我叫 %s 今年 %d 岁!" % ('小明', 10))


'''
python字符串格式化符号:

    符   号	描述
      %c	 格式化字符及其ASCII码
      %s	 格式化字符串
      %d	 格式化整数
      %u	 格式化无符号整型
      %o	 格式化无符号八进制数
      %x	 格式化无符号十六进制数
      %X	 格式化无符号十六进制数（大写）
      %f	 格式化浮点数字，可指定小数点后的精度
      %e	 用科学计数法格式化浮点数
      %E	 作用同%e，用科学计数法格式化浮点数
      %g	 %f和%e的简写
      %G	 %f 和 %E 的简写
      %p	 用十六进制数格式化变量的地址
      
      猜想 python 中应该如同 C 语言一样，%g 用于打印数据时，会去掉多余的零，至多保留六位有效数字。
      
格式化操作符辅助指令:

符号	功能
*	定义宽度或者小数点精度
-	用做左对齐
+	在正数前面显示加号( + )
<sp>	在正数前面显示空格
#	在八进制数前面显示零('0')，在十六进制前面显示'0x'或者'0X'(取决于用的是'x'还是'X')
0	显示的数字前面填充'0'而不是默认的空格
%	'%%'输出一个单一的'%'
(var)	映射变量(字典参数)
m.n.	m 是显示的最小总宽度,n 是小数点后的位数(如果可用的话)      
'''

# python三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符。
print ()
para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
SELECT t.id,t.title,t.channel,t.`from`,t.company,t.stockCode,t.stockName,t.jjName,t.JJCompanyName  
FROM tp_stock t
where t.`from`='中国证券报'
"""
print (para_str)


'''
Python2.6 开始，新增了一种格式化字符串的函数 str.format()，它增强了字符串格式化的功能。
基本语法是通过 {} 和 : 来代替以前的 % 。
format 函数可以接受不限个参数，位置可以不按顺序。
实例
>>>"{} {}".format("hello", "world") # 不设置指定位置，按默认顺序
'hello world'
>>> "{0} {1}".format("hello", "world") # 设置指定位置
'hello world'
>>> "{1} {0} {1}".format("hello", "world") # 设置指定位置
'world hello world'
'''
print()
print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))
# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))
# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list)) # "0" 是必须的


# format 用法, refer to: 
# http://blog.xiayf.cn/2013/01/26/python-string-format/
# https://docs.python.org/3/library/string.html

print("{:.2f}".format(3.1415926));


'''
数字	格式	输出	描述
3.1415926	{:.2f}	3.14	保留小数点后两位
3.1415926	{:+.2f}	+3.14	带符号保留小数点后两位
-1	{:+.2f}	-1.00	带符号保留小数点后两位
2.71828	{:.0f}	3	不带小数
5	{:0>2d}	05	数字补零 (填充左边, 宽度为2)
5	{:x<4d}	5xxx	数字补x (填充右边, 宽度为4)
10	{:x<4d}	10xx	数字补x (填充右边, 宽度为4)
1000000	{:,}	1,000,000	以逗号分隔的数字格式
0.25	{:.2%}	25.00%	百分比格式
1000000000	{:.2e}	1.00e+09	指数记法
13	{:10d}	        13	右对齐 (默认, 宽度为10)
13	{:<10d}	13	左对齐 (宽度为10)
13	{:^10d}	    13	中间对齐 (宽度为10)
11	
'{:b}'.format(11)
'{:d}'.format(11)
'{:o}'.format(11)
'{:x}'.format(11)
'{:#x}'.format(11)
'{:#X}'.format(11)	
1011
11
13
b
0xb
0XB	进制
^, <, > 分别是居中、左对齐、右对齐，后面带宽度， : 号后面带填充的字符，只能是一个字符，不指定则默认是用空格填充。

+ 表示在正数前显示 +，负数前显示 -；  （空格）表示在正数前加空格

b、d、o、x 分别是二进制、十进制、八进制、十六进制。
'''

print ("{} 对应的位置是 {{0}}".format("runoob"))


'''
Python 的字符串常用内建函数如下：

序号	方法及描述
1	
capitalize()
将字符串的第一个字符转换为大写

2	
center(width, fillchar)


返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
3	
count(str, beg= 0,end=len(string))


返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
4	
bytes.decode(encoding="utf-8", errors="strict")


Python3 中没有 decode 方法，但我们可以使用 bytes 对象的 decode() 方法来解码给定的 bytes 对象，这个 bytes 对象可以由 str.encode() 来编码返回。
5	
encode(encoding='UTF-8',errors='strict')


以 encoding 指定的编码格式编码字符串，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'
6	
endswith(suffix, beg=0, end=len(string))
检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.

7	
expandtabs(tabsize=8)


把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8 。
8	
find(str, beg=0 end=len(string))


检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1
9	
index(str, beg=0, end=len(string))


跟find()方法一样，只不过如果str不在字符串中会报一个异常.
10	
isalnum()


如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True,否则返回 False
11	
isalpha()


如果字符串至少有一个字符并且所有字符都是字母则返回 True, 否则返回 False
12	
isdigit()


如果字符串只包含数字则返回 True 否则返回 False..
13	
islower()


如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
14	
isnumeric()


如果字符串中只包含数字字符，则返回 True，否则返回 False
15	
isspace()


如果字符串中只包含空白，则返回 True，否则返回 False.
16	
istitle()


如果字符串是标题化的(见 title())则返回 True，否则返回 False
17	
isupper()


如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
18	
join(seq)


以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
19	
len(string)


返回字符串长度
20	
ljust(width[, fillchar])


返回一个原字符串左对齐,并使用 fillchar 填充至长度 width 的新字符串，fillchar 默认为空格。
21	
lower()


转换字符串中所有大写字符为小写.
22	
lstrip()


截掉字符串左边的空格或指定字符。
23	
maketrans()


创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
24	
max(str)


返回字符串 str 中最大的字母。
25	
min(str)


返回字符串 str 中最小的字母。
26	
replace(old, new [, max])


把 将字符串中的 str1 替换成 str2,如果 max 指定，则替换不超过 max 次。
27	
rfind(str, beg=0,end=len(string))

类似于 find()函数，不过是从右边开始查找.
28	
rindex( str, beg=0, end=len(string))


类似于 index()，不过是从右边开始.
29	
rjust(width,[, fillchar])


返回一个原字符串右对齐,并使用fillchar(默认空格）填充至长度 width 的新字符串
30	
rstrip()


删除字符串字符串末尾的空格.
31	
split(str="", num=string.count(str))


num=string.count(str)) 以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取 num 个子字符串
32	
splitlines([keepends])


按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
33	
startswith(str, beg=0,end=len(string))


检查字符串是否是以 obj 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查。
34	
strip([chars])


在字符串上执行 lstrip()和 rstrip()
35	
swapcase()


将字符串中大写转换为小写，小写转换为大写
36	
title()


返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())
37	
translate(table, deletechars="")


根据 str 给出的表(包含 256 个字符)转换 string 的字符, 要过滤掉的字符放到 deletechars 参数中
38	
upper()


转换字符串中的小写字母为大写
39	
zfill (width)


返回长度为 width 的字符串，原字符串右对齐，前面填充0
40	
isdecimal()


检查字符串是否只包含十进制字符，如果是返回 true，否则返回 false。

'''

num=10
print('十六进制：%#x' % num)    #使用%x将十进制num格式化为十六进制
# 十六进制：0xa

print('二进制:', bin(num))      #使用bin将十进制num格式化为二进制
# 二进制: 0b1010

print('八进制：%#o' % num)      #使用%o将十进制num格式化为八进制
#八进制：0o12



print()
#针对 Counter 的升级使用，示例如下：

#必须引用如下库
from collections import Counter

#定义两个字符串变量
Var1 = "1116122137143151617181920849510"
Var2 = "1987262819009787718192084951"

#以字典的形式，输出每个字符串中出现的字符及其数量
print (Counter(Var1))
print (Counter(Var2))
#输出如下：
# Counter({'1': 12, '2': 3, '6': 2, '3': 2, '7': 2, '4': 2, '5': 2, '8': 2, '9': 2, '0': 2})
# Counter({'1': 5, '9': 5, '8': 5, '7': 4, '2': 3, '0': 3, '6': 1, '4': 1, '5': 1})
# 针对输出的结果，可以根据字典的定义进行其他必要的操作


'''
# b 字节类型
>>> s = b'witch which has which witches wrist watch'
>>> type(s)
# <class 'bytes'>
>>> len(s)
# 41

# 以下字符串类型
>>> ss = 'witch which has which witches wrist watch'
>>> type(ss)
# <class 'str'>
>>> len(ss)
# 41

# 字符串 转 字节 类型
>>> ss_utf8 = ss.encode(encoding="utf-8")
>>> ss_utf8
b'witch which has which witches wrist watch'
>>> type(ss_utf8)
# <class 'bytes'>
>>> len(ss_utf8)
# 41
'''


# 测试实例一
print("测试实例一")
str = "runoob.com"
print(str.isalnum()) # 判断所有字符都是数字或者字母
print(str.isalpha()) # 判断所有字符都是字母
print(str.isdigit()) # 判断所有字符都是数字
print(str.islower()) # 判断所有字符都是小写
print(str.isupper()) # 判断所有字符都是大写
print(str.istitle()) # 判断所有单词都是首字母大写，像标题
print(str.isspace()) # 判断所有字符都是空白字符、\t、\n、\r

str = "www.runoob.com"
print(str.upper())          # 把所有字符中的小写字母转换成大写字母
print(str.lower())          # 把所有字符中的大写字母转换成小写字母
print(str.capitalize())     # 把第一个字母转化为大写字母，其余小写
print(str.title())          # 把每个单词的第一个字母转化为大写，其余小写
'''
WWW.RUNOOB.COM
www.runoob.com
Www.runoob.com
Www.Runoob.Com
'''


