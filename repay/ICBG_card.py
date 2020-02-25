from repay.credit_card import Card


def IGBG_main():
    IGBG = Card(54000, 2500, 0.005)
    day, timeStamp = IGBG.lend_day("2020-2-12")
    print(day, timeStamp)


if __name__ == '__main__':
    IGBG_main()
