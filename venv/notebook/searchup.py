from StockObj import StockObj


def search_up_days(days,end_day):
        with open('../../hkstk') as f:
            lines = f.read().splitlines()
        hk = 0
        for line in lines:
            abc = StockObj("abc", str(line))
            conn = abc.create_connection("/Users/chenyanyang/tst.db")
            #conn = abc.create_connection("D:\\stks\\tst.db")

            if abc.get_up(conn, days, end_day) is True:
                print(str(abc.stock))
                hk = hk + 1
        print(str(hk) + " hk stocks met requirements")



search_up_days(5,"2019-04-15")
