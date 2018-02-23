
'''
迭代器
迭代是Python最强大的功能之一，是访问集合元素的一种方式。。

迭代器是一个可以记住遍历的位置的对象。

迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。

迭代器有两个基本的方法：iter() 和 next()。

字符串，列表或元组对象都可用于创建迭代器：

>>>list=[1,2,3,4]
>>> it = iter(list) # 创建迭代器对象
>>> print (next(it)) # 输出迭代器的下一个元素
1
>>> print (next(it))
2
'''
# 迭代器对象可以使用常规for语句进行遍历：
list=[1,2,3,4]
it = iter(list) # 创建迭代器对象
for x in it:
    print (x, end=" ")
    

'''
list=[1,2,3,4]
it = iter(list) # 创建迭代器对象
while True:
    try:
        print (next(it))
    except StopIteration:
        sys.exit()
'''


'''
生成器
在 Python 中，使用了 yield 的函数被称为生成器（generator）。

跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。

在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回yield的值。并在下一次执行 next()方法时从当前位置继续运行。

一个函数 f，f 返回一个 list，这个 list 是动态计算出来的（不管是数学上的计算还是逻辑上的读取格式化），
并且这个 list 会很大（无论是固定很大还是随着输入参数的增大而增大），
这个时候，我们希望每次调用这个函数并使用迭代器进行循环的时候一个一个的得到每个 list 元素而不是直接得到一个完整的 list 来节省内存，这个时候 yield 就很有用。

简单地讲，yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数不再是一个普通函数，
Python 解释器会将其视为一个 generator，调用 fibonacci(5) 不会执行 fab 函数，而是返回一个 iterable 对象！
在 for 循环执行时，每次循环都会执行 fibonacci 函数内部的代码，执行到 yield b 时，
fibonacci 函数就返回一个迭代值，下次迭代时，代码从 yield b 的下一条语句继续执行，
而函数的本地变量看起来和上次中断执行前是完全一样的，于是函数继续执行，直到再次遇到 yield。
当函数执行结束时，generator 自动抛出 StopIteration 异常，表示迭代完成。在 for 循环里，无需处理 StopIteration 异常，循环会正常结束。

以下实例使用 yield 实现斐波那契数列：
'''
print()
print("生成器函数 - 斐波那契")
def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield b
        a, b = b, a + b
        counter += 1
        
f = fibonacci(10) # f 是一个迭代器，由生成器返回生成
for x in f : 
    print (x, end=" ")

'''
while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()
'''


print()
l = [i for i in range(0,15)]
print(l)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

m = (i for i in range(0,15))
print(m)
# <generator object <genexpr> at 0x104b6f258>
for g in m:
    print(g,end=', ')


'''
通过 iterable 对象来迭代

for i in range(1000): pass
会导致生成一个 1000 个元素的 List，而代码：

for i in xrange(1000): pass
则不会生成一个 1000 个元素的 List，而是在每次迭代中返回下一个数值，内存空间占用很小。因为 xrange 不返回 List，而是返回一个 iterable 对象。
'''

# for i in xrange(1000): pass


class Fab(object):
    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration()

for n in Fab(5):
    print(n)


'''
一个带有 yield 的函数就是一个 generator，它和普通函数不同，生成一个 generator 看起来像函数调用，但不会执行任何函数代码，
直到对其调用 next()（在 for 循环中会自动调用 next()）才开始执行。虽然执行流程仍按函数的流程执行，
但每执行到一个 yield 语句就会中断，并返回一个迭代值，下次执行时从 yield 的下一个语句继续执行。
看起来就好像一个函数在正常执行的过程中被 yield 中断了数次，每次中断都会通过 yield 返回当前的迭代值。

yield 的好处是显而易见的，把一个函数改写为一个 generator 就获得了迭代能力，
比起用类的实例保存状态来计算下一个 next() 的值，不仅代码简洁，而且执行流程异常清晰。
'''

# 如何判断一个函数是否是一个特殊的 generator 函数？可以利用 isgeneratorfunction 判断：
from inspect import isgeneratorfunction
print(isgeneratorfunction(fibonacci))

# 要注意区分 fibonacci 和 fibonacci(5)，fibonacci 是一个 generator function，而 fibonacci(5) 是调用 fibonacci 返回的一个 generator，好比类的定义和类的实例的区别：
import types
print(isinstance(fibonacci, types.GeneratorType))
# False
print(isinstance(fibonacci(5), types.GeneratorType))
# True

# fibonacci 是无法迭代的，而 fibonacci(5) 是可迭代的：
from collections import Iterable
print(isinstance(fibonacci, Iterable))
# False
print(isinstance(fibonacci(5), Iterable))
# True


'''
return 的作用
在一个 generator function 中，如果没有 return，则默认执行至函数完毕，如果在执行过程中 return，则直接抛出 StopIteration 终止迭代。
'''


'''
另一个例子
另一个 yield 的例子来源于文件读取。如果直接对文件对象调用 read() 方法，会导致不可预测的内存占用。好的方法是利用固定长度的缓冲区来不断读取文件内容。通过 yield，我们不再需要编写读文件的迭代类，就可以轻松实现文件读取：

清单 9. 另一个 yield 的例子

实例
def read_file(fpath):
BLOCK_SIZE = 1024
with open(fpath, 'rb') as f:
while True:
block = f.read(BLOCK_SIZE)
if block:
yield block
else:
return
'''



