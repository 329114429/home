import pandas as pd
import collections
import numpy as np


def test1():
    num = [[1, 2], [2, 3], [3, 4]]
    num1, num2 = max(num, key=lambda x: x[0])
    print(num1, num2)


def test2():
    list2 = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
    a = np.array(list2)
    a_counter = collections.Counter(a.flatten())
    print(a_counter)


if __name__ == '__main__':
    test2()
