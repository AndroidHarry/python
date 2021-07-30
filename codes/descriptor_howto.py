
# In general, a descriptor is an attribute value that has one of the methods in the descriptor protocol. Those methods
# are __get__(), __set__(), and __delete__(). If any of those methods are defined for an attribute, it is
# said to be a descriptor.

# descr.__get__(self, obj, type=None) -> value
# descr.__set__(self, obj, value) -> None
# descr.__delete__(self, obj) -> None

# If an object defines __set__() or __delete__(), it is considered a data descriptor. Descriptors that only define
# __get__() are called non-data descriptors (they are often used for methods but other uses are possible).

# To use the descriptor, it must be stored as a class variable in another class.
# Descriptors only work when used as class variables. When put in instances, they have no effect.

# Descriptors get invoked by the dot “operator” during attribute lookup.
# If a descriptor is accessed indirectly with vars(some_class)[descriptor_name], the descriptor instance is returned without invoking it.

# Descriptors are used throughout the language. It is how functions turn into bound methods. Common tools like
# classmethod(), staticmethod(), property(), and functools.cached_property() are all
# implemented as descriptors.


################    demo1     ################
# import os
#
# # The self parameter is size, an instance of DirectorySize. The obj parameter is either g or s, an instance of
# # Directory. It is the obj parameter that lets the __get__() method learn the target directory. The objtype parameter
# # is the class Directory.
#
# class DirectorySize:
#     # obj: 这个 descriptor 所在类的实例
#     # objtype: obj 的类型
#     def __get__(self, obj, objtype = None):
#         return len(os.listdir(obj.dirname))
#
#
# class Directory:
#     size = DirectorySize()  # Descriptor instance
#
#     def __init__(self, dirname):
#         self.dirname = dirname # Regular instance attribute


# >>> s = Directory('songs')
# >>> g = Directory('games')
# >>> s.size # The songs directory has twenty files
# 20
# >>> g.size # The games directory has three files
# 3
# >>> os.remove('games/chess') # Delete a game
# >>> g.size # File count is automatically updated
# 2
################   end demo1     ################


################    demo2     ################

# import logging
#
# logging.basicConfig(level=logging.INFO)
#
# # class LoggedAgeAccess:
# #     def __get__(self, obj, objtype=None):
# #         value = obj._age
# #         logging.info('Accessing %r giving %r', 'age', value)
# #         return value
# #
# #     def __set__(self, obj, value):
# #         logging.info('Updating %r to %r', 'age', value)
# #         obj._age = value
# #
# #
# # class Person:
# #     age = LoggedAgeAccess()     # Descriptor instance
# #
# #     def __init__(self, name, age):
# #         self.name = name    # Regular instance attribute
# #         self.age = age      # Calls __set__()
# #
# #     def birthday(self):
# #         self.age += 1       # Calls both __get__() and __set__()
#
#
# class LoggedAccess:
#     def __set_name__(self, owner, name):
#         self.public_name = name
#         self.private_name = '_' + name
#
#     def __get__(self, obj, objtype=None):
#         value = getattr(obj, self.private_name)
#         logging.info('Accessing %r giving %r', self.public_name, value)
#         return value
#
#     def __set__(self, obj, value):
#         logging.info('Updating %r to %r', self.public_name, value)
#         setattr(obj, self.private_name, value)
#
#
# class Person:
#     name = LoggedAccess() # First descriptor instance
#     age = LoggedAccess() # Second descriptor instance
#
#     def __init__(self, name, age):
#         self.name = name # Calls the first descriptor
#         self.age = age # Calls the second descriptor
#
#     def birthday(self):
#         self.age += 1
#
#
# mary = Person('Mary M', 30)

################   end demo2     ################


################    demo3     ################

# from abc import ABC, abstractmethod
#
#
# class Validator(ABC):
#     def __set_name__(self, owner, name):
#         self.private_name = '_' + name
#
#     def __get__(self, obj, objtype=None):
#         return getattr(obj, self.private_name)
#
#     def __set__(self, obj, value):
#         self.validate(value)
#         setattr(obj, self.private_name, value)
#
#     @abstractmethod
#     def validate(self, value):
#         pass
#
#
# class OneOf(Validator):
#     def __init__(self, *options):
#         self.options = set(options)
#
#     def validate(self, value):
#         if value not in self.options:
#             raise ValueError(f'Expected {value!r} to be one of {self.options!r}')
#
#
# class Number(Validator):
#     def __init__(self, minvalue=None, maxvalue=None):
#         self.minvalue = minvalue
#         self.maxvalue = maxvalue
#
#     def validate(self, value):
#         if not isinstance(value, (int, float)):
#             raise TypeError(f'Expected {value!r} to be an int or float')
#         if self.minvalue is not None and value < self.minvalue:
#             raise ValueError(
#                 f'Expected {value!r} to be at least {self.minvalue!r}'
#             )
#             if self.maxvalue is not None and value > self.maxvalue:
#                 raise ValueError(
#                     f'Expected {value!r} to be no more than {self.maxvalue!r}'
#                 )
#
#
# class String(Validator):
#     def __init__(self, minsize=None, maxsize=None, predicate=None):
#         self.minsize = minsize
#         self.maxsize = maxsize
#         self.predicate = predicate
#
#     def validate(self, value):
#         if not isinstance(value, str):
#             raise TypeError(f'Expected {value!r} to be an str')
#         if self.minsize is not None and len(value) < self.minsize:
#             raise ValueError(
#                 f'Expected {value!r} to be no smaller than {self.minsize!r}'
#             )
#         if self.maxsize is not None and len(value) > self.maxsize:
#             raise ValueError(
#                 f'Expected {value!r} to be no bigger than {self.maxsize!r}'
#             )
#         if self.predicate is not None and not self.predicate(value):
#             raise ValueError(
#                 f'Expected {self.predicate} to be true for {value!r}'
#             )
#
#
# class Component:
#     name = String(minsize=3, maxsize=10, predicate=str.isupper)
#     kind = OneOf('wood', 'metal', 'plastic')
#     quantity = Number(minvalue=0)
#
#     def __init__(self, name, kind, quantity):
#         self.name = name
#         self.kind = kind
#         self.quantity = quantity


# >>> Component('Widget', 'metal', 5) # Blocked: 'Widget' is not all uppercase
# Traceback (most recent call last):
# ...
# ValueError: Expected <method 'isupper' of 'str' objects> to be true for 'Widget'
# >>> Component('WIDGET', 'metle', 5) # Blocked: 'metle' is misspelled
# Traceback (most recent call last):
# ...
# ValueError: Expected 'metle' to be one of {'metal', 'plastic', 'wood'}
# >>> Component('WIDGET', 'metal', -5) # Blocked: -5 is negative
# Traceback (most recent call last):
# ...
# ValueError: Expected -5 to be at least 0
# >>> Component('WIDGET', 'metal', 'V') # Blocked: 'V' isn't a number
# Traceback (most recent call last):
# ...
# TypeError: Expected 'V' to be an int or float
# >>> c = Component('WIDGET', 'metal', 5) # Allowed: The inputs are valid

################   end demo3     ################



################    demo4     ################

class Field:
    def __set_name__(self, owner, name):
        self.fetch = f'SELECT {name} FROM {owner.table} WHERE {owner.key}=?;'
        self.store = f'UPDATE {owner.table} SET {name}=? WHERE {owner.key}=?;'

    def __get__(self, obj, objtype=None):
        # return conn.execute(self.fetch, [obj.key]).fetchone()[0]
        print('conn.execute(', self.fetch, [obj.key], ').fetchone()[0]')

    def __set__(self, obj, value):
        print('conn.execute(', self.store, [value, obj.key], ')')
        # conn.execute(self.store, [value, obj.key])
        # conn.commit()


class Movie:
    table = 'Movies'    # Table name
    key = 'title'       # Primary key
    director = Field()
    year = Field()

    def __init__(self, key):
        self.key = key


class Song:
    table = 'Music'
    key = 'title'
    artist = Field()
    year = Field()
    genre = Field()

    def __init__(self, key):
        self.key = key



################   end demo4     ################



print('end')
