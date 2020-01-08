#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from collections import Collection


def pparser():
    # 请求的地址,彩票url
    basic_url = "http://kaijiang.zhcw.com/zhcw/html/ssq/list_1.html"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",

    }
    response = requests.get(basic_url, headers, timeout=10)
    # response.encoding("utf-8")

    # 请求后的彩票地址转成HTML格式
    html_ball = response.text

    # 解析内容
    soup = BeautifulSoup(html_ball, "html.parser")

    page = int(soup.find('p', attrs={'class': 'pg'}).find_all()[0].text)

    # print(page)

    url_part = "http://kaijiang.zhcw.com/zhcw/html/ssq/list"

    # 获得每一分页的信息
    for i in range(1, page + 1):
        url = url_part + "_" + str(i) + ".html"

        response = requests.get(url, headers=headers, timeout=10)

        context = response.text

        soups = BeautifulSoup(context, 'html.parser')

        if soups.table is None:
            continue
        elif soups.table:
            # 获取table的日期
            table_rows = soups.table.find_all("tr")

        else:
            continue


def save_to_file(content):
    # 存入文件
    pass


def predict():
    # 预言
    pass

if __name__ == '__main__':
    # pparser()
    pass
