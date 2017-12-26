# _*_ coding: utf-8 _*_
# import re
# import time
from sequence_search_table import SST
# from utils.util import store_file_to_obj
from queue import Queue


class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.lchild = None
        self.rchild = None
        self.child_nums = 0


class BST(object):
    def __init__(self):
        self.root = None
        self.count = 0

    def update(self, key, value):
        self.search(key).value = value
        return

    def insert(self, key, value):
        if self.contain(key):
            self.update(key, value)
            return
        # self.root = self.__insert(self.root, key, value)
        self.root = self._insert(self.root, key, value)

    def __insert(self, node, key, value):
        """使用递归方法实现"""
        if not node:
            self.count += 1
            _node = Node(key, value)
            _node.child_nums += 1
            return _node
        if node.key == key:
            node.value = value
        elif key < node.key:
            node.lchild = self.__insert(node.lchild, key, value)
            node.child_nums += 1
        else:
            node.rchild = self.__insert(node.rchild, key, value)
            node.child_nums += 1
        return node

    def _insert(self, node, key, value):
        """使用非递归方法实现"""
        if not node:
            self.count += 1
            _node = Node(key, value)
            _node.child_nums += 1
            return _node
        _node = node
        while True:
            if key < _node.key:
                _node.child_nums += 1
                if not _node.lchild:
                    self.count += 1
                    _node.lchild = Node(key, value)
                    _node.lchild.child_nums += 1
                    break
                else:
                    _node = _node.lchild
            elif key > _node.key:
                _node.child_nums += 1
                if not _node.rchild:
                    self.count += 1
                    _node.rchild = Node(key, value)
                    _node.rchild.child_nums += 1
                    break
                else:
                    _node = _node.rchild
            else:
                node.value = value
                break
        return node

    def search(self, key):
        node = self.__search(self.root, key)
        # a = self._search(self.root, key)
        return node

    def __search(self, node, key):
        """使用递归方法实现查找"""
        if not node:
            return None
        if node.key == key:
            return node
        if key > node.key:
            return self.__search(node.rchild, key)
        else:
            return self.__search(node.lchild, key)

    def _search(self, node, key):
        """使用非递归方法实现查找"""
        _node = node
        while True:
            if not _node:
                return None
            if key > _node.key:
                _node = _node.rchild
            elif key < _node.key:
                _node = _node.lchild
            else:
                return _node

    def contain(self, key):
        return True if self.__search(self.root, key) else False

    def per_order(self):
        """前序遍历"""
        self.__per_order(self.root)

    def __per_order(self, node):
        if node:
            print node.key,
            self.__per_order(node.lchild)
            self.__per_order(node.rchild)

    def in_order(self):
        """中序遍历"""
        self.__in_order(self.root)

    def __in_order(self, node):
        if node:
            self.__in_order(node.lchild)
            print node.key,
            self.__in_order(node.rchild)

    def post_order(self):
        """后序遍历"""
        self.__post_order(self.root)

    def __post_order(self, node):
        if node:
            self.__post_order(node.lchild)
            self.__post_order(node.rchild)
            print node.key,

    def level_order(self):
        """层序遍历,即广度优先遍历"""
        q = Queue()
        q.put(self.root)
        while not q.empty():
            _node = q.get()
            print _node.key,
            if _node.lchild:
                q.put(_node.lchild)
            if _node.rchild:
                q.put(_node.rchild)

    def minimum(self):
        """查找最小值"""
        assert self.count > 0
        node = self.__minimum(self.root)
        return node.key

    def __minimum(self, node):
        if not node.lchild:
            return node
        return self.__minimum(node.lchild)

    def maximum(self):
        """查找最大值"""
        assert self.count > 0
        node = self.__maximum(self.root)
        return node.key

    def __maximum(self, node):
        if not node.rchild:
            return node
        return self.__maximum(node.rchild)

    def remove_minimum(self):
        """删除最小值"""
        # 没有左右孩子的情况
        # 没有左孩子但是有又孩子的情况
        if self.root:
            self.root = self.__remove_minimum(self.root)
            # print 'new_root: ', self.root.key

    def __remove_minimum(self, node):
        if not node.lchild:
            new_node = node.rchild
            del node
            self.count -= 1
            return new_node
        node.lchild = self.__remove_minimum(node.lchild)
        node.child_nums -= 1
        return node

    def remove_maximum(self):
        """删除最大值"""
        if self.root:
            self.root = self.__remove_maximum(self.root)

    def __remove_maximum(self, node):
        if not node.rchild:
            new_node = node.lchild
            del node
            self.count -= 1
            return new_node
        node.rchild = self.__remove_maximum(node.rchild)
        node.child_nums -= 1
        return node

    def remove(self, key):
        node = self.contain(key)
        if node:
            self.root = self.__remove(self.root, key)
            # self.root = self._remove(self.root, key)

    def __remove(self, node, key):
        """通过查找 待删除 节点的后继实现 remove 操作"""
        if node.key == key:
            if not node.lchild:
                _node = node.rchild
                del node
                self.count -= 1
            elif not node.rchild:
                _node = node.lchild
                del node
                self.count -= 1
            else:
                _node = self.__minimum(node.rchild)
                _node.rchild = self.__remove_minimum(node.rchild)
                _node.lchild = node.lchild
                del node
            return _node
        elif key > node.key:
            node.child_nums -= 1
            node.rchild = self.__remove(node.rchild, key)
        else:
            node.child_nums -= 1
            node.lchild = self.__remove(node.lchild, key)
        return node

    def _remove(self, node, key):
        """通过查找 待删除 节点的前驱实现 remove 操作"""
        if node.key == key:
            if not node.lchild:
                _node = node.rchild
                del node
                self.count -= 1
            elif not node.rchild:
                _node = node.lchild
                del node
                self.count -= 1
            else:
                _node = self.__maximum(node.lchild)
                _node.lchild = self.__remove_maximum(node.lchild)
                _node.rchild = node.rchild
                del node
            return _node
        elif key > node.key:
            node.child_nums -= 1
            node.rchild = self._remove(node.rchild, key)

        else:
            node.child_nums -= 1
            node.lchild = self._remove(node.lchild, key)

        return node

    def successor(self, key):
        """查找一个节点的后继(特指在中序遍历中)"""
        node = self.search(key)
        _node = self.__minimum(node.rchild)
        return _node

    def predecessor(self, key):
        """查找一个节点的前驱(特指在中序遍历中)"""
        node = self.search(key)
        _node = self.__maximum(node.lchild)
        return _node

    def floor(self, key):
        """查找最接近 key并且小于 key的节点并将其返回"""
        if self.contain(key):
            return self.predecessor(key)
        return self.__floor(self.root, key)

    def __floor(self, node, key):
        if key > node.key:
            if not node.rchild:
                return node
            return self.__floor(node.rchild, key)
        else:
            if not node.lchild:
                return None
            return self.__floor(node.lchild, key)

    def ceil(self, key):
        """查找最接近 key并且大于 key的节点并将其返回"""
        if self.contain(key):
            return self.successor(key)
        return self.__ceil(self.root, key)

    def __ceil(self, node, key):
        if key > node.key:
            if not node.rchild:
                return None
            return self.__ceil(node.rchild, key)
        else:
            if not node.lchild:
                return node
            return self.__ceil(node.lchild, key)

    def rank(self, key):
        """查找 key 是在二叉树中排名第几的元素"""
        if self.contain(key):
            return self.__rank(self.root, key)
        return -1

    def __rank(self, node, key):
        if key > node.key:
            return self.__rank(node.rchild, key)
        elif key < node.key:
            return self.__rank(node.lchild, key)
        else:
            pass

    def select(self, rank):
        """查找 排名第 rank 名的元素"""
        pass

    def size(self):
        return self.count

    def is_empty(self):
        return self.count == 0


if __name__ == "__main__":
    bst = BST()
    sst = SST()
    bst.insert(42, 'a')
    # bst.insert(11, 'aaa')
    bst.insert(32, 'b')
    bst.insert(56, 'c')
    bst.insert(25, 'd')
    bst.insert(35, 'e')
    bst.insert(23, 'f')
    bst.insert(26, 'g')
    bst.insert(33, 'h')
    bst.insert(36, 'i')
    bst.insert(56, 'j')
    bst.insert(50, 'k')
    bst.insert(59, 'l')
    bst.insert(45, 'm')
    bst.insert(52, 'n')
    bst.insert(57, 'o')
    bst.insert(60, 'p')
    print bst.root.value
    # # print bst.root.lchild.key
    # # print bst.root.lchild.rchild.key
    print bst.count
    node = bst.search(35)
    if node:
        print 'node:', node.value
    else:
        print node
    print 'per_order: ',
    bst.per_order()
    print '\nin_order: ',
    bst.in_order()
    print '\npost_order: ',
    bst.post_order()
    print '\nlevel_order: ',
    bst.level_order()
    print '\nmaximum element: ', bst.maximum()
    print '\nchild_nums: ', bst.root.child_nums
    print '\nrank: ', bst.search(56).child_nums
    bst.remove(35)
    print '\nrank: ', bst.search(56).child_nums
    print '\nrank: ', bst.search(50).child_nums
    print '\nrank: ', bst.search(59).child_nums
    print '\nrank: ', bst.search(32).child_nums
    print '\nchild_nums: ', bst.root.child_nums
    # bst.remove_maximum()
    # print 'maximum element: ', bst.maximum()
    # bst.remove_maximum()
    # print 'maximum element: ', bst.maximum()
    # bst.remove_maximum()
    # print 'maximum element: ', bst.maximum()
    # bst.remove(56)
    # print 'per_order: ',
    # bst.per_order()
    # res = bst.ceil(61)
    # if res:
    #     print res.key
    # else:
    #     print res
    # pre = bst.predecessor(56)
    # if pre:
    #     print pre.key
    # 42 32 25 23 26 35 33 36 57 50 45 52 59 60
    # 42 32 25 23 26 35 33 36 56 50 45 52 59 60
    # print bst.count
    # print bst.root.value
    # print bst.contain(10)
    # start_time = time.clock()
    # count = 1  # 统计圣经中单词的个数
    # # 将bible.txt全部存入 二叉搜索树
    # store_file_to_obj('bible.txt', bst)
    # # with open('bible.txt', 'r') as f:
    # #     line = f.readline()
    # #     while line:
    # #         word_lists = re.findall(r"[\w]+", line)
    # #         for word in word_lists:
    # #             word = word.lower()
    # #             # bst: 二叉搜索树
    # #             res = bst.search(word)
    # #             if res:
    # #                 res.value += 1
    # #             else:
    # #                 bst.insert(word, 1)
    # #             count += 1
    # #         line = f.readline()
    # node = bst.search('god')
    # post_time = time.clock()
    # print '%s: %s' % ('god', node.value)
    # print 'BST: run out of %s s' % (post_time - start_time)

    # count_1 = 0
    # start_time_1 = time.clock()
    # # 将bible.txt全部存入 顺序搜索表
    # store_file_to_obj('bible.txt', sst)
    # # with open('bible.txt', 'r') as f:
    # #     line = f.readline()
    # #     while line:
    # #         word_lists = re.findall(r"[\w]+", line)
    # #         for word in word_lists:
    # #             word = word.lower()
    # #             # bst: 二叉搜索树
    # #             res = sst.search(word)
    # #             if res:
    # #                 res.value += 1
    # #             else:
    # #                 sst.insert(word, 1)
    # #             count_1 += 1
    # #         line = f.readline()
    # node_1 = sst.search('god')
    # post_time_1 = time.clock()
    # print '%s: %s' % ('god', node_1.value)
    # print 'SST: run out of %s s' % (post_time_1 - start_time_1)
