
'''
很多类都倾向于将对象创建为有初始状态的。因此类可能会定义一个名为 __init__() 的特殊方法（构造方法），像下面这样：

def __init__(self):
    self.data = []


self代表类的实例，而非类
类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。
self 不是 python 关键字，我们把他换成 runoob 也是可以正常执行的:
'''

class MyClass:
    """一个简单的类实例"""
    i = 12345
    
    def __init__(self, data):
        self.data = data

    def f(self):
        return 'hello world', self.data
    
    def prt(self):
        print(self)
        print(self.__class__)
    
# 实例化类
x = MyClass([1,2,3])
# 访问类的属性和方法
print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类的方法 f 输出为：", x.f())
x.prt()



#类定义
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
        
    def speak(self):
        print("%s 说: 我 %d 岁，体重 %d 公斤。" %(self.name,self.age,self.__weight))
        
# 实例化类
p = people('runoob',10,30)
p.speak()



'''
继承
Python 同样支持类的继承，如果一种语言不支持继承，类就没有什么意义。派生类的定义如下所示:

class DerivedClassName(BaseClassName1):
<statement-1>
.
.
.
<statement-N>
需要注意圆括号中基类的顺序，若是基类中有相同的方法名，而在子类使用时未指定，python从左至右搜索 即方法在子类中未找到时，从左到右查找基类中是否包含方法。

BaseClassName（示例中的基类名）必须与派生类定义在一个作用域内。除了类，还可以用表达式，基类定义在另一个模块中时这一点非常有用:

class DerivedClassName(modname.BaseClassName):
'''

#单继承示例
class student(people):
    grade = ''
    
    def __init__(self,n,a,w,g):
        #调用父类的构函
        people.__init__(self,n,a,w)
        self.grade = g
        
    #覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))
        
s = student('ken',10,60,3)
s.speak()




'''
多继承
Python同样有限的支持多继承形式。多继承的类定义形如下例:

class DerivedClassName(Base1, Base2, Base3):
<statement-1>
.
.
.
<statement-N>
需要注意圆括号中父类的顺序，若是父类中有相同的方法名，而在子类使用时未指定，python从左至右搜索 即方法在子类中未找到时，从左到右查找父类中是否包含方法。
'''


#另一个类，多重继承之前的准备
class speaker():
    topic = ''
    name = ''
    
    def __init__(self,n,t):
        self.name = n
        self.topic = t
        
    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))

#多重继承
class sample(speaker,student):
    a =''
    
    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)

test = sample("Tim",25,80,4,"Python")
test.speak() #方法名同，默认调用的是在括号中排前的父类的方法



'''
方法重写
如果你的父类方法的功能不能满足你的需求，你可以在子类重写你父类的方法，实例如下：
'''
class Parent: # 定义父类
    def myMethod(self):
        print ('调用父类方法')
        
class Child(Parent): # 定义子类
    def myMethod(self):
        print ('调用子类方法')
        
c = Child() # 子类实例
c.myMethod() # 子类调用重写方法
# super() 函数是用于调用父类(超类)的一个方法。
super(Child,c).myMethod() #用子类对象调用父类已被覆盖的方法



'''
类属性与方法
类的私有属性
__private_attrs：两个下划线开头，声明该属性为私有，不能在类地外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。

类的方法
在类地内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self，且为第一个参数，self 代表的是类的实例。

self 的名字并不是规定死的，也可以使用 this，但是最好还是按照约定是用 self。

类的私有方法
__private_method：两个下划线开头，声明该方法为私有方法，只能在类的内部调用 ，不能在类地外部调用。self.__private_methods。
'''

class JustCounter:
    __secretCount = 0 # 私有变量
    publicCount = 0 # 公开变量
    
    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print (self.__secretCount)
        
counter = JustCounter()
counter.count()
counter.count()
print (counter.publicCount)
# print (counter.__secretCount) # 报错，实例不能访问私有变量



class Site:
    def __init__(self, name, url):
        self.name = name # public
        self.__url = url # private
        
    def who(self):
        print('name : ', self.name)
        print('url : ', self.__url)
        
    def __foo(self): # 私有方法
        print('这是私有方法')
        
    def foo(self): # 公共方法
        print('这是公共方法')
        self.__foo()
        
x = Site('菜鸟教程', 'www.runoob.com')
x.who() # 正常输出
x.foo() # 正常输出
# x.__foo() # 报错



'''
类的专有方法：
__init__ : 构造函数，在生成对象时调用
__del__ : 析构函数，释放对象时使用
__repr__ : 打印，转换
__setitem__ : 按照索引赋值
__getitem__: 按照索引获取值 https://www.cnblogs.com/MY0213/p/7884166.html (harry: 普通方法,key可以是字符串; 迭代时,只能是整形索引.)
__len__: 获得长度
__cmp__: 比较运算
__call__: 函数调用 https://www.jianshu.com/p/e1d95c4e1697 (harry: 如果在类中实现了 __call__ 方法，那么实例对象也将成为一个可调用对象.)
__add__: 加运算
__sub__: 减运算
__mul__: 乘运算
__div__: 除运算
__mod__: 求余运算
__pow__: 乘方
'''

# Python同样支持运算符重载，我们可以对类的专有方法进行重载

class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)
    
    def __add__(self,other):
        return Vector(self.a + other.a, self.b + other.b)
    
v1 = Vector(2,10)
v2 = Vector(5,-2)
print (v1 + v2)

'''
* 我们可以使用 __str__ 和 __repr__ 方法定义类到字符串的转化方式，而不需要手动打印某些属性或是添加额外的方法。

* 一般来说，__str__ 的返回结果在于强可读性，而 __repr__ 的返回结果在于准确性。

* 我们至少需要添加一个 __repr__ 方法来保证类到字符串的自定义转化的有效性，__str__ 是可选的。因为默认情况下，在需要却找不到 __str__ 方法的时候，会自动调用 __repr__ 方法。

def __repr__(self):
    return '{}({!r},{!r})'.format(self.__class__.__name__, self.color, self.mileage)
注意，我们这里用了 !r 标记，是为了保证 self.color 与 self.mileage 在转化为字符串的时候使用 repr(self.color) 和 repr(self.mileage) ，而不是 str(self.color) 和 str(self.mileage) 。
使用对象的 __class__.__name__ 属性，该属性总代表着类的名称。
'''


'''
python __nonzero__方法
类的nonzero方法用于将类转换为布尔值。通常在用类进行判断和将类转换成布尔值时调用。比如语句if A: print 'foo'中就会调用A.nonzero()来判断。下面这个程序应该能帮助你理解nonzero的作用。

class A:
  def __nonzero__(self):
    print 'A._nonzero__()'
    return True

print 'A is not zero' if A() else 'A is zero'
print bool(A())
output：

A._nonzero__()
A is not zero
A._nonzero__()
True


def __bool__(self):
        return self.__nonzero__()
'''



