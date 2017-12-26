# _*_ coding: utf-8 _*_
"""
    二分查找法
    1、在有序序列中查找target
    2、如果有 target 则返回target的索引
    3、如果没有target，则返回 -1
"""


def binary_search(arr, n, target):
    # 在arr [l.......r]中查找元素 e
    l, r = 0, n - 1
    while l <= r:
        mid = l + (r - l) / 2
        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return -1


def __binary_search(arr, l, r, mid, target):
    if arr[mid] == target:
        return mid
    if arr[mid] > target:
        r = mid - 1
    else:
        l = mid + 1
    mid = l + (r - l) / 2
    return __binary_search(arr, l, r, mid, target)


def ex_binary_search(arr, n, target):
    """使用递归实现二分查找"""
    l, r = 0, n - 1
    mid = l + (r - l) / 2
    return __binary_search(arr, l, r, mid, target)


"""
    二分查找法的变种,floor和ceil
    floor: 如果target在目标序列中存在多个,那么使用floor方法我们得到的将是target第一次出现的值
    ceil: 对于带查找序列中有多个值为target的,那么使用ceil我们将得到的是target最后一次出现的索引的
"""


def floor(arr, n, target):
    # 在arr [l.......r]中查找元素 e
    l, r = 0, n - 1
    while l <= r:
        mid = l + (r - l) / 2
        if arr[mid] == target:
            r = mid
            if l + (r - l) / 2 == mid:
                return mid
            continue
        if arr[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return l - 1


def ceil(arr, n, target):
    # 在arr [l.......r]中查找元素 e
    l, r = 0, n - 1
    while l <= r:
        mid = l + (r - l) / 2
        if arr[mid] == target:
            l = mid
            if l + (r - l) / 2 == mid:
                return mid
            continue
        if arr[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return l


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 12, 12, 22, 23, 23, 23, 23, 56, 78]
    n = len(arr)
    # index = ex_binary_search(arr, n, 12)
    index = floor(arr, n, 79)
    print index
    print ceil(arr, n, 79)
