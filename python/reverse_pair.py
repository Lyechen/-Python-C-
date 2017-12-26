# _*_coding:utf-8 _*_
import time
import copy
from sort_helper import SortHelper

"""
求逆序对
"""


def statistic_reverse_pair(arr):
    """最简单的思路，复杂度为 n^2"""
    i = 0
    cn = 0
    while i < len(arr):
        j = i + 1
        while j < len(arr):
            if arr[i] > arr[j]:
                cn += 1
            j += 1
        i += 1
    return cn

cn = 0


def __adv_statistic_merge(arr, l, mid, r):
    aux = arr[l:r+1]
    i = l
    j = mid + 1
    n = l
    while n <= r:
        if i > mid:
            arr[n] = aux[j - l]
            j += 1
        elif j > r:
            arr[n] = aux[i - l]
            i += 1
        elif aux[i - l] < aux[j - l]:
            arr[n] = aux[i - l]
            i += 1
        else:
            arr[n] = aux[j - l]
            global cn
            cn += mid - i + 1
            j += 1
        n += 1


def __adv_statistic_reverse_pair(arr, l, r):
    if l >= r:
        return
    mid = (r + l) / 2
    __adv_statistic_reverse_pair(arr, l, mid)
    __adv_statistic_reverse_pair(arr, mid + 1, r)
    __adv_statistic_merge(arr, l, mid, r)


def adv_statistic_reverse_pair(arr):
    """采用归并算法的思路"""
    n = len(arr)
    __adv_statistic_reverse_pair(arr, 0, n - 1)

if __name__ == "__main__":
    helper = SortHelper()
    n = 100000
    arr = helper.gen_random_int_list(n, 1, n)
    arr_1 = copy.copy(arr)
    # start_time = time.clock()
    # cn_1 = statistic_reverse_pair(arr)
    # end_time = time.clock()
    strart_time_1 = time.clock()
    adv_statistic_reverse_pair(arr)
    end_time_1 = time.clock()
    # print "statistic_reverse_pair: ", end_time - start_time
    print "adv_statistic_reverse_pair: ", end_time_1 - strart_time_1
