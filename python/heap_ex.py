# _*_ coding: utf-8 _*_

from sort_helper import SortHelper


class Heap(object):
    """下标从 0 开始的堆 """
    def __init__(self):
        self.heap_list = []
        self.index = -1

    def insert(self, elem):
            self.heap_list.append(elem)
            self.index += 1


class MaxHeap(Heap):
    """大根堆"""
    def insert(self, elem):
        super(MaxHeap, self).insert(elem)
        self.shift_up(self.index)

    def shift_up(self, k):
        while k > 0 and self.heap_list[k] > self.heap_list[k / 2]:
            self.heap_list[k], self.heap_list[k / 2] = self.heap_list[k / 2], self.heap_list[k]
            k /= 2

    def shift_down(self, k):
        # assert self.index >= 0
        while 2 * k + 1 <= self.index:
            j = 2 * k + 1
            if j + 1 <= self.index and self.heap_list[j] < self.heap_list[j + 1]:
                j += 1
            if self.heap_list[k] > self.heap_list[j]:
                break
            self.heap_list[k], self.heap_list[j] = self.heap_list[j], self.heap_list[k]
            k = j

    def extract_max_elem(self):
        # assert self.index >= 0
        ret = self.heap_list[0]
        self.heap_list[self.index], self.heap_list[0] = self.heap_list[0], self.heap_list[self.index]
        self.index -= 1
        self.shift_down(0)
        return ret

    def heapify(self, arr):
        super(MaxHeap, self).__init__()
        self.heap_list.extend(arr)
        self.index = len(arr) - 1
        for e in range(self.index / 2, -1, -1):
            self.shift_down(e)


def heap_sort(arr):
    max_heap.heapify(arr)
    for i in range(len(arr)):
        arr[i] = max_heap.extract_max_elem()

if __name__ == "__main__":
    n = 1000000
    max_heap = MaxHeap()
    sort_helper = SortHelper()
    arr = sort_helper.gen_random_int_list(n, 1, n)
    sort_helper.test_time('heap_sort', heap_sort, arr)