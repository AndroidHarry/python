#!/usr/bin/python3
import keyword;
import sys;

print("Hello, World!");

'''
第三注释
第四注释
'''

"""
第五注释
第六注释
"""

print(keyword.kwlist);


'''
python最具特色的就是使用缩进来表示代码块，不需要使用大括号({})。
缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数。实例如下：

多个语句构成代码组
缩进相同的一组语句构成一个代码块，我们称之代码组。

像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。

我们将首行及后面的代码组称为一个子句(clause)。
'''
if True:
    print ("True")
    print ("Answer")
else:
    print ("False")

'''
Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠(\)来实现多行语句，例如：
'''
item_one = "item_one ";
item_two = "item_two ";
item_three = "item_three";
total = item_one + \
        item_two + \
        item_three;
print(total);

'''
数据类型
python中数有四种类型：整数、长整数、浮点数和复数。
整数， 如 1
长整数 是比较大的整数
浮点数 如 1.23、3E-2
复数 如 1 + 2j、 1.1 + 2.2j
'''

'''
字符串
python中单引号和双引号使用完全相同。
转义符 '\'
自然字符串， 通过在字符串前加r或R。 如 r"this is a line with \n" 则\n会显示，并不是换行。
python允许处理unicode字符串，加前缀u或U， 如 u"this is an unicode string"。
字符串是不可变的。
按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。
'''
# 使用三引号('''或""")可以指定一个多行字符串。
word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，
可以由多行组成"""

#执行下面的程序在按回车键后就会等待用户输入：
input("\n\n按下 enter 键后退出。")

#Python可以在同一行中使用多条语句，语句之间使用分号(;)分割，以下是一个简单的实例：
x = 'runoob'; sys.stdout.write(x + '\n')


'''
Print 输出
print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""：
'''
x="a"
y="b"
# 换行输出
print( x )
print( y )
print('---------')
# 不换行输出
print( x, end=" " )
print( y, end=" " )
print()


'''
import 与 from...import
在 python 用 import 或者 from...import 来导入相应的模块。

将整个模块(somemodule)导入，格式为： import somemodule

从某个模块中导入某个函数,格式为： from somemodule import somefunction

从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc

将某个模块中的全部函数导入，格式为： from somemodule import *
'''
print('================Python import mode==========================');
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)

from sys import argv,path # 导入特定的成员
print('================python from import===================================')
print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path

help(max)
print(max.__doc__)



