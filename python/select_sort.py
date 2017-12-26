# _*_ coding:utf-8 _*_
import random

seed = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpKkRrSsTtUuVvWwXxYyZz"


def random_list(n, rangeL, rangeR, data_type):
    """
    :param n: 列表长度
    :param rangeL: 随机数组的左边界值
    :param rangeR: 随机数组的右边界值
    :param data_type: 随机数组的数据类型 int float or char
    :return:
    """
    assert data_type in ["int", "float", "char"]
    random_list = []
    for i in range(0, n):
        if data_type == "int":
            random_list.append(random.randint(rangeL, rangeR + 1))
        elif data_type == "float":
            random_list.append(random.uniform(rangeL, rangeR + 1))
        elif data_type == "char":
            random_list.append(random.choice(seed))
    return random_list


def select_sort(unsort_list):
    length = len(unsort_list)
    for i in range(0, length):
        min_index = i
        for j in range(i + 1, length):
            """找出 [i+1, n] 范围内最小的数，且其值也满足小于 i """
            if unsort_list[min_index] > unsort_list[j]:
                min_index = j

        unsort_list[i], unsort_list[min_index] = unsort_list[min_index], unsort_list[i]
    return unsort_list


if __name__ == "__main__":
    test_list = random_list(10, 1, 100, "int")
    print "before sort: ", test_list
    sorted_list = select_sort(test_list)
    print "after sort: ", sorted_list

    test_list_1 = random_list(10, 1, 100, "float")
    print "before sort: ", test_list_1
    sorted_list_1 = select_sort(test_list_1)
    print "after sort: ", sorted_list_1

    test_list_2 = random_list(10, 'A', 'z', "char")
    print "before sort: ", test_list_2
    sorted_list_2 = select_sort(test_list_2)
    print "after sort: ", sorted_list_2
