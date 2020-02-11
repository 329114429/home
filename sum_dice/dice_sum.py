from random import choice
import matplotlib.pyplot as plt
import numpy as np


# 两个骰子的和的概率, source_url = http://www.pianshen.com/article/7181253584/

class Die():
    # 一个骰子的属性
    def __init__(self, size=6):
        self.size = size

    # 返回每次点数的值
    def compute_add(self, times=2):
        if times <= 0:
            return 0
        else:
            faces = []
            result = 0
            for num in range(1, self.size + 1):
                faces.append(num)

            for time in range(times):
                ones_result = choice(faces)  # 选择列表的元素
                result += ones_result
            return result


