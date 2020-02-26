from repay.repay_money import Credit_card
from datetime import datetime


# 进行信用卡分析


class Card():

    # 构造信用卡
    def __init__(self, rental, lend_money, rate):
        self.card = Credit_card(rental, lend_money, rate)

    # 借钱日期, 借钱时间戳
    def lend_day(self, lend_str_day):
        self.lendday, self.lend_timeStamp = self.card.lend_date(lend_str_day)
        return self.lendday, self.lend_timeStamp

    # 还钱日期, 还钱时间戳
    def repay_day(self, repay_str_day):
        self.repayday, self.repay_timeStamp = self.card.repay_date(repay_str_day)
        return self.repayday, self.repay_timeStamp

    # (还钱日期 - 借钱日期) * 利率
    def day_rate(self):
        repay_day = datetime.utcfromtimestamp(self.repay_timeStamp)
        lend_day = datetime.utcfromtimestamp(self.lend_timeStamp)
        days = (repay_day - lend_day).days
        days_money = self.card.lend_money * days * self.card.rate + self.card.lend_money
        return days, days_money
