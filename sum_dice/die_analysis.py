from sum_dice.dice_sum import Die
import matplotlib.pyplot as plt


# 骰子分析
def die_analysis():
    die_6 = Die()

    two_result = []
    twice_face_times = []

    for i in range(3000):
        two_result.append(die_6.compute_add())  # 骰子 3000次, 把两次的结果加起来

    for i in range(2, 13):  # 2~12 出现的次数
        twice_face_times.append(two_result.count(i))  # 数元素的个数

    return two_result, twice_face_times


# 画柱状图
def bar_graph():
    two_result, twice_face_times = die_analysis()
    plt.figure(num='Twice')
    ax = plt.gca()

    # 设置有边框和头部边框颜色为空right、top、bottom、left
    ax.spines['top'].set_color('none')  # 边框的头部为空
    ax.spines['right'].set_color('none')

    x_axis = []
    for i in range(2, 13):
        x_axis.append(i)

    plt.bar(x_axis, twice_face_times, width=0.7, color="blue")

    for x, y in zip(x_axis, twice_face_times):
        plt.text(x - 0.2, y + 2, y)

    plt.title('Die_analysis')
    plt.xticks(x_axis)
    plt.show()


if __name__ == '__main__':
    bar_graph()
