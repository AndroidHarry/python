# class DataBase:
#     '''Python 3 中的类'''
#
#     def __init__(self, id, address):
#         '''初始化方法'''
#         self.id = id
#         self.address = address
#         self.d = {self.id: 1,
#                   self.address: "192.168.1.1",
#                   }
#
#     def __getitem__(self, key):
#         # return self.__dict__.get(key, "100")
#         return self.d.get(key, "default")
#
#
# data = DataBase(1, "192.168.2.11")
# print(data["hi"])
# print(data[data.id])


# class DataBase:
#     '''Python 3 中的类'''
#
#     def __init__(self, id, address):
#         '''初始化方法'''
#         self.id = id
#         self.address = address
#
#     def __getitem__(self, key):
#         return self.__dict__.get(key, "100")
#
#
# data = DataBase(1, "192.168.2.11")
# print(data["hi"])
# print(data["id"])



class STgetitem:
    def __init__(self, text):
        self.text = text

    def __getitem__(self, index):
        result = self.text[index].upper()
        return result


p = STgetitem("黄哥Python")
print(p[0])
print("------------------------")
for char in p:
    print(char)

