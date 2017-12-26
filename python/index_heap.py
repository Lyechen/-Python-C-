# _*_ coding: utf-8 _*_
import random


class IndexMaxHeap(object):
    """ 索引堆 """
    def __init__(self):
        """初始化索引堆"""
        self.data = [0]
        self.indexes = [0]
        self.count = 0
        self.reverse = [0]

    def clear(self):
        """清理索引堆"""
        self.data = [0]
        self.indexes = [0]
        self.count = 0
        self.reverse = [0]

    def is_empty(self):
        """查看索引堆是否为空"""
        return len(self.data) == 1

    def size(self):
        """返回索引堆的尺寸"""
        return len(self.data) - 1

    def insert(self, i, e):
        """向索引堆中插入元素,并保持索引堆的性质"""
        self.data.append(e)
        assert self.count + 1 <= len(self.data) - 1
        assert 0 <= i + 1 <= len(self.data)
        i += 1
        self.data[i] = e
        self.indexes.append(i)
        self.reverse.append(0)
        self.reverse[i] = self.count + 1
        self.count += 1
        self.shift_up(self.count)

    def shift_up(self, k):
        """以 k  为堆底向上形成索引堆"""
        while k > 1 and self.data[self.indexes[k / 2]] < self.data[self.indexes[k]]:
            # self.data[k / 2], self.data[k] = self.data[k], self.data[k / 2]
            # 只需要交换索引即可
            self.indexes[k / 2], self.indexes[k] = self.indexes[k], self.indexes[k / 2]
            self.reverse[self.indexes[k / 2]] = k / 2
            self.reverse[self.indexes[k]] = k
            k /= 2

    def shift_down(self, k):
        """以 k 为堆顶向下排序形成索引堆"""
        while 2 * k <= self.count:
            j = 2 * k
            if j + 1 <= self.count and self.data[self.indexes[j]] < self.data[self.indexes[j + 1]]:
                j += 1
            if self.data[self.indexes[k]] > self.data[self.indexes[j]]:
                break
            self.indexes[k], self.indexes[j] = self.indexes[j], self.indexes[k]
            self.reverse[self.indexes[k]] = k
            self.reverse[self.indexes[j]] = j
            k = j

    def exec_max_ele(self):
        """删除堆顶元素"""
        index = self.indexes[1]
        self.indexes[1], self.indexes[self.count] = self.indexes[self.count], self.indexes[1]
        self.reverse[self.indexes[1]] = 1
        self.reverse[self.count] = 0
        self.count -= 1
        self.shift_down(1)
        return self.data[index]

    def exec_max_index(self):
        """删除堆顶元素的索引"""
        assert self.count > 0
        index = self.indexes[1] - 1
        self.indexes[1], self.indexes[self.count] = self.indexes[self.count], self.indexes[1]
        self.reverse[self.indexes[1]] = 1
        self.reverse[self.count] = 0
        self.count -= 1
        self.shift_down(1)
        return index

    def get_element(self, index):
        """获取堆中指定下标的元素"""
        assert self.is_contain(index)
        return self.data[index + 1]

    def change(self, k, e):
        """
        索引堆相对于一般对最大的优点是可以在O(1)的时间复杂度内实现将一个堆中元素的值改变
        :param k: 需要改变的堆中的下标
        :param e: 改变后的值
        :return:
        """
        assert self.is_contain(k)
        k += 1
        self.data[k] = e
        # 方法一: 时间复杂度为O(n)
        # for i in range(1, self.count + 1):
        #     if self.indexes[i] == k:
        #         self.shift_up(i)
        #         self.shift_down(i)
        #         return
        # 方法二: 通过 reverse[k] 直接定位到需要进行 shift_up和shift_down操作的下标
        j = self.reverse[k]
        self.shift_down(j)
        self.shift_up(j)

    def is_contain(self, k):
        """判断索引是否合理"""
        assert 0 < k + 1 <= self.count
        if self.reverse[k + 1] != 0:
            return True
        else:
            return False


if __name__ == "__main__":
    index_max_heap = IndexMaxHeap()
    init_list = [0]
    for i in range(30):
        index_max_heap.insert(i, random.randint(1, 50))
        init_list.append(index_max_heap.data[i + 1])
    # print init_list
    print index_max_heap.data
    # heap_list = [0]
    # for i in range(30):
    #     heap_list.append(index_max_heap.data[index_max_heap.indexes[i + 1]])
    # print heap_list
    # sort_list = []
    # for i in range(30):
    #     sort_list.append(index_max_heap.exec_max_ele())
    # print sort_list
    print [i for i in range(0, len(index_max_heap.indexes))]
    print index_max_heap.indexes
    print index_max_heap.reverse
