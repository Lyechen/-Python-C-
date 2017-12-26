# _*_ coding:utf-8 _*_
from sort_helper import SortHelper
import copy


def __merge(arr, l, mid, r):
    """
    对 待排序数组做 归并操作
    :param arr: 待排序数组
    :param l: 数组的 左边界
    :param mid: 数组的中间位置
    :param r: 数组的右边界
    :return:
    """
    aux = arr[l:r+1][:]
    i = l
    j = mid + 1
    for n in range(l, r+1):
        if i > mid:
            arr[n] = aux[j - l]
            j += 1
        elif j > r:
            arr[n] = aux[i - l]
            i += 1
        elif aux[i - l] > aux[j - l]:
            arr[n] = aux[j - l]
            j += 1
        else:
            arr[n] = aux[i - l]
            i += 1


def __merge_sort(arr, l, r):
    """

    :param arr: 待排序数组
    :param l: 数组的 左边界
    :param r: 数组的右边界
    :return:
    """
    if l >= r:
        return
    mid = (r + l) / 2
    __merge_sort(arr, l, mid)
    __merge_sort(arr, mid + 1, r)
    if arr[mid] > arr[mid + 1]:
        __merge(arr, l, mid, r)


def merge_sort(arr):
    """
    自顶向下的归并排序算法
    :param arr: 待排序数组
    :return:
    """
    n = len(arr)
    __merge_sort(arr, 0, n - 1)


def merge_sort_bu(arr):
    """
    自底向上的归并排序
    :param arr: 待排序数组
    :return:
    """
    n = len(arr)
    i = 1
    while i < n:
        j = 0
        # 对arr[i, j+i-1] 和 arr[j+i, j+i+i-1] 进行归并
        while j + i < n:
            if arr[j+i-1] > arr[j+i]:
                __merge(arr, j, j+i-1, min(j+i+i-1, n-1))
            j += i+i
        i += i


if __name__ == "__main__":
    sort_helper = SortHelper()
    arr = sort_helper.gen_random_int_list(1000000, 1, 1000000)
    arr_1 = copy.copy(arr)
    print id(arr), id(arr_1)
    sort_helper.test_time("merge_sort", merge_sort, arr)
    sort_helper.test_time("merge_sort_bu", merge_sort_bu, arr_1)
