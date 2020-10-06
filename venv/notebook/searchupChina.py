from StockObj import StockObj


def search_up_days(days,end_day):
        with open('../tks/SZtks') as f:
            lines = f.read().splitlines()
        sz = 0
        for line in lines:
            abc = StockObj("abc", str(line)+".SZ")
            conn = abc.create_connection("/Users/chenyanyang/tst.db")
            #conn = abc.create_connection("D:\\stks\\tst.db")

            if abc.get_up(conn, days, end_day) is True:
                print(str(abc.stock))
                sz = sz + 1
        print(str(sz) + " sz stocks met requirements")

        with open('../tks/SStks') as f:
            lines = f.read().splitlines()
        ss = 0
        for line in lines:
            abc = StockObj("abc", str(line)+".SS")
            conn = abc.create_connection("/Users/chenyanyang/tst.db")
            #conn = abc.create_connection("D:\\stks\\tst.db")

            if abc.get_up(conn, days, end_day) is True:
                print(str(abc.stock))
                ss = ss + 1
        print(str(ss) + " ss stocks met requirements")

search_up_days(6,"2019-04-15")
