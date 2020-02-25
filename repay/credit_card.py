from repay.repay_money import Credit_card


# 进行信用卡分析

def analysis():
    # 广发银行
    ICGB = Credit_card(54000, 25000, 0.0005)
    lend_Money = ICGB.lend(8000)
    if lend_Money:
        print(lend_Money)
    else:
        print("No more money")


if __name__ == '__main__':
    analysis()
