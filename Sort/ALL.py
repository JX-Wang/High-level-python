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
                else:
                    pass
            if not flag:
                rst.append(tmp)
    return rst


def quick_sort(array):
    pass


def max_heapify(heap, HeapSize, root):  # 在堆中做结构调整使得父节点的值大于子节点

    left = 2*root + 1
    right = left + 1
    larger = root
    if left < HeapSize and heap[larger] < heap[left]:
        larger = left
    if right < HeapSize and heap[larger] < heap[right]:
        larger = right
    if larger != root:  # 如果做了堆调整则larger的值等于左节点或者右节点的，这个时候做对调值操作
        heap[larger], heap[root] = heap[root], heap[larger]
        max_heapify(heap, HeapSize, larger)


def build_max_heap(heap):  # 构造一个堆，将堆中所有数据重新排序
    HeapSize = len(heap)  # 将堆的长度单独拿出来方便
    for i in xrange((HeapSize - 2)//2, -1, -1):  # 从后往前出数
        max_heapify(heap, HeapSize, i)


def heap_sort(heap):  # 将根节点取出与最后一位做对调，对前面len-1个节点继续进行对调整过程。
    build_max_heap(heap)
    for i in range(len(heap)-1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        max_heapify(heap, i, 0)
    return heap


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
    print heap_sort(array)
