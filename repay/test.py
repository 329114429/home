from datetime import datetime


def test_datetime():
    d = "2020-2-12"
    year_s, mon, day = d.split("-")

    a = datetime(int(year_s), int(mon), int(day))

    b = 0.05 * 0.01
    print(b)


# 两次循环,一个一个加入内存
def chain(*iterables):
    for it in iterables:
        for element in it:
            yield element


# 拼接元素 迭代器
def test_chain():
    char = list(chain(['i', 'love'], ['you']))
    print(char)
    return char


if __name__ == '__main__':
    # test_datetime()
    test_chain()
