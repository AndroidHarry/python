
'''
Python两种输出值的方式: 表达式语句和 print() 函数。

第三种方式是使用文件对象的 write() 方法，标准输出文件可以用 sys.stdout 引用。

如果你希望输出的形式更加多样，可以使用 str.format() 函数来格式化输出值。

如果你希望将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现。

str()： 函数返回一个用户易读的表达形式。
repr()： 产生一个解释器易读的表达形式。
'''


#  repr() 函数可以转义字符串中的特殊字符
hello = 'hello, runoob\n'
hellos = repr(hello)
print(hellos)
print(str(hello))
# 'hello, runoob\n'

# repr() 的参数可以是 Python 的任何对象
x=10
y=20
print(repr((x, y, ('Google', 'Runoob'))))



# 这里有两种方式输出一个平方与立方的表:
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # 注意前一行 'end' 的使用
    print(repr(x*x*x).rjust(4))
'''
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
'''
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
'''
注意：在第一个例子中, 每列间的空格由 print() 添加。

这个例子展示了字符串对象的 rjust() 方法, 它可以将字符串靠右, 并在左边填充空格。

还有类似的方法, 如 ljust() 和 center()。 这些方法并不会写任何东西, 它们仅仅返回新的字符串。
'''


'''
另一个方法 zfill(), 它会在数字的左边填充 0，如下所示：

>>> '12'.zfill(5)
'00012'
>>> '-3.14'.zfill(7)
'-003.14'
>>> '3.14159265359'.zfill(5)
'3.14159265359'
'''


#####################################################################################
# str.format() 的基本使用如下:

print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))
# 菜鸟教程网址： "www.runoob.com!"
# 括号及其里面的字符 (称作格式化字段) 将会被 format() 中的参数替换。
# 在括号中的数字用于指向传入对象在 format() 中的位置，如下所示：

print('{0} 和 {1}'.format('Google', 'Runoob'))
# Google 和 Runoob
print('{1} 和 {0}'.format('Google', 'Runoob'))
# Runoob 和 Google

# 如果在 format() 中使用了关键字参数, 那么它们的值会指向使用该名字的参数。
print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))
# 菜鸟教程网址： www.runoob.com

# 位置及关键字参数可以任意的结合:
print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Runoob', other='Taobao'))
# 站点列表 Google, Runoob, 和 Taobao。

# '!a' (使用 ascii()), '!s' (使用 str()) 和 '!r' (使用 repr()) 可以用于在格式化某个值之前对其进行转化:
import math
print('常量 PI 的值近似为： {}。'.format(math.pi))
# 常量 PI 的值近似为： 3.141592653589793。
print('常量 PI 的值近似为： {!r}。'.format(math.pi))
# 常量 PI 的值近似为： 3.141592653589793。
print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi))
# 常量 PI 的值近似为 3.142。

# 在 ':' 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用。
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
for name, number in table.items():
    print('{0:10} ==> {1:10d}'.format(name, number))
'''
Runoob     ==>          2
Taobao     ==>          3
Google     ==>          1
'''

# 如果你有一个很长的格式化字符串, 而你不想将它们分开, 那么在格式化时通过变量名而非位置会是很好的事情。
# 最简单的就是传入一个字典, 然后使用方括号 '[]' 来访问键值 :
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
print('Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))
# Runoob: 2; Google: 1; Taobao: 3
# 也可以通过在 table 变量前使用 '**' 来实现相同的功能：
print('Runoob: {Runoob:d}; Google: {Google:d}; Taobao: {Taobao:d}'.format(**table))
# Runoob: 2; Google: 1; Taobao: 3


# 旧式字符串格式化
# % 操作符也可以实现字符串格式化。 它将左边的参数作为类似 sprintf() 式的格式化字符串, 而将右边的代入, 然后返回格式化后的字符串. 例如:
print('常量 PI 的值近似为：%5.3f。' % math.pi)
# 常量 PI 的值近似为：3.142。

#因为 str.format() 比较新的函数， 大多数的 Python 代码仍然使用 % 操作符。但是因为这种旧式的格式化最终会从该语言中移除, 应该更多的使用 str.format().

#####################################################################################


'''
读取键盘输入
Python提供了 input() 置函数从标准输入读入一行文本，默认的标准输入是键盘。

input 可以接收一个Python表达式作为输入，并将运算结果返回。

str = input("请输入：");
print ("你输入的内容是: ", str)
'''


# 打开一个文件
f = open("/foo.txt", "w")
num = f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
print(num)
# 关闭打开的文件
f.close()

# 打开一个文件
f = open("/foo.txt", "r")
str1 = f.read()
print(str1)
# 关闭打开的文件
f.close()

# 迭代一个文件对象然后读取每行:

# 打开一个文件
f = open("/foo.txt", "r")
for line in f:
    print(line, end='')
# 关闭打开的文件
f.close()


# f.tell() 返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数。

'''
如果要改变文件当前的位置, 可以使用 f.seek(offset, from_what) 函数。

from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾，例如：

seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符
seek(x,1) ： 表示从当前位置往后移动x个字符
seek(-x,2)：表示从文件的结尾往前移动x个字符
'''
f = open('/foo.txt', 'rb+')
print(f.write(b'0123456789abcdef'))
# 16
print(f.seek(5))        # 移动到文件的第六个字节
# 5
print(f.read(1))
b'5'
print(f.seek(-3, 2))    # 移动到文件的倒数第三字节
# 13
print(f.read(1))
# b'd'
# 关闭打开的文件
f.close()


# 当处理一个文件对象时, 使用 with 关键字是非常好的方式。在结束后, 它会帮你正确的关闭文件。 而且写起来也比 try - finally 语句块要简短
with open('/foo.txt', 'rb') as f:
    read_data = f.read()
    print(read_data)
    
print(f.closed)
# True



###########################################################################################################
# pickle 模块
'''
python的pickle模块实现了基本的数据序列和反序列化。

通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。

通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。

基本接口：
pickle.dump(obj, file, [,protocol])
有了 pickle 这个对象, 就能对 file 以读取的形式打开:

x = pickle.load(file)
注解：从 file 中读取一个字符串，并将它重构为原来的python对象。

file: 类文件对象，有read()和readline()接口。
'''

import pickle

# 使用pickle模块将数据对象保存到文件
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open('data.pkl', 'wb')

# Pickle dictionary using protocol 0.
pickle.dump(data1, output)
print(data1)

# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)
print(selfref_list)
print(selfref_list[0], selfref_list[3], selfref_list[3][1])

output.close()


import pprint, pickle

#使用pickle模块从文件中重构python对象
pkl_file = open('data.pkl', 'rb')

data1 = pickle.load(pkl_file)
pprint.pprint(data1)
print(data1)

data2 = pickle.load(pkl_file)
pprint.pprint(data2)
print(data2)

pkl_file.close()
###########################################################################################################


###########################################################################################################
from urllib import request

response = request.urlopen("http://www.baidu.com/")  # 打开网站
fi = open("project.txt", 'w')                        # open一个txt文件
page = fi.write(str(response.read()))                # 网站代码写入
fi.close()                                           # 关闭txt文件
###########################################################################################################













