from StockObj import StockObj


def search_get_ratio(days,end_day):
        with open('../hkstk') as f:
            lines = f.read().splitlines()
        hk = 0
        for line in lines:
            abc = StockObj("abc", str(line))
            # conn = abc.create_connection("/Users/chenyanyang/tst.db")
            conn = abc.create_connection("D:\\stks\\tst.db")

            if abc.get_delta_price(conn, days, end_day) > 0.1 is True:
                print(str(abc.stock) + " up ratio is " + abc.get_delta_price(conn, days, end_day))
                hk = hk + 1
        print(str(hk) + " hk stocks met requirements")

        # with open('./tks/SZtks') as f:
        #     lines = f.read().splitlines()
        # sz = 0
        # for line in lines:
        #     abc = StockObj("abc", str(line)+".SZ")
        #     # conn = abc.create_connection("/Users/chenyanyang/tst.db")
        #     conn = abc.create_connection("D:\\stks\\tst.db")

        #     if abc.get_up(conn, days) is True:
        #         print(str(abc.stock))
        #         sz = sz + 1
        # print(str(sz) + " sz stocks met requirements")

        # with open('./tks/SStks') as f:
        #     lines = f.read().splitlines()
        # ss = 0
        # for line in lines:
        #     abc = StockObj("abc", str(line)+".SS")
        #     # conn = abc.create_connection("/Users/chenyanyang/tst.db")
        #     conn = abc.create_connection("D:\\stks\\tst.db")

        #     if abc.get_up(conn, days) is True:
        #         print(str(abc.stock))
        #         ss = ss + 1
        # print(str(ss) + " ss stocks met requirements")



search_get_ratio(7,"2019-04-03")
