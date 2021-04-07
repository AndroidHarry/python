
# https://www.cnblogs.com/omg-hxy/p/9081177.html
# python中，在形参前面加上“*”与“”“**”，称为动态参数
# 加“*”时，函数可接受任意多个参数，全部放入一个元组中
# 加“**”时，函数接受参数时，返回为字典

### !!! 对于 list, *list 返回列表里的每个元素 !!! ###
### !!! 对于 dict, *dict 返回 dict 里所有的 key, **dict 返回 dict 里所有的 key=value 对. 参见 FKey 例子 !!! ###


'''
Python: 什么是*args和**kwargs (https://www.cnblogs.com/zhangzhuozheng/p/8053045.html)
---------------------------------
可以看到，这两个是python中的可变参数。*args表示任何多个无名参数，它是一个tuple；**kwargs表示关键字参数，它是一个dict。
并且同时使用*args和**kwargs时，必须*args参数列要在**kwargs前，像foo(a=1, b='2', c=3, a', 1, None, )这样调用的话，
会提示语法错误“SyntaxError: non-keyword arg after keyword arg”。

呵呵，知道*args和**kwargs是什么了吧。还有一个很漂亮的用法，就是创建字典：
    def kw_dict(**kwargs):
        return kwargs
    print kw_dict(a=1,b=2,c=3) == {'a':1, 'b':2, 'c':3}
其实python中就带有dict类，使用dict(a=1,b=2,c=3)即可创建一个字典了。
'''

'''
Python | 动态参数的使用
https://www.jianshu.com/p/c0ce45122849

深入理解python的 *args 和**kwargs 可变参数
https://www.jianshu.com/p/037b6ea516f1
'''


######################################

def F(*args):
    print(args)

F(123,"456")

# (123, '456')


######################################


def F(**kwargs):
    print(kwargs)

F(k1=123,k2="456")

# {'k1': 123, 'k2': '456'}


######################################


def F(p,*args,**kwargs):
    print(p)
    print(args)
    print(kwargs)

F(11,"abc",[789],k1=123,k2="456")

# 11
# ('abc', [789])
# {'k1': 123, 'k2': '456'}


######################################


def F(*args):
    print(args)

li = [11,22,33,44]
F(li)
F(*li)

# ([11, 22, 33, 44],)
# (11, 22, 33, 44)


######################################


def F(**kwargs):
    print(kwargs)

li = {"k1":1,"k2":2}
F(k=li)
F(**li)

# {'k': {'k2': 2, 'k1': 1}}
# {'k2': 2, 'k1': 1}


######################################


def FKey(*args,**kwargs):
    print(kwargs)
    print(args)

li = {"k1":1,"k2":2}

FKey(*li)

# {}
# ('k1', 'k2')

