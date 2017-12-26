# _*_ coding:utf-8 _*_
import time
import random


class SortHelper(object):
    def __init__(self):
        self.start_time = 0
        self.end_time = 0
        self.random_list = []

    def test_time(self, func_name, func, arg_lists):
        """
        测试一个排序算法的 排序过程 所需的时间
        :param func_name: 排序函数名
        :param func: 排序函数
        :param arg_lists: 参数列表
        :return:
        """
        self.start_time = time.clock()
        func(arg_lists)
        self.end_time = time.clock()
        assert self.is_sort(arg_lists)
        print func_name, ":", self.end_time - self.start_time, "s"

    def gen_random_int_list(self, n, rangeL, rangeR):
        """
        生成一个随机的 整型数组
        :param n: 列表长度
        :param rangeL: 随机整数数组的左边界值
        :param rangeR: 随机整数数组的右边界值
        :return: 长度为 n 的随机列表
        """
        for i in range(0, n):
            self.random_list.append(random.randint(rangeL, rangeR + 1))
        return self.random_list

    def gen_random_nearly_order_int_list(self, n, swap_times):
        """
        生成一个 近乎有序 的整型数组
        :param n: 列表长度
        :param swap_times: 交换次数
        :return: 长度为 n 的随机列表
        """
        for i in range(1, n + 1):
            self.random_list.append(i)
        for i in range(0, swap_times + 1):
            posX = random.randint(0, n-1)
            posY = random.randint(0, n - 1)
            self.random_list[posX], self.random_list[posY] = self.random_list[posY], self.random_list[posX]
        return self.random_list

    def is_sort(self, arr):
        """
        判断一个数组是否有序
        :param arr: 待判断的数组
        :return: bool值,True代表为排序好的数组,False代表未排序好的数组
        """
        is_sort = False
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                is_sort = False
                break
            is_sort = True
        if not is_sort:
            for i in range(1, len(arr)):
                if arr[i] < arr[i - 1]:
                    is_sort = False
                    break
                is_sort = True
        return is_sort
