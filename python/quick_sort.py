# _*_ coding:utf-8 _*_
import random
import copy
from sort_helper import SortHelper
# import sys
#
# sys.setrecursionlimit(100000000)


def __partition(arr, l, r):
    """
    单路快排的核心，就是patition过程
    :param arr: 待排序数组
    :param l: 数组左边界值
    :param r: 数组右边界值
    :return:
    """
    tmp = random.randint(l, r)
    arr[l], arr[tmp] = arr[tmp], arr[l]
    v = arr[l]
    j = l
    i = l + 1
    while i <= r:
        if arr[i] < v:
            arr[j + 1], arr[i] = arr[i], arr[j + 1]
            j += 1
        i += 1
    arr[j], arr[l] = arr[l], arr[j]
    return j


def __quick_sort(arr, l, r):
    if l >= r:
        return
    p = __partition(arr, l, r)
    __quick_sort(arr, l, p - 1)
    __quick_sort(arr, p + 1, r)


def quick_sort(arr):
    """
    快速排序
    :param arr: 待排序数组
    :return:
    """
    n = len(arr)
    __quick_sort(arr, 0, n - 1)


def __partition_2(arr, l, r):
    """
    双路快排的核心，就是patition_2过程
    :param arr: 待排序数组
    :param l: 数组左边界值
    :param r: 数组右边界值
    :return:
    """
    tmp = random.randint(l, r)
    arr[l], arr[tmp] = arr[tmp], arr[l]
    v = arr[l]
    # arr [l+1....i) <= v, arr (i+1....r] >= v
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


def __quick_sort_2(arr, l, r):
    if l >= r:
        return
    p = __partition_2(arr, l, r)
    __quick_sort_2(arr, l, p - 1)
    __quick_sort_2(arr, p + 1, r)


def quick_sort_2(arr):
    """
    快速排序
    :param arr: 待排序数组
    :return:
    """
    n = len(arr)
    __quick_sort_2(arr, 0, n - 1)


def __partition_3(arr, l, r):
    """
    三路快排的核心，就是patition_3过程
    :param arr: 待排序数组
    :param l: 数组左边界值
    :param r: 数组右边界值
    :return:
    """
    tmp = random.randint(l, r)
    arr[l], arr[tmp] = arr[tmp], arr[l]
    v = arr[l]
    # arr [l+1....i) <= v, arr (i+1....r] >= v
    lt = l
    gt = r + 1
    i = l + 1
    while i < gt:
        if arr[i] < v:
            arr[i], arr[lt + 1] = arr[lt + 1], arr[i]
            lt += 1
            i += 1
        elif arr[i] > v:
            arr[i], arr[gt - 1] = arr[gt - 1], arr[i]
            gt -= 1
        else:
            i += 1
    arr[l], arr[lt] = arr[lt], arr[l]
    return lt, gt


def __quick_sort_3(arr, l, r):
    if l >= r:
        return
    lt, gt = __partition_3(arr, l, r)
    __quick_sort_3(arr, l, lt - 1)
    __quick_sort_3(arr, gt, r)


def quick_sort_3(arr):
    """
    快速排序
    :param arr: 待排序数组
    :return:
    """
    n = len(arr)
    __quick_sort_3(arr, 0, n - 1)


if __name__ == "__main__":
    sort_helper = SortHelper()
    n = 1000000
    arr = sort_helper.gen_random_int_list(n, 1, n)
    # arr = sort_helper.gen_random_nearly_order_int_list(1000000, 100)
    arr_1 = copy.copy(arr)
    arr_2 = copy.copy(arr)

    # 会出现递归到底的情况
    # sort_helper.test_time("quick_sort", quick_sort, arr)
    sort_helper.test_time("quick_sort_2", quick_sort_2, arr_1)
    sort_helper.test_time("quick_sort_3", quick_sort_3, arr_2)


