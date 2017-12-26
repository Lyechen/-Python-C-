# _*_ coding: utf-8 _*_


class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next_child = None


class SST(object):
    """顺序搜索表"""
    def __init__(self):
        self.head = None
        self.count = 0

    def insert(self, key, value):
        self.head = self._insert(self.head, key, value)

    def __insert(self, node, key, value):
        """递归方法实现"""
        if not node:
            self.count += 1
            return Node(key, value)
        if key == node.key:
            node.value = value
        else:
            node.next_child = self.__insert(node.next_child, key, value)
        return node

    def _insert(self, node, key, value):
        """使用循环方法实现"""
        if not node:
            self.count += 1
            return Node(key, value)
        t_node = node
        while True:
            if key == node.key:
                node.value = value
                break
            else:
                if not node.next_child:
                    node.next_child = Node(key, value)
                    self.count += 1
                    break
                else:
                    node = node.next_child
        return t_node

    def search(self, key):
        # return self.__search(self.head, key)
        return self._search(self.head, key)

    def __search(self, node, key):
        """迭代方式实现"""
        if not node:
            return None
        if node.key == key:
            return node
        else:
            return self.__search(node.next_child, key)

    def _search(self, node, key):
        """使用循环的方法实现"""
        t_node = node
        while True:
            if not t_node:
                return None
            if t_node.key == key:
                return t_node
            else:
                t_node = t_node.next_child

    def contain(self, key):
        return True if self.__search(self.head, key) else False

    def size(self):
        return self.count

    def is_empty(self):
        return True if not self.head else False


if __name__ == "__main__":
    sst = SST()
    sst.insert(11, 'a')
    sst.insert(11, 'aaa')
    sst.insert(9, 'b')
    sst.insert(12, 'c')
    sst.insert(10, 'd')
    sst.insert(13, 'e')
    print sst.head.value
    node = sst.search(12)
    if node:
        print node.value
    else:
        print None
