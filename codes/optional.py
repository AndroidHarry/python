
from typing import Optional


# def foo_v2(a: int, b: Optional[int] = None):
def foo_v2(a: int, b: Optional[int] = 1):
    if b:
        print(a + b)
    else:
        print("parameter b is a NoneType!")


#   只传入a位置的实参
foo_v2(2)

# # 输出
# >>> parameter b is a NoneType!
# ————————————————
# 版权声明：本文为CSDN博主「秋墓」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/qq_44683653/article/details/108990873