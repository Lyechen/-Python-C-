# _*_ coding:utf-8 _*_
import random

seed = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpKkRrSsTtUuVvWwXxYyZz"
name_length = 5


def gen_random_list(n, rangeL, rangeR, data_type):
    """
    :param n: 列表长度
    :param rangeL: 随机数组的左边界值
    :param rangeR: 随机数组的右边界值
    :param data_type: 随机数组的数据类型 int, float, char
    :return: 长度为 n 的随机列表
    """
    assert data_type in ["int", "float", "char"]
    return gen_dict[data_type](n, rangeL, rangeR)


def gen_random_int_list(n, rangeL, rangeR):
    """
    :param n: 列表长度
    :param rangeL: 随机整数数组的左边界值
    :param rangeR: 随机整数数组的右边界值
    :return: 长度为 n 的随机列表
    """
    random_list = []
    for i in range(0, n):
        random_list.append(random.randint(rangeL, rangeR + 1))
    return random_list


def gen_random_float_list(n, rangeL, rangeR):
    """
    :param n: 生成对象的个数
    :param rangeL: 生成的随机小数列表的 左边界
    :param rangeR: 生成的随机小数的列表右边界
    :return: 长度为 n 的随机列表
    """
    random_list = []
    for i in range(0, n):
        random_list.append(random.uniform(rangeL, rangeR + 1))
    return random_list


def gen_random_char_list(n, rangeL, rangeR):
    """
    :param n: 生成对象的个数
    :param rangeL:
    :param rangeR:
    :return: 长度为 n 的随机列表
    """
    random_list = []
    for i in range(0, n):
        random_list.append(random.choice(seed))
    return random_list


def gen_random_object_list(n, rangeL, rangeR):
    """
    :param n: 生成对象的个数
    :param rangeL: 对象 score 属性值 的 左边界
    :param rangeR: 对象 score 属性值 的 右边界
    :return: 长度为 n 的随机列表
    """
    name = ''
    score = random.randint(rangeL, rangeR + 1)
    random_list = []
    for i in range(0, name_length):
        name += random.choice(seed)
    for i in range(0, n):
        random_list.append(Student(name, score))
    return random_list


gen_dict = {
    "int": gen_random_int_list,
    "float": gen_random_float_list,
    "char": gen_random_char_list,
}


def select_sort(unsort_list):
    """该方法除了可以对 整数、小数、字符串进行排序外，他还可以对对象进行排序"""
    length = len(unsort_list)
    for i in range(0, length):
        min_index = i
        for j in range(i + 1, length):
            """找出 [i+1, n] 范围内最小的数，且其值也满足小于 i """
            if unsort_list[min_index] > unsort_list[j]:
                min_index = j

        unsort_list[i], unsort_list[min_index] = unsort_list[min_index], unsort_list[i]
    return unsort_list


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __gt__(self, other):
        return True if self.score > other.score else False

    def __lt__(self, other):
        return True if self.score < other.score else False

    def __str__(self):
        return "Student: " + self.name + ", Score: " + str(self.score)


if __name__ == "__main__":
    test_list = gen_random_list(10, 1, 100, "int")
    print "before sort: ", test_list
    sorted_list = select_sort(test_list)
    print "after sort: ", sorted_list
    print "=" * 30
    test_list_1 = gen_random_list(10, 1, 100, "float")
    print "before sort: ", test_list_1
    sorted_list_1 = select_sort(test_list_1)
    print "after sort: ", sorted_list_1
    print "=" * 30
    test_list_2 = gen_random_list(10, 'A', 'z', "char")
    print "before sort: ", test_list_2
    sorted_list_2 = select_sort(test_list_2)
    print "after sort: ", sorted_list_2
    print "=" * 30
    # 对对象进行排序
    """其实为了统一，也可以构造一个方法用来生成随机对象"""
    A = Student('Bob', 90)
    B = Student('Li', 92)
    C = Student('King', 92)
    D = Student('Deny', 85)
    E = Student('Kong', 98)
    test_list_3 = [A, B, C, D, E]
    for i in test_list_3:
        print "before sort: ", i, " "
    print "=" * 30
    sorted_list_3 = select_sort(test_list_3)
    for i in test_list_3:
        print "after sort: ", i, " "
