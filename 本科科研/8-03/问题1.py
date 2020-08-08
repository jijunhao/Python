"""
定义一个字典类：Dictclass。完成下面的功能：
1. 删除某个key
del_dict(key)
2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"
get_dict(key)
3 返回键组成的列表：返回类型;(list)
get_key()
4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)
update_dict({要合并的字典})
"""
class Dictclass(object):
    # 字典类
    def __init__(self,dict1):
        self.dict = dict1

    def del_dict(self,key):
        # 删除某个key
        if key in self.dict:
            del self.dict[key]
            return self.dict
        else:
            return "Key is not in dictclass."

    def get_dict(self,key):
        # 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"
        if key in self.dict:
            return self.dict[key]
        else:
            return "not found"

    def get_key(self):
        # 返回键组成的列表：返回类型;(list)
        return list(self.dict.keys())

    def update_dict(self,dict2):
        # 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)
        self.dict.update(dict2)
        return list(self.dict.values())

if __name__ == '__main__':
    A = Dictclass({'a': 1, 'b': 2})
    print(A.get_dict('c'))
    print(A.del_dict('c'))
    print(A.get_key())
    print(A.update_dict({'c': 3, 'd': 4}))