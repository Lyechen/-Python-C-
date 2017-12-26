# _*_ coding: utf-8 _*_
import random


class ThreeBranchHeap(object):
    """
    三叉堆：
    1、每个节点都最多有三个子节点
    2、根元素大于子节点
    3、除最下一层之外,其它层数必须为满
    """
    def __init__(self):
        self.data = [0]
        self.count = 0

    def clear(self):
        self.data = [0]
        self.count = 0

    def insert(self, i, e):
        assert 0 < i + 1 <= self.count + 1
        self.data.append(e)
        self.count += 1
        self.shift_up(self.count)

    def shift_up(self, k):
        while 1 < k:
            if k % 3 == 2 and self.data[(k + 1)/3] < self.data[k]:
                self.data[(k + 1) / 3], self.data[k] = self.data[k], self.data[(k + 1) / 3]
                k = (k + 1) / 3
            elif k % 3 == 0 and self.data[k / 3] < self.data[k]:
                self.data[k / 3], self.data[k] = self.data[k], self.data[k / 3]
                k /= 3
            elif k % 3 == 1 and self.data[(k - 1)/3] < self.data[k]:
                self.data[(k - 1)/3], self.data[k] = self.data[k], self.data[(k - 1)/3]
                k = (k - 1)/3
            else:
                break

    def shift_down(self, k):
        while 0 < 3 * k - 1 <= self.count:
            j = 3 * k - 1
            if 3 * k < self.count and self.data[j] < self.data[3 * k]:
                j = 3 * k
            if 3 * k + 1 < self.count and self.data[j] < self.data[3 * k + 1]:
                j = 3 * k + 1
            if self.data[k] > self.data[j]:
                break
            self.data[k], self.data[j] = self.data[j], self.data[k]
            k = j

    def extract_max_elem(self):
        element = self.data[1]
        self.data[1], self.data[self.count] = self.data[self.count], self.data[1]
        self.count -= 1
        self.shift_down(1)
        return element


if __name__ == "__main__":
    three_branch_heap = ThreeBranchHeap()
    for i in range(20):
        three_branch_heap.insert(i, random.randint(1, 50))
    print three_branch_heap.data
    heap = []
    for i in range(20):
        heap.append(three_branch_heap.extract_max_elem())
    print heap
