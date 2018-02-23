
import math  # 导入 math 模块
import random  # 导入 random 模块

'''
Python 数字数据类型用于存储数值。

数据类型是不允许改变的,这就意味着如果改变数字数据类型得值，将重新分配内存空间。

以下实例在变量赋值时 Number 对象将被创建：

var1 = 1
var2 = 10
您也可以使用del语句删除一些数字对象的引用。

del语句的语法是：

del var1[,var2[,var3[....,varN]]]]
您可以通过使用del语句删除单个或多个对象的引用，例如：

del var
del var_a, var_b
'''


'''
Python 支持三种不同的数值类型：

整型(Int) - 通常被称为是整型或整数，是正或负整数，不带小数点。Python3 整型是没有限制大小的，可以当作 Long 类型使用，所以 Python3 没有 Python2 的 Long 类型。
浮点型(float) - 浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示（2.5e2 = 2.5 x 102 = 250）
复数( (complex)) - 复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型。

>>> number = 0xA0F # 十六进制
>>> number
2575

>>> number=0o37 # 八进制
>>> number
31
'''


dec = int(input("输入数字："))

print("十进制数为：", dec)
print("转换为二进制为：", bin(dec))
print("转换为八进制为：", oct(dec))
print("转换为十六进制为：", hex(dec))



# 具体实现
# 十进制到二进制：
def dec2bin(num):
    l = []
    if num < 0:
        return '-' + dec2bin(abs(num))
    while True:
        num, remainder = divmod(num, 2)
        l.append(str(remainder))
        if num == 0:
            return ''.join(l[::-1])
        
# 十进制到八进制：
def dec2oct(num):
    l = []
    if num < 0:
        return '-' + dec2oct(abs(num))
    while True:
        num, remainder = divmod(num, 8)
        l.append(str(remainder))
        if num == 0:
            return ''.join(l[::-1])
        
# 十进制到十六进制：
base = [str(x) for x in range(10)] + [ chr(x) for x in range(ord('A'),ord('A')+6)]
def dec2hex(num):
    l = []
    if num < 0:
        return '-' + dec2hex(abs(num))
    while True:
        num,rem = divmod(num, 16)
        l.append(base[rem])
        if num == 0:
            return ''.join(l[::-1])
        

'''
以下代码用于实现ASCII码与字符相互转换：

# Filename : test.py
# author by : www.runoob.com

# 用户输入字符
c = input("请输入一个字符: ")

# 用户输入ASCII码，并将输入的数字转为整型
a = int(input("请输入一个ASCII码: "))


print( c + " 的ASCII 码为", ord(c))
print( a , " 对应的字符为", chr(a))
执行以上代码输出结果为：

python3 test.py 
请输入一个字符: a
请输入一个ASCII码: 101
a 的ASCII 码为 97
101  对应的字符为 e
'''


'''
在交互模式中，最后被输出的表达式结果被赋值给变量 _ 。例如：

>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625
>>> round(_, 2)
113.06
此处， _ 变量应被用户视为只读变量。
---
文中对于 _ 提到，它代表了上一次的输出结果，"用户应该将其视为只读变量"，实际情况是你也可以
对于_ 赋值，_=10 是没有毛病的，但这样的结果会导致你在之后调用 _ 的时候全部变成了10，
除非你 del _。
'''


'''
对于round:

round(10.5)
10
round(11.5)
12

Python 所谓的奇进偶弃，因为浮点数的表示在计算机中并不准确，用的时候可能要注意一下。
---
print(round(10.4)) #10
print(round(10.5)) #10
print(round(10.6)) #11
print()
print(round(11.4)) #11
print(round(11.5)) #12
print(round(11.6)) #12
由运行得出结论：

当小数点左边为偶数：小数点右边X<6，舍
当小数点左边为偶数：小数点右边X>=6，入
当小数点左边为奇数：小数点右边X<5，舍
当小数点左边为奇数：小数点右边X>=5，入
所以当小数点左边分别为奇数和偶数的时候，小数点右边的取舍也分别对应两种取舍标准

这是个坑啊！不知道小数点后两位是怎样的，有兴趣的小伙伴可以试一下
---
关于round,接力分析，结论如下：

当个位为奇数，小数部分>=0.5入，其余为舍

当个位为偶数，小数部分>0.5入，其余为舍。

交互模式下的 example:

round(10.49)
10
round(10.50)
10
round(10.51)
11
round(11.50)
12
round(11.49)
11
---
国家标准也已经规定使用 "4舍6入5看齐,奇进偶不进" 取代"四舍五入".
从统计学的角度上来讲,如果大量数据无脑的采用四舍五入会造成统计结果偏大。而"奇进偶舍"可以将舍入误差降到最低。
奇进偶舍是一种比较精确比较科学的计数保留法，是一种数字修约规则。
其具体要求如下（以保留两位小数为例）：
（1）要求保留位数的后一位如果是4或者4以下的数字，则舍去， 例如 5.214保留两位小数为5.21。
（2）如果保留位数的后一位如果是6或者6以上的数字，则进上去， 例如5.216保留两位小数为5.22。
（3）如果保留位数的后一位如果是5，且该位数后没有数字。要根据保留位数的那一位决定是舍去还是进入：如果是奇数则进入，如果是偶数则舍去。例如5.215保留两位小数为5.22，5.225保留两位小数为5.22。
（4）如果保留位数的后一位如果是5，且该位数后有数字。则进上去，例如5.2152保留两位小数为5.22，5.2252保留两位小数为5.23，5.22500001保留两位小数为5.23。
从统计学的角度，"奇进偶舍"比"四舍五入"要科学，在大量运算时，它使舍入后的结果误差的均值趋于零，而不是像四舍五入那样逢五就入，导致结果偏向大数，使得误差产生积累进而产生系统误差，"奇进偶舍"使测量结果受到舍入误差的影响降到最低。
'''


# exp(x)	返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045

# log(x)	如math.log(math.e)返回1.0,math.log(100,10)返回2.0
# log10(x)	返回以10为基数的x的对数，如math.log10(100)返回 2.0


# modf(x)	返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。

print ("math.modf(100.12) : ", math.modf(100.12))
print ("math.modf(100.72) : ", math.modf(100.72))
print ("math.modf(math.pi) : ", math.modf(math.pi))


'''
随机数函数
随机数可以用于数学，游戏，安全等领域中，还经常被嵌入到算法中，用以提高算法效率，并提高程序的安全性。

Python包含以下常用随机数函数：

函数	描述
choice(seq)	从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
randrange ([start,] stop [,step])	从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1
random()	随机生成下一个实数，它在[0,1)范围内。
seed([x])	改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
shuffle(lst)	将序列的所有元素随机排序
uniform(x, y)	随机生成下一个实数，它在[x,y]范围内。
'''

print ("从 range(100) 返回一个随机数 : ", random.choice(range(100)))
print ("从列表中 [1, 2, 3, 5, 9]) 返回一个随机元素 : ", random.choice([1, 2, 3, 5, 9]))
print ("从字符串中 'Runoob' 返回一个随机字符 : ", random.choice("Runoob"))


# random.randrange ([start,] stop [,step])
# 从 1-100 中选取一个奇数
print ("randrange(1,100, 2) : ", random.randrange(1,100,2))
# 从 0-99 选取一个随机数
print ("randrange(100) : ", random.randrange(100))


# 第一个随机数
print ("random() : ", random.random())

# 第二个随机数
print ("random() : ", random.random())

# random.randint(x,y)　
# 随机生一个整数int类型，可以指定这个整数的范围
print ("random.randint(100,999)", random.randint(100,999))

# random.sample(sequence,length) 可以从指定的序列中，随机的截取指定长度的片断，不修改原序列。
lst = random.sample('abcd1234',4)
print("random.sample('abcd1234',4) :", lst)
strs = ''.join(lst)
print("strs :", strs)

# random.seed ( [x] )
# x -- 改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
random.seed()
print ("使用默认种子生成随机数：", random.random())

random.seed(10)
print ("使用整数种子生成随机数：", random.random())

random.seed("hello",2)
print ("使用字符串种子生成随机数：", random.random())


list = [20, 16, 10, 5];
random.shuffle(list)
print ("随机排序列表 : ", list)
random.shuffle(list)
print ("随机排序列表 : ", list)


# uniform() 方法将随机生成下一个实数，它在[x,y]范围内。
print ("uniform(5, 10) 的随机浮点数 : ", random.uniform(5, 10))
print ("uniform(5, 10) 的随机浮点数 : ", random.uniform(5, 10))
print ("uniform(7, 20) 的随机浮点数 : ", random.uniform(7, 20))
print ("uniform(7, 20) 的随机浮点数 : ", random.uniform(7, 20))






