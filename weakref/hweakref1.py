# https://www.jianshu.com/p/33da60740d3b

import gc

class Node(object):

    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def __del__(self):
        print('__del__',self,self.data)

n = Node(0)
del n
# __del__
n1 = Node(1)
n2 = Node(2)
n1.add_child(n2)
del n1 # no output
print(n2.parent)
del n2
# <__main__.Node at 0x7fd87ad5c250>

# 双亲节点的指针指向孩子节点，孩子节点又指向双亲节点。这构成了循环引用，所以每个对象的引用计数都不可能变成 0 。


print('--------------------------')

n11 = Node(11)
n12 = Node(12)
print(n11, n12)
# <__main__.Node object at 0x7f94109906d0> <__main__.Node object at 0x7f9410990610>
n11.add_child(n12)
del n11
del n12
print('after del n11, n12')
gc.collect()
# 64
print('gc collected.')
gc.garbage
# [<__main__.Node object at 0x7f94109906d0> <__main__.Node object at 0x7f9410990610>]
