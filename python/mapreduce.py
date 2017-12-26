# _*_ coding: utf-8 _*_
import gzip
import time
import os
import glob
import collections
import itertools
import operator
import multiprocessing


class AdMapReduce(object):
    def __init__(self, map_func, reduce_func, num_workers=None):
        """
            num_workers: 不指定就是默认可用cpu的核数
            map_func: map函数: 要求返回格式类似:[(a, 1), (b, 3)]
            reduce_func: reduce函数: 要求返回格式类似: (c, 10)
        """
        self.map_func = map_func
        self.reduce_func = reduce_func
        self.pool = multiprocessing.Pool(num_workers)

    def partition(self, mapped_values):
        partitioned_data = collections.defaultdict(list)
        for key, value in mapped_values:
            partitioned_data[key].append(value)
        return partitioned_data.items()

    def __call__(self, inputs, chunksize=1):
        """
            调用类的时候被触发
        """
        # 其实都是借用multiprocessing.Pool.map这个函数, inputs是一个需要处理的列表,想想map函数
        # chunksize表示每次给mapper的量, 这个根据需求调整效率
        map_responses = self.pool.map(self.map_func, inputs, chunksize=chunksize)
        # itertools.chain是把mapper的结果链接起来为一个可迭代的对象
        partitioned_data = self.partition(itertools.chain(*map_responses))
        # 大家想,上面的就是[(a, [1,2]), (b, [2,3]),列表中的数就是当时符合的次数,reduce就是吧列表符合项sum
        reduced_values = self.pool.map(self.reduce_func, partitioned_data)
        return reduced_values


def mapper_match(one_file):
    """
        第一次的map函数,从每个文件里面获取符合的条目
    """
    output = []
    # for line in gzip.open(one_file).readlines():
    for line in open(one_file).readlines():
        l = line.rstrip().split(',')
        if int(l[20]) == 16309 and int(l[22]) == 2656:
            cookie = l[1]
            output.append((cookie, 1))
    return output


def reduce_match(item):
    """
        第一次的reduce函数,给相同的key做统计
    """
    cookie, occurances = item
    return (cookie, sum(occurances))


def mapper_count(item):
    """
        第二次mapper函数,其实就是把某key的总数做键,但是值标1
    """
    _, count = item
    return [(count, 1)]


def reduce_count(item):
    """
         第二次reduce函数
    """
    freq, occurances = item
    return (freq, sum(occurances))


if __name__ == '__main__':
    start = time.time()
    # input_files = glob.glob('/datacenter/input/2013-12-1[01]/*')
    input_files = glob.glob('E:\algo')
    # input_files = glob.glob('./data.txt')
    mapper = AdMapReduce(mapper_match, reduce_match)
    cookie_feq = mapper(input_files)
    mapper = AdMapReduce(mapper_count, reduce_count)
    cookie_feq = mapper(cookie_feq)
    cookie_feq.sort(key=operator.itemgetter(1))
    for freq, count in cookie_feq:
        print '{0}\t{1}\t{2}'.format(freq, count, freq * count)
    # cookie_feq.reverse()
    end = time.time()
    print 'cost:', end - start