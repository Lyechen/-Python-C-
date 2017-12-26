# _*_ coding:utf-8 _*_
from select_sort import random_list


def insertion_sort(arr, n):
    for i in range(1, n):
        e = arr[i]
        suit_index = i
        for j in reversed(range(1, i+1)):
            if e < arr[j - 1]:
                arr[j] = arr[j - 1]
                suit_index = j - 1
        arr[suit_index] = e
    return arr

if __name__ == "__main__":
    test_list = random_list(10, 1, 100, "int")
    print "before sort: ", test_list
    sorted_list = insertion_sort(test_list, 10)
    print "after sort: ", sorted_list
