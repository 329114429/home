from repay.credit_card import Card


def IGBG_run():
    IGBG = Card(54000, 25000, 0.005)

    # 借钱日期
    lend_day, lend_timeStamp = IGBG.lend_day("2020-2-12")
    print(lend_day, lend_timeStamp)

    # 还钱日期
    repay_day, repay_timeStamp = IGBG.repay_day("2020-2-14")
    print(repay_day, repay_timeStamp)

    days, days_money = IGBG.day_rate()
    print("相差天数:{}, 需要还钱:{}".format(days, days_money))


if __name__ == '__main__':
    IGBG_run()
