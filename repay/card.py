from repay.credit_card import Card


def IGBG_run():
    IGBG = Card(54000, 25000, 0.005)

    # 借钱日期
    try:
        lend_day, lend_timeStamp = IGBG.lend_day("2020-2-11")
        if lend_day:
            print("借钱日期:{}".format(lend_day))
        else:
            print("输入借钱日期:")
    except FileNotFoundError:
        print("借钱日期无法找到")

    # 还钱日期
    try:
        repay_day, repay_timeStamp = IGBG.repay_day("2020-3-12")
        if repay_day:
            print("还钱日期:{}".format(repay_day))
        else:
            print("输入还钱日期:")
    except FileNotFoundError:
        print("还钱日期无法找到")

    days, days_money = IGBG.day_rate()

    print("相差天数:{}, 需要还钱:{}".format(days, days_money))


if __name__ == '__main__':
    IGBG_run()
