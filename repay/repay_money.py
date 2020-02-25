from datetime import datetime
import time


# 信用卡还款的详细,然后根据信用卡的还款日期转换使用


class Credit_card():

    # 信用卡总额, 可借用金额, 利率
    def __init__(self, rental, lend_money, rate):
        self.rental = int(rental)
        self.lend_money = int(lend_money)
        self.rate = float(rate)

    # 借钱
    def lend(self, lend_money):
        self.lend_money = int(lend_money)
        return self.lend_money

    # 还钱
    def repay(self, repay_money):
        self.repay_money = int(repay_money)
        total_repay_money = self.repay_money + self.lend_money * self.rate
        return total_repay_money

    # 还款日期
    def repay_date(self, repay_str_date):
        year, mon, day = repay_str_date.split("-")
        self.repaydate = datetime(int(year), int(mon), int(day))

        # 转为时间戳
        timeArray = time.strptime(repay_str_date, "%Y-%m-%d")
        timeStamp = int(time.mktime(timeArray))

        return self.repaydate, timeStamp

    # 借款日期
    def lend_date(self, lend_str_date):
        year, mon, day = lend_str_date.split("-")
        self.lenddate = datetime(int(year), int(mon), int(day))
        return self.lenddate
