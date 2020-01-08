#!/usr/bin/env python
# -*- coding: utf-8 -*-

# curses 用来在终端上显示图形界面
import curses

# random 模块用来生成随机数
from random import choice, randrange

# collections 提供了一个字典的子类 defaultdict。可以指定 key 值不存在时，value 的默认值。
from collections import defaultdict

actions = ['Up', 'Down', 'Left', 'Right', 'Restart', 'Exit']

# ord() 函数以一个字符作为参数，返回参数对应的 ASCII 数值，便于和后面捕捉的键位关联
letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']

actions_dict = dict(zip(letter_codes, actions * 2))


def init():
    '''初始化游戏棋盘'''
    return 'Game'


def not_game(state):
    '''展示游戏结束界面。
            读取用户输入得到 action，判断是重启游戏还是结束游戏
            '''
    responses = defaultdict(lambda: state)
    responses['Restart'], responses['Exit'] = 'restart', 'exit'
    return responses[actions]
