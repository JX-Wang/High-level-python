#! encoding:utf-8
"""
排序算法总结
===========
Auth@Wangjunxiong
Data@2019/09/11
"""


def bubble_sort(array):
    """
    时间复杂度O(n^2)
    缺点：低效，需要的交换次数非常多
    优点：稳定
    :param array:
    :return: sorted array

    """
    for _ in range(len(array)):
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
            else:
                pass
        print array
    return array


def select_sort(array):
    """
    时间复杂度O(n^2)
    缺点：时间复杂度也是O(n^2)
    优点：是冒泡排序的优化
    :param array:
    :return: sorted array
    """
    for i, num in enumerate(array):
        for j, m in enumerate(array[i+1:]):
            if num > m:
                array[i], array[i+j+1] = array[i+j+1], array[i]
            else:
                pass
    return array


def insert_sort(array):
    """
    时间复杂度O(n^2)
    缺点：
    优点：
    :param array:
    :return: sorted array
    """
    if not array:
        return
    rst = []
    while array:
        tmp = array.pop()
        if rst == []:
            rst.append(tmp)
        else:
            flag = 0
            for i, num in enumerate(rst):
                if num > tmp:
                    rst.insert(i, tmp)
                    flag = 1
                    break
                else:pass
            if not flag:
                rst.append(tmp)
    return rst


def quick_sort(array):
    pass


def heap_sort(array):
    pass


def shell_sort(array):
    pass


def merge_sort(array):
    pass


def count_sort(array):
    pass


def bucket_sort(array):
    pass


def radix_sort(array):
    pass


if __name__ == '__main__':
    array = [3, 4, 2, 5, 1, 6, 9, 8, 7]
    print insert_sort(array)
