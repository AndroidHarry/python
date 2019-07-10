# from .subpackage1.test11 import Test11
# from test11 import Test11

print("You have imported mypackage")

__all__ = ['subpackage1', 'subpackage2']    # harry, __all__ 关联了一个模块列表，当执行 from xx import * 时，就会导入列表中的模块。

print(__all__)
