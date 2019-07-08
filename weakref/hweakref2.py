# https://www.jianshu.com/p/33da60740d3b

import weakref

class Node(object):

    def __init__(self, data):
        self.data = data
        self._parent = None
        self.children = []

    @property
    def parent(self):
        return None if self._parent is None else self._parent()

    @parent.setter
    def parent(self, node):
        self._parent = weakref.ref(node, callback)

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

def callback(ref):
    print('__del__', ref)

n1 = Node(0)
n2 = Node(2)
print(n1,n2)
# <__main__.Node object at 0x7fb0c2750c10> <__main__.Node object at 0x7fb0c2750d10>
n1.add_child(n2)
del n1
# __del__ <weakref at 0x7fb0c26e75d0; dead>



# 不过，如果我们使用 weakref.ref() 创建弱引用，每次使用时都需要形如这样 xx() 来获取，有一点别扭。 可以通过 weakref.proxy() 这种来避免 () 操作。

n = Node(10)
p = weakref.proxy(n)
p.data
# 10