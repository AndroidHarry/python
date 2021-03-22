
# -*- coding: UTF-8 -*-

'''
字典是另一种可变容器模型，且可存储任意类型对象。

字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中 ,格式如下所示：

d = {key1 : value1, key2 : value2 }
键必须是唯一的，但值则不必。

值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。

一个简单的字典实例：
'''


dict1 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print ("dict['Age']: ", dict1['Age'])
print ("dict['Class']: ", dict1.get('Class'))
#print ("dict['School']: ", dict['School'])


del dict1['Name'] # 删除键 'Name'
dict1.clear()     # 清空字典
# del dict         # 删除字典


# 键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行。


# 构造函数 dict() 直接从键值对元组列表中构建字典。如果有固定的模式，列表推导式指定特定的键值对：
d1 = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(d1)
# {'sape': 4139, 'jack': 4098, 'guido': 4127}

# 此外，字典推导可以用来创建任意键和值的表达式词典：
d2 = {x: x**2 for x in (2, 4, 6)}
print(d2)
# {2: 4, 4: 16, 6: 36}

# 如果关键字只是简单的字符串，使用关键字参数指定键值对有时候更方便：
d3 = dict(sape=4139, guido=4127, jack=4098)
print(d3)
# {'sape': 4139, 'jack': 4098, 'guido': 4127}


'''
Python字典包含了以下内置函数：

序号	函数及描述	实例
1	len(dict)
计算字典元素个数，即键的总数。	
>>> dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
>>> len(dict)
3
2	str(dict)
输出字典，以可打印的字符串表示。	
>>> dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
>>> str(dict)
"{'Name': 'Runoob', 'Class': 'First', 'Age': 7}"
3	type(variable)
返回输入的变量类型，如果变量是字典就返回字典类型。	
>>> dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
>>> type(dict)
<class 'dict'>
'''


'''
copy()方法
浅拷贝
'''
dict1 = {'user':'runoob','num':[1,2,3]}
dict2 = dict1 # 浅拷贝: 引用对象
dict3 = dict1.copy() # 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用
# 修改 data 数据
dict1['user']='root'
dict1['num'].remove(1)
# 输出结果
print(dict1)
print(dict2)
print(dict3)
'''
实例中 dict2 其实是 dict1 的引用（别名），所以输出结果都是一致的，dict3 父对象进行了深拷贝，不会随dict1 修改而修改，子对象是浅拷贝所以随 dict1 的修改而修改。

{'user': 'root', 'num': [2, 3]}
{'user': 'root', 'num': [2, 3]}
{'user': 'runoob', 'num': [2, 3]}
'''


'''
Python 字典 fromkeys() 函数用于创建一个新字典，以序列seq中元素做字典的键，value为字典所有键对应的初始值。
dict.fromkeys(seq[, value]))
'''
seq = ('name', 'age', 'sex')

dict = dict.fromkeys(seq)
print ("新的字典为 : %s" %  str(dict))

dict = dict.fromkeys(seq, 10)
print ("新的字典为 : %s" %  str(dict))


'''
Python 字典 get() 函数返回指定键的值，如果值不在字典中返回默认值。
dict.get(key, default=None)
'''
dict = {'Name': 'Runoob', 'Age': 27}

print ("Age 值为 : %s" %  dict.get('Age'))
print ("Sex 值为 : %s" %  dict.get('Sex', "NA"))


'''
Python 字典 items() 方法以列表返回可遍历的(键, 值) 元组数组。
dict.items()
'''
dict1 = {'Name': 'Runoob', 'Age': 7}
print ("Value : %s" %  dict1.items())

# 在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来：
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
# gallahad the pure
# robin the brave


'''
Python 字典 keys() 方法以列表返回一个字典所有的键。
dict.keys()
'''
dict = {'Name': 'Runoob', 'Age': 7}
print ("字典所有的键为 : %s" %  dict.keys())


'''
Python 字典 setdefault() 方法和get()方法类似, 如果键不已经存在于字典中，将会添加键并将值设为默认值。
dict.setdefault(key, default=None)
返回值
如果 key 在 字典中，返回对应的值。如果不在字典中，则插入 key 及设置的默认值 default，并返回 default ，default 默认值为 None。
'''
dict = {'Name': 'Runoob', 'Age': 7}

print ("Age 键的值为 : %s" %  dict.setdefault('Age', None))
print ("Sex 键的值为 : %s" %  dict.setdefault('Sex', None))
print ("新字典为：", dict)


'''
Python 字典 update() 函数把字典dict2的键/值对更新到dict里。
dict.update(dict2)
该方法没有任何返回值。
'''
dict = {'Name': 'Runoob', 'Age': 7}
dict2 = {'Sex': 'female' }
dict.update(dict2)
print ("更新字典 dict : ", dict)


'''
Python 字典 values() 方法以列表返回字典中的所有值。
dict.values()
返回字典中的所有值。
'''
dict = {'Sex': 'female', 'Age': 7, 'Name': 'Zara'}
print ("字典所有值为 : ",  list(dict.values()))


'''
popitem()
Python 字典 popitem() 方法随机返回并删除字典中的一对键和值(一般删除末尾对)。
如果字典已经为空，却调用了此方法，就报出KeyError异常。
返回一个键值对(key,value)形式。
'''
site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
pop_obj=site.popitem()
print(pop_obj)   
print(site)


'''
pop(key[,default])
Python 字典 pop() 方法删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
返回被删除的值。
'''
site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
pop_obj=site.pop('name')
print(pop_obj)
print(site)


citys={
    '北京':{
        '朝阳':['国贸','CBD','天阶','我爱我家','链接地产'],
        '海淀':['圆明园','苏州街','中关村','北京大学'],
        '昌平':['沙河','南口','小汤山',],
        '怀柔':['桃花','梅花','大山'],
        '密云':['密云A','密云B','密云C']
    },
    '河北':{
        '石家庄':['石家庄A','石家庄B','石家庄C','石家庄D','石家庄E'],
        '张家口':['张家口A','张家口B','张家口C'],
        '承德':['承德A','承德B','承德C','承德D']
    }
}
for i in citys['北京']:
    print(i)
    
for i in citys['北京']['海淀']:
    print(i)
    


params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
print(params.keys())
# ['server', 'uid', 'database', 'pwd']
print(params.values())
# ['mpilgrim', 'sa', 'master', 'secret']
print(params.items())
# [('server', 'mpilgrim'), ('uid', 'sa'), ('database', 'master'), ('pwd', 'secret')]
print([k for k, v in params.items()])
# ['server', 'uid', 'database', 'pwd']
print([v for k, v in params.items()])
# ['mpilgrim', 'sa', 'master', 'secret']
print(["%s=%s" % (k, v) for k, v in params.items()])
# ['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']


dict 构造函数
------------------
d={"a":1}
d2={'b':5}
d3=dict(d,**d2)
---------
d3
{'a': 1, 'b': 5}






