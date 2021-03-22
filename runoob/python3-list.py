
# refer to
# http://www.runoob.com/python3/python3-list-operator.html


a=[1,2,3]
b=a
c=a[:]  # 浅拷贝, 非引用
a[0]=5
a   # [5, 2, 3]
b   # [5, 2, 3]
c   # [1, 2, 3]


import math  # 导入 math 模块

# 列表的数据项不需要具有相同的类型
list1 = ['Google', 'Runoob', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];
print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])

list1 = ['Google', 'Runoob', 1997, 2000]
print ("第三个元素为 : ", list1[2])
list1[2] = 2001
print ("更新后的第三个元素为 : ", list1[2])

# 可以使用 del 语句来删除列表的的元素
list1 = ['Google', 'Runoob', 1997, 2000]
print (list1)
del list1[2]
print ("删除第三个元素 : ", list1)


'''
Python 表达式	结果	描述
len([1, 2, 3])	3	长度
[1, 2, 3] + [4, 5, 6]	[1, 2, 3, 4, 5, 6]	组合
['Hi!'] * 4	['Hi!', 'Hi!', 'Hi!', 'Hi!']	重复
3 in [1, 2, 3]	True	元素是否存在于列表中
for x in [1, 2, 3]: print(x, end=" ")	1 2 3	迭代
'''

# 嵌套列表
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print (x)


'''
Python包含以下方法:

序号	方法
1	list.append(obj)
在列表末尾添加新的对象
2	list.count(obj)
统计某个元素在列表中出现的次数
3	list.extend(seq)
在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
4	list.index(obj)
从列表中找出某个值第一个匹配项的索引位置
5	list.insert(index, obj)
将对象插入列表
6	list.pop(obj=list[-1])
移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
7	list.remove(obj)
移除列表中某个值的第一个匹配项
8	list.reverse()
反向列表中元素
9	list.sort([func])
对原列表进行排序
10	list.clear()
清空列表
11	list.copy()
复制列表
'''

# extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）。
# 该方法没有返回值，但会在已存在的列表中添加新的列表内容。
list1 = ['Google', 'Runoob', 'Taobao']
list2=list(range(5)) # 创建 0-4 的列表
list1.extend(list2)  # 扩展列表
print ("扩展后的列表：", list1)


list1 = ['Google', 'Runoob', 'Taobao']
print ('Runoob 索引值为', list1.index('Runoob'))
print ('Taobao 索引值为', list1.index('Taobao'))

list1 = ['Google', 'Runoob', 'Taobao']
list1.insert(1, 'Baidu')
print ('列表插入元素后为 : ', list1)

list1 = ['Google', 'Baidu', 'Runoob', 'Taobao']
list1.pop()
print ("列表现在为 : ", list1)
list1.pop(1)
print ("列表现在为 : ", list1)

list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
list1.remove('Taobao')
print ("列表现在为 : ", list1)
list1.remove('Baidu')
print ("列表现在为 : ", list1)

list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
list1.reverse()
print ("列表反转后: ", list1)

list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
list1.sort()
print ("列表排序后 : ", list1)


# clear() 函数用于清空列表，类似于 del a[:]。
list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
list1.clear()
print ("列表清空后 : ", list1)

# copy() 函数用于复制列表，类似于 a[:]。
list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
list2 = list1.copy()
print ("list2 列表: ", list2)


'''
python 创建二维列表，将需要的参数写入 cols 和 rows 即可

list_2d = [[0 for col in range(cols)] for row in range(rows)]
实例：

>>> list_2d = [ [0 for i in range(5)] for i in range(5)]
>>> list_2d[0].append(3)
>>> list_2d[0].append(5)
>>> list_2d[2].append(7)
>>> list_2d
[[0, 0, 0, 0, 0, 3, 5], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 7], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
'''


'''
list.remove(x)	删除列表中值为 x 的第一个元素。如果没有这样的元素，就会返回一个错误。

>>> a = [66.25, 333, 333, 1, 1234.5]
>>> print(a.count(333), a.count(66.25), a.count('x'))
2 1 0
>>> a.insert(2, -1)
>>> a.append(333)
>>> a
[66.25, 333, -1, 333, 1, 1234.5, 333]
>>> a.index(333)
1
>>> a.remove(333)
>>> a
[66.25, -1, 333, 1, 1234.5, 333]
>>> a.reverse()
>>> a
[333, 1234.5, 1, 333, -1, 66.25]
>>> a.sort()
>>> a
[-1, 1, 66.25, 333, 333, 1234.5]
'''


'''
将列表当做堆栈使用
列表方法使得列表可以很方便的作为一个堆栈来使用，堆栈作为特定的数据结构，最先进入的元素最后一个被释放（后进先出）。用 append() 方法可以把一个元素添加到堆栈顶。用不指定索引的 pop() 方法可以把一个元素从堆栈顶释放出来。例如：

>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack.append(7)
>>> stack
[3, 4, 5, 6, 7]
>>> stack.pop()
7
>>> stack
[3, 4, 5, 6]
>>> stack.pop()
6
>>> stack.pop()
5
>>> stack
[3, 4]
'''


'''
将列表当作队列使用
也可以把列表当做队列用，只是在队列里第一加入的元素，第一个取出来；但是拿列表用作这样的目的效率不高。在列表的最后添加或者弹出元素速度快，然而在列表里插入或者从头部弹出速度却不快（因为所有其他的元素都得一个一个地移动）。

>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")           # Terry arrives
>>> queue.append("Graham")          # Graham arrives
>>> queue.popleft()                 # The first to arrive now leaves
'Eric'
>>> queue.popleft()                 # The second to arrive now leaves
'John'
>>> queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
'''


# 在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到：
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
'''
0 tic
1 tac
2 toe
'''


# 同时遍历两个或更多的序列，可以使用 zip() 组合：
# 除了用'{0}{1}'.format(q,a)的方法，还可以使用%s方法（两者效果一样一样的）：
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
    print('what is your %s? it is %s' %(q,a))
'''
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.
'''


'''
列表推导式
列表推导式提供了从序列创建列表的简单途径。通常应用程序将一些操作应用于某个序列的每个元素，用其获得的结果作为生成新列表的元素，或者根据确定的判定条件创建子序列。

每个列表推导式都在 for 之后跟一个表达式，然后有零到多个 for 或 if 子句。返回结果是一个根据表达从其后的 for 和 if 上下文环境中生成出来的列表。如果希望表达式推导出一个元组，就必须使用括号。

这里我们将列表中每个数值乘三，获得一个新的列表：

>>> vec = [2, 4, 6]
>>> [3*x for x in vec]
[6, 12, 18]
现在我们玩一点小花样：

>>> [[x, x**2] for x in vec]
[[2, 4], [4, 16], [6, 36]]
这里我们对序列里每一个元素逐个调用某方法：

>>> freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
>>> [weapon.strip() for weapon in freshfruit]
['banana', 'loganberry', 'passion fruit']
我们可以用 if 子句作为过滤器：

>>> [3*x for x in vec if x > 3]
[12, 18]
>>> [3*x for x in vec if x < 2]
[]
以下是一些关于循环和其它技巧的演示：

>>> vec1 = [2, 4, 6]
>>> vec2 = [4, 3, -9]
>>> [x*y for x in vec1 for y in vec2]
[8, 6, -18, 16, 12, -36, 24, 18, -54]
>>> [x+y for x in vec1 for y in vec2]
[6, 5, -7, 8, 7, -5, 10, 9, -3]
>>> [vec1[i]*vec2[i] for i in range(len(vec1))]
[8, 12, -54]
列表推导式可以使用复杂表达式或嵌套函数：

>>> [str(round(355/113, i)) for i in range(1, 6)]
['3.1', '3.14', '3.142', '3.1416', '3.14159']
'''


'''
嵌套列表解析
Python的列表还可以嵌套。

以下实例展示了3X4的矩阵列表：

>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]
以下实例将3X4的矩阵列表转换为4X3列表：

>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
以下实例也可以使用以下方法来实现：

>>> transposed = []
>>> for i in range(4):
...     transposed.append([row[i] for row in matrix])
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
另外一种实现方法：

>>> transposed = []
>>> for i in range(4):
...     # the following 3 lines implement the nested listcomp
...     transposed_row = []
...     for row in matrix:
...         transposed_row.append(row[i])
...     transposed.append(transposed_row)
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
'''


'''
列表推导式的执行顺序：各语句之间是嵌套关系，左边第二个语句是最外层，依次往右进一层，左边#第一条语句是最后一层。

[x*y for x in range[1,5] if x > 2 for y in range[1,4] if x < 3]
他的执行顺序是

for x in range[1,5]
    if x > 2
        for y in range[1,4]
            if x < 3
                x*y
'''


# 推导语句，应该先执行最右侧的 for，但是左侧的for用[]括起来，所以它的优先级提高了，会被先执行
matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]
[[print(row[i]) for row in matrix] for i in range(4)]
'''
关于嵌套列表解析，从左到右的for语句顺序对应的是从外到里的层次关系。上面有些笔记是用优先级来解析，这样是不太合理的，不便于理解。

最左侧的表达式可以直接使用后面出现的变量，而不是只限于相连的for，所以结合上面的结论。例子还可以写 [row[i] for i in range(4) for row in matrix]，效果一样。

例子为何不用()来改变嵌套的层次关系而用 []，因为 python 解析器会把 (row[i] for row in matrix) 解析为一个 生成器 generator。这里举一个例子

>>> (i for i in range(4))
<generator object <genexpr> at 0x110114360>
>>> [i for i in range(4)]
[0, 1, 2, 3]
>>> a = (i for i in range(4))
>>> next(a)
0
>>> next(a)
1
'''


# 以下例子，求最大数
N = int(input('输入需要对比大小数字的个数：\n'))

num=[ int(input('请输入第 %d 个对比数字 \n'%(i)))for i in range(1,N+1)]

# print('您输入的数字为:',list(num))
print('您输入的数字为:',num)
print('最大值为: ',max(num))


# 使用切片
mylist[start:end:step]
# mylist[::-1] 就能达到逆序的目的


