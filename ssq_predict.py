import requests
from bs4 import BeautifulSoup
from collections import Counter


# 双色球的分析
def parser():
    # 发送请求
    basic_url = "http://kaijiang.zhcw.com/zhcw/html/ssq/list_1.html"

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
    }

    response = requests.get(basic_url, headers=headers, timeout=10)
    response.encoding = "utf-8"
    html_response = response.text

    # 解析内容
    soup = BeautifulSoup(html_response, "html.parser")

    # 获取页面信息,总共页码数
    page = int(soup.find("p", attrs={"class": "pg"}).find_all("strong")[0].text)

    # url 前缀
    url_part = "http://kaijiang.zhcw.com/zhcw/html/ssq/list"

    red_num = []  # 红球
    blue_num = []  # 篮球

    # 分页的获取每一页开奖信息
    for index in range(1, page + 1):
        url = url_part + "_" + str(index) + ".html"  # 拼接url
        response_page = requests.get(url, headers=headers, timeout=10)
        response_page.encoding = "utf-8"
        context = response_page.text
        soups = BeautifulSoup(context, "html.parser")

        if soups.table is None:
            continue
        elif soups.table:
            table_rows = soups.table.find_all("tr")
            for row_num in range(2, len(table_rows) - 1):
                row_tds = table_rows[row_num].find_all("td")
                ems = row_tds[2].find_all("em")  # 只要双色球的数字

                # 把一行的数据结果都打印出来
                result = str(row_tds[0]) + "," + str(row_tds[1]) + "," + str(row_tds[2]) + "," + str(
                    row_tds[3]) + "," + str(row_tds[4]) + "," + str(row_tds[5]) + "," + str(row_tds[6])

                save_to_file(result)  # 保存文件

                # 红色的球,一个6个
                red_num.append(ems[0].string)
                red_num.append(ems[1].string)
                red_num.append(ems[2].string)
                red_num.append(ems[3].string)
                red_num.append(ems[4].string)
                red_num.append(ems[5].string)

                # 蓝色的球
                blue_num.append(ems[6].string)

        else:
            continue

    return red_num, blue_num


def save_to_file(content):
    with open("ssq.txt", "w", encoding="utf-8") as f:
        f.write(content + "\n")


def predict(red_num, blue_num):
    red_count = Counter(red_num)
    blue_count = Counter(blue_num)

    print("----------分割线----------")

    # 按照出现频率倒序
    red_sorted = sorted(red_count.items(), key=lambda x: x[1], reverse=True)
    blue_sorted = sorted(blue_count.items(), key=lambda x: x[1], reverse=True)

    red = red_sorted[0:6]
    blue = blue_sorted[0:3]

    red = list(map(lambda x: x[0], red))  # 这里不明白是什么意思?
    blue = list(map(lambda x: x[0], blue))

    red.sort()
    blue.sort()

    print("号码 -1 : " + str(red) + ", " + blue[0])
    print("号码 -2 : " + str(red) + ", " + blue[1])
    print("号码 -3 : " + str(red) + ", " + blue[2])

    print("--------------------------------------------")

    # 按照出现频率顺序
    red_sorted = sorted(red_count.items(), key=lambda x: x[1], reverse=False)
    blue_sorted = sorted(blue_count.update(), key=lambda x: x[1], reverse=False)

    red = red_sorted[0:6]
    blue = blue_sorted[0:3]

    red = list(map(lambda x: x[0], red))
    blue = list(map(lambda x: x[0], blue))

    red.sort()
    blue.sort()

    print("号码 -1 : " + str(red) + ", " + blue[0])
    print("号码 -2 : " + str(red) + ", " + blue[1])
    print("号码 -3 : " + str(red) + ", " + blue[2])


if __name__ == '__main__':
    red_num = []
    blue_num = []

    parser()
    predict(red_num, blue_num)
