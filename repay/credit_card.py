from repay.repay_money import Credit_card


# 进行信用卡分析


class Card():

    # 构造信用卡
    def __init__(self, rental, lend_money, rate):
        self.card = Credit_card(rental, lend_money, rate)

    # 借钱日期, 借钱时间戳
    def lend_day(self, lend_str_day):
        self.lenddate, self.lend_timeStamp = self.card.lend_date(lend_str_day)
        return self.lenddate, self.lend_timeStamp

    # 还钱日期, 还钱时间戳
    def repay_day(self, repay_str_day):
        self.repayday, self.repay_timeStamp = self.card.repay_date(repay_str_day)
        return self.repayday, self.repay_timeStamp

        # # 借钱日期
        # lend_data, lend_data_timeStamp = lend_date("2020-2-23")
        # print("借钱日期:", lend_data)
        # print("借钱时间:", lend_data_timeStamp)
        #
        # # 还钱日期, 还钱时间戳
        # repay_date, repay_date_timeStamp = ICGB.repay_date("2020-3-11")
        # print("还钱日期:", repay_date)
        # print("还钱时间:", repay_date_timeStamp)
        #
        # lend_Money = ICGB.lend(8000)
        # if lend_Money:
        #     print(lend_Money)
        # else:
        #     print("No more money")
        #
        # total_time = repay_date_timeStamp - lend_data_timeStamp
        # print("还钱时间 - 借钱时间:", total_time)


if __name__ == '__main__':
    ICBG = Card(54000, 25000, 0.0005)
