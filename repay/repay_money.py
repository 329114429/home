from datetime import datetime


# 信用卡还款的详细,然后根据信用卡的还款日期转换使用


class Credit_card():

    # 信用卡总额, 可借用金额, 利率
    def __init__(self, rental, lend_money, rate):
        self.rental = int(rental)
        self.lend_money = int(lend_money)
        self.rate = float(rate)

    # 借钱
    def lend(self, lend_money):
        self.lend_money = lend_money
        return lend_money

    # 还钱
    def repay(self, repay_money):
        self.repay_money = repay_money

        total_repay_money = self.repay_money + self.lend_money * self.rate

        return total_repay_money

    # 还款日期
    def repay_date(self, str_date):
        year, mon, day = str_date.split("-")
        self.repaydate = datetime(int(year), int(mon), int(day))
        return self.repaydate

    # 借款日期
    def lend_date(self, lend_date):
        self.lend_date = lend_date
        return lend_date
