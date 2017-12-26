# _*_ coding:utf-8 _*_
import copy
import time
from sort_helper import SortHelper


"""
求一个无序数组中的第 n 小的元素
思路一： 直接先对数组排序, 然后通过索引取第 n - 1, O(nlogN) 级别时间复杂度
思路二： 可以采用 快排 的思路, 实现一个 O(n) 级别的 时间复杂度
"""


def __get_partition(arr, l, r):
    v = arr[l]
    i = l + 1
    j = r
    while True:
        while i <= r and arr[i] < v:
            i += 1
        while j >= l + 1 and arr[j] > v:
            j -= 1
        if i > j:
            break
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    arr[l], arr[j] = arr[j], arr[l]
    return j


def __get_big_n_num(arr, l, r, m):
    """通过快排思路进行实现"""
    if l == r:
        return arr[l]
    p = __get_partition(arr, l, r)
    if m == p + 1:
        return arr[p]
    elif m < p:
        return __get_big_n_num(arr, l, p - 1, m)
    else:
        return __get_big_n_num(arr, p + 1, r, m)


def get_big_n_num(arr, m):
    """通过快排思路进行实现"""
    n = len(arr)
    return __get_big_n_num(arr, 0, n - 1, m)


def __get_big_n_num_1(arr, l, r):
    """通过快排思路进行实现"""
    if l >= r:
        return
    p = __get_partition(arr, l, r)
    __get_big_n_num_1(arr, l, p - 1)
    __get_big_n_num_1(arr, p + 1, r)


def get_big_n_num_1(arr, m):
    """通过先排序后取值的方式实现"""
    n = len(arr)
    m -= 1
    __get_big_n_num_1(arr, 0, n - 1)
    return arr[m]


if __name__ == "__main__":
    sort_helper = SortHelper()
    n = 1000000
    arr = sort_helper.gen_random_int_list(n, 1, n)
    arr_1 = copy.copy(arr)
    m = 10000
    start_time = time.clock()
    k = get_big_n_num(arr, m)
    end_time = time.clock()
    start_time_1 = time.clock()
    l = get_big_n_num_1(arr_1, m)
    end_time_1 = time.clock()
    print k
    print l
    print "get_big_n_num:", end_time - start_time
    print "get_big_n_num_1:", end_time_1 - start_time_1
