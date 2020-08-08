"""
定义一个集合的操作类：Setinfo
包括的方法:
1 集合元素添加: add_setinfo(keyname) [keyname:字符串或者整数类型]
2 集合的交集：get_intersection(unioninfo) [unioninfo :集合类型]
3 集合的并集： get_union(unioninfo)[unioninfo :集合类型]
4 集合的差集：del_difference(unioninfo) [unioninfo :集合类型]
"""
class Setinfo(object):
    # 集合操作类
    def __init__(self,set1):
        self.set = set1

    def add_setinfo(self, keyname):
        # 集合元素添加: add_setinfo(keyname) [keyname:字符串或者整数类型]
        if isinstance(keyname, (str, int)):
            self.set.add(keyname)
            return self.set

    def get_intersection(self, unioninfo):
        # 集合的交集：get_intersection(unioninfo) [unioninfo :集合类型]
        if isinstance(unioninfo, set):
            a = self.set & (unioninfo)
            return a

    def get_union(self, unioninfo):
        # 集合的并集： get_union(unioninfo)[unioninfo :集合类型]
        if isinstance(unioninfo, set):
            a = self.set | (unioninfo)
            return a

    def del_difference(self, unioninfo):
        # 集合的差集：del_difference(unioninfo) [unioninfo :集合类型]
        if isinstance(unioninfo, set):
            a = self.set - (unioninfo)
            return a

if __name__ == '__main__':
    A = set([1, 2, 3, 4, 5, 2])
    B = set([5, 6, 3])
    set_info = Setinfo(A)
    print(set_info.add_setinfo('f'))
    print(set_info.get_intersection(B))
    print(set_info.get_union(B))
    print(set_info.del_difference(B))