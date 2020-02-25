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

    # 借款日期
    def lend_date(self, lend_str_day):
        year, mon, day = lend_str_day.split("-")
        self.lenddate = datetime(int(year), int(mon), int(day))

        # 借钱 转为时间戳
        lend_timeArray = time.strptime(lend_str_day, "%Y-%m-%d")    # 转为时间数组
        repay_timeStamp = int(time.mktime(lend_timeArray))   # 转为时间戳

        return self.lenddate, repay_timeStamp

    # 还款日期
    def repay_date(self, repay_str_day):
        year, mon, day = repay_str_day.split("-")
        self.repaydate = datetime(int(year), int(mon), int(day))

        # 转为时间戳
        repay_timeArray = time.strptime(repay_str_day, "%Y-%m-%d")
        repay_timeStamp = int(time.mktime(repay_timeArray))

        return self.repaydate, repay_timeStamp
