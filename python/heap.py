# _*_ coding: utf-8 _*_
import random
import time
from sort_helper import SortHelper


class Heap(object):
    def __init__(self):
        self.heap_list = [0]  # 元素从 下标 1 开始插入,下标 0 采用 0 进行占位
        self.index = 0

    def insert(self, elem):
        self.heap_list.append(elem)
        self.index += 1

    # def print_heap(self):
    #     n = len(self.heap_list)
    #     max_level = 0
    #     number_per_level = 1
    #     while n > 0:
    #         max_level += 1
    #         n -= number_per_level
    #         number_per_level *= 2
    #     max_level_number = pow(2, max_level - 1)
    #     cur_tree_max_level_number = max_level_number
    #     index = 1
    #     level = 0
    #     while level < max_level:
    #         line_1 = ' ' * (max_level_number * 3 - 1)
    #         cur_level_number = min(self.index - pow(2, level) + 1, pow(2, level))
    #         is_left = True
    #         index_cur_level = 0
    #         while index_cur_level < cur_level_number:
    #             self.putNumberInLine(self.heap_list[index], line_1, index_cur_level,
    #                                  (cur_tree_max_level_number * 3 - 1), is_left)
    #             is_left = not is_left
    #             index_cur_level += 1
    #         print line_1
    #         if level == max_level - 1:
    #             break
    #         line_2 = ' ' * (max_level_number * 3 - 1)
    #         index_cur_level = 0
    #         while index_cur_level < cur_level_number:
    #             self.putBranchInLine(line_2, index_cur_level, cur_tree_max_level_number * 3 - 1)
    #             index_cur_level += 1
    #         print line_2
    #         cur_tree_max_level_number /= 2
    #
    # def putNumberInLine(self, num, line_1, index_cur_level, cur_tree_width, isLeft):
    #     sub_tree_width = (cur_tree_width - 1) / 2
    #     offset = index_cur_level * (cur_tree_width + 1) + sub_tree_width
    #     assert (offset + 1 < len(line_1))
    #     if num >= 10:
    #         line_1[offset + 0] = (num / 10)
    #         line_1[offset + 1] = (num % 10)
    #     else:
    #         if isLeft:
    #             line_1[offset + 0] = num
    #         else:
    #             line_1[offset + 1] = num
    #
    # def putBranchInLine(self, line_2, index_cur_level, cur_tree_width):
    #     sub_tree_width = (cur_tree_width - 1) / 2
    #     sub_sub_tree_width = (sub_tree_width - 1) / 2
    #     offset_left = index_cur_level * (cur_tree_width + 1) + sub_sub_tree_width
    #     assert (offset_left + 1 < len(line_2))
    #     offset_right = index_cur_level * (cur_tree_width + 1) + sub_tree_width + 1 + sub_sub_tree_width
    #     assert (offset_right < len(line_2))
    #     line_2[offset_left + 1] = '/'
    #     line_2[offset_right + 0] = '\\'


class MaxHeap(Heap):
    """大根堆"""
    def insert(self, elem):
        super(MaxHeap, self).insert(elem)
        self.shift_up(self.index)

    def shift_up(self, k):
        while k > 1 and self.heap_list[k] > self.heap_list[k/2]:
            self.heap_list[k], self.heap_list[k/2] = self.heap_list[k/2], self.heap_list[k]
            k /= 2

    def shift_down(self, k):
        assert self.index >= 0
        while 2 * k <= self.index:
            j = 2 * k
            if j + 1 <= self.index and self.heap_list[j] < self.heap_list[j + 1]:
                j += 1
            if self.heap_list[k] > self.heap_list[j]:
                break
            self.heap_list[k], self.heap_list[j] = self.heap_list[j], self.heap_list[k]
            k = j

    def extract_max_elem(self):
        assert self.index >= 0
        ret = self.heap_list[1]
        self.heap_list[self.index], self.heap_list[1] = self.heap_list[1], self.heap_list[self.index]
        # self.heap_list.remove(self.heap_list[-1])
        self.index -= 1
        # self.heap_list[-1], self.heap_list[1] = self.heap_list[1], self.heap_list[-1]
        self.shift_down(1)
        return ret

    def heapify(self, arr):
        super(MaxHeap, self).__init__()
        self.heap_list.extend(arr)
        self.index = len(arr)
        for e in range(self.index / 2, 0, -1):
            self.shift_down(e)


class MinHeap(Heap):
    """小根堆"""
    def insert(self, elem):
        super(MinHeap, self).insert(elem)
        self.shift_up(self.index)

    def shift_up(self, k):
        while k > 1 and self.heap_list[k] < self.heap_list[k/2]:
            self.heap_list[k], self.heap_list[k/2] = self.heap_list[k/2], self.heap_list[k]
            k /= 2

    def extract_min_elem(self):
        assert self.index >= 0
        ret = self.heap_list[1]
        self.heap_list[self.index], self.heap_list[1] = self.heap_list[1], self.heap_list[self.index]
        self.index -= 1
        self.shift_down(1)
        return ret

    def shift_down(self, k):
        assert self.index >= 0
        while 2 * k <= self.index:
            j = 2 * k
            if j + 1 <= self.index and self.heap_list[j + 1] < self.heap_list[j]:
                j += 1
            if self.heap_list[k] < self.heap_list[j]:
                break
            self.heap_list[k], self.heap_list[j] = self.heap_list[j], self.heap_list[k]
            k = j

    def heapify(self, arr):
        super(MinHeap, self).__init__()
        self.heap_list.extend(arr)
        self.index = len(arr)
        for e in range(self.index / 2, 0, -1):
            self.shift_down(e)


def heap_sort_simply(obj, random_list, sort_type="increase"):
    for elem in random_list:
        obj.insert(elem)
    assert sort_type in ['increase', 'reverse']
    if sort_type == "increase":
        sorted_list = [obj.extract_min_elem() for i in range(0, len(random_list))]
    else:
        sorted_list = [obj.extract_max_elem() for i in range(0, len(random_list))]
    return sorted_list


def heap_sort_middle(obj, random_list, sort_type="increase"):
    obj.heapify(random_list)
    if sort_type == "increase":
        sorted_list = [obj.extract_min_elem() for i in range(0, len(random_list))]
    else:
        sorted_list = [obj.extract_max_elem() for i in range(0, len(random_list))]
    return sorted_list


if __name__ == "__main__":
    n = 1000000
    max_heap = MaxHeap()

    min_heap = MinHeap()
    sort_helper = SortHelper()
    random_list = sort_helper.gen_random_int_list(n, 1, n)
    random_list_1 = random_list[:]
    random_list_2 = random_list[:]
    random_list_3 = random_list[:]
    random_list_4 = random_list[:]
    # print random_list
    # for elem in random_list:
    #     max_heap.insert(elem)
    # for elem in random_list_1:
    #     min_heap.insert(elem)
    start_time = time.clock()
    random_list_1 = heap_sort_simply(min_heap, random_list_1)
    end_time = time.clock()
    assert sort_helper.is_sort(random_list_1)
    print 'heap_sort_simply', ":", end_time - start_time, "s"
    # random_list_1 = heap_sort_simply(max_heap, random_list_1, 'reverse')
    # random_list_2 = heap_sort_simply(min_heap, random_list_2)

    sort_helper = SortHelper()
    start_time = time.clock()
    random_list_3 = heap_sort_middle(min_heap, random_list_3)
    end_time = time.clock()
    assert sort_helper.is_sort(random_list_3)
    print 'heap_sort_simply', ":", end_time - start_time, "s"

    # random_list_3 = heap_sort_middle(max_heap, random_list_3, 'reverse')
    # random_list_4 = heap_sort_middle(min_heap, random_list_4)

    # print random_list_1
    # print random_list_2
    # print random_list_3
    # print random_list_4
    # print "MaxHeap:", max_heap.heap_list
    # print "MinHeap:", min_heap.heap_list
    # print [max_heap.extract_max_elem() for i in range(0, len(random_list))]
    # print [min_heap.extract_min_elem() for i in range(0, len(random_list_1))]
    # heap_sort(random_list_2)
    # print max_heap.print_heap()
