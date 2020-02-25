from repay.repay_money import Credit_card


# 进行信用卡分析

def analysis():
    # 广发银行
    ICGB = Credit_card(54000, 25000, 0.0005)

    # 借钱日期
    lend_data = ICGB.lend_date("2020-2-23")
    print("借钱日期:", lend_data)

    # 还钱日期, 还钱时间戳
    repay_date, repay_date_timeStamp = ICGB.repay_date("2020-3-11")
    print("还钱日期:", repay_date)
    print("还钱时间:", repay_date_timeStamp)

    lend_Money = ICGB.lend(8000)
    if lend_Money:
        print(lend_Money)
    else:
        print("No more money")


if __name__ == '__main__':
    analysis()
