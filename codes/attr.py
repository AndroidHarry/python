class A(object):
    def __init__(self, value):
        print("into __init__")
        self.value = value

    def __setattr__(self, name, value):
        print("into __setattr__")
        if value == 10:
            print("from __init__")
        object.__setattr__(self, name, value)


a = A(10)
# into __init__
# into __setattr__
# from __init__
print(a.value)
# 10
a.value = 100
# into __setattr__
print(a.value)
# 100
# ————————————————
# 版权声明：本文为CSDN博主「yusuiyu」的原创文章，遵循CC
# 4.0
# BY - SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https: // blog.csdn.net / yusuiyu / article / details / 87945149
