import requests
from bs4 import BeautifulSoup
import os
import re


# 模仿浏览器 获取页面源码
def get_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
    }

    response_page = requests.get(url=url, headers=headers, timeout=10)
    response_page.encoding = "utf-8"

    text = BeautifulSoup(response_page.text, 'lxml')
    return text


# 获取总页数
def get_PageNum():
    # 循环每一页
    for index in range(1, 124):
        url = "http://kaijiang.zhcw.com/zhcw/html/ssq/list_{}.html".format(index)
        text = get_page(url)
        ems = text.find_all("em")
        divs = text.find_all("td", {"align": "center"})

        n = 0
        with open("lottery.txt", "a") as f:
            for em in ems:
                # print(em.get_text())
                message = em.get_text()
                n += 1
                if n == 7:
                    n = 0
                    message = message + "\n"
                else:
                    message += "\t"
                f.write(str(message))

        with open("date.txt", "a") as f:
            for div in divs:
                date = div.get_text().strip("")
                # 这里要把日期提取出来, 正则匹配
                date_num = re.findall("\d{4}-\d{2}-\d{2}", date)
                date_num = str(date_num[::1])  # 复制,步数为1
                date_num = date_num[2:13]
                if len(date_num) == 0:
                    continue
                elif len(date_num) > 1:
                    f.write(str(date_num) + "\n")  # 把日期写进入,然后换行

        num_date = []
        ball_num = []

        fp01 = open("date.txt", "r")
        for line01 in fp01:
            num_date.append(line01.strip("\n"))
        fp01.close()

        fp02 = open("lottery.txt", "r")
        for line02 in fp02:
            ball_num.append(line02.strip("\n"))
        fp02.close()

        fp = open("num.txt", "a")
        for cc in zip(num_date, ball_num):
            # print(cc)
            fp.write(str(cc) + "\n")
        fp.close()


if __name__ == '__main__':
    get_PageNum()
