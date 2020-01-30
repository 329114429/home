import pandas
import numpy
import matplotlib.pyplot as plt
import codecs
import collections


def get_blue_ball():
    # 得到蓝色球
    ball_list = []
    file = codecs.open("lottery.txt", mode="r", encoding="utf-8")  # 打开txt文件

    line = file.readline()  # 以行形式进行读取
    while line:
        num_row = line.split()
        ball_blue = num_row[-1]
        # print(ball_blue)
        ball_list.append(ball_blue)
        line = file.readline()  # 读一行,最后一个数
    file.close()

    return ball_list


def analyze_blue_ball():
    # 分析蓝色球
    blue_ball_list = get_blue_ball()
    blue_ball_dict = collections.Counter(blue_ball_list)  # key, value 已经排好, 返回是字典

    blue_ball_sort = sorted(blue_ball_dict.items(), key=lambda x: x[0],
                            reverse=False)  # 对dict 按照value排序 True表示翻转 ,转为了列表形式

    x_blue = []
    y_blue = []

    for index in blue_ball_sort:
        x_blue.append(index[0])
        y_blue.append(index[1])

    x = x_blue
    y = y_blue

    fig, ax = plt.subplots()
    ax.barh(x, y, color="deepskyblue")
    labels = ax.get_xticklabels()
    plt.setp(labels, rotation=0)

    for a, b in zip(x, y):
        plt.text(b + 1, a, b, ha="center", va="center")
    ax.legend(["label"], loc="lower_right")

    # plt.rcParams["font.sans-serif"] = ["SimHei"]  # 用来正常显示中文标签
    plt.ylabel("num")
    plt.xlabel("counter")
    plt.rcParams['savefig.dpi'] = 300  # 图片像素
    plt.rcParams['figure.dpi'] = 300  # 分辨率
    plt.title("blue")
    plt.show()

    return blue_ball_sort


def get_red_ball():
    # 得到红球列表
    red_ball_list = []
    file = codecs.open("lottery.txt", mode="r", encoding="utf-8")

    line = file.readline()  # 读取一行
    while line:
        num_row = line.split()
        red_ball = num_row[:6]
        red_ball_list.append(red_ball)
        line = file.readline()
    file.close()

    return red_ball_list


def analyze_red_ball():
    # 分析红球
    red_ball_list = get_red_ball()
    red_ball_list_counter = numpy.array(red_ball_list)
    red_counter = collections.Counter(red_ball_list_counter.flatten())  # 默认按照行的方向降维,二维变成一维

    red_ball_sort = sorted(red_counter.items(), key=lambda x: x[1], reverse=False)  # 对dict 按照value排序 True表示翻转 ,转为了列表形式

    x_red = []
    y_red = []

    for index in red_ball_sort:
        x_red.append(index[0])
        y_red.append(index[1])

    x = x_red
    y = y_red

    plt.bar(x, y, color="red", tick_label=x, width=0.3, align='center')
    plt.xticks(x, x, size='small', rotation=90)

    plt.xlabel('num_ball')
    plt.ylabel('num_counter')
    plt.title("analyze_red_ball")

    # 设置数字标签
    for a, b in zip(x, y):
        plt.text(a, b + 2, '%.0f' % b, ha='center', va='bottom', fontsize=6)

    plt.show()

    return red_ball_sort


if __name__ == '__main__':
    # # balls = get_blue_ball()
    # a = analyze_blue_ball()
    # print(a)
    analyze_red_ball()
