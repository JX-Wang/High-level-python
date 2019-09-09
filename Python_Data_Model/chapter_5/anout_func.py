# def fact(n) -> int:
#     """
#     this is a doc about this func
#     :param n:
#     :return: int n
#     """
#     return 1 if n < 2 else n * fact(n-1)
#
#
# print(fact.__doc__)
# print(fact(42))
# print(list(map(fact, range(6))))

# fruits = ['aa', 'ab', 'ac', 'ah', 'az', 'af', 'ae']
# rst = sorted(fruits, key=lambda r: r[::-1])
# print(rst)

import random


# class BingoCage:
#     def __init__(self, items):
#         self._items = list(items)
#         random.shuffle(self._items)
#
#     def pick(self):
#         try:
#             return self._items.pop()
#         except IndexError:
#             raise LookupError('pick from e B')
#
#     def __call__(self, *args, **kwargs):
#             return self.pick()
#
#
# b = BingoCage(range(3))
# print(b.pick())
# print(callable(b))

# def t(name, age, b, c, **exp):
#         print(exp)
#         return 1
#
#
# i = {'name': 'wud',
#      'age': 22,
#      'b': 'b',
#      'c': 'c',
#      'collage': 'harbin institute of technology'
# }
#
#
# t(**i)
# def d(func):
#     def inner():
#         print('running %s' % func)
#     return inner
#
# @d
# def taget():
#     print("running target")
#
# taget()
# print (taget)
# a = [1, 2, 3]
# b = [1, 2, 3]
# print(a.__eq__(b))
# import threading
# import time
#
#
# def run():
#     i = 0
#     print('Now thread is : ' + threading.current_thread().name)
#     for _ in range(100000000):
#         i += 1
#
# def start():
#
#     start = time.time()
#     thread_list = []
#     for i in range(5):
#         t = threading.Thread(target=run, name="thread_%d" % i)
#         thread_list.append(t)
#         t.start()
#
#     for t in thread_list:
#         t.join()
#
#     print("Total time:", time.time() - start)
#
#
# if __name__ == '__main__':
#     start()
