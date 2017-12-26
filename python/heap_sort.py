# _*_ coding: utf-8 _*_
from sort_helper import SortHelper


def __shift_down(arr, n, k):
    while 2 * k + 1 < n:
        j = 2 * k + 1
        if j + 1 < n and arr[j] < arr[j + 1]:
            j += 1
        if arr[k] > arr[j]:
            break
        arr[k], arr[j] = arr[j], arr[k]
        k = j


def __heapify(arr, n):
    # 构建一个大根堆
    for i in range(len(arr) / 2 - 1, -1, -1):
        __shift_down(arr, n, i)
    # 对大根堆排序
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        __shift_down(arr, i, 0)


def heap_sort(arr):
    n = len(arr)
    __heapify(arr, n)


if __name__ == "__main__":
    n = 1000000
    sort_helper = SortHelper()
    arr = sort_helper.gen_random_int_list(n, 1, n)
    sort_helper.test_time('heap_sort', heap_sort, arr)
