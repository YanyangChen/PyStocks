from StockObj import StockObj


def search_up_days(days):
        with open('/home/Aaron/PyStocks/venv/tks/HKtks2') as f:
            lines = f.read().splitlines()
        hk = 0
        for line in lines:
            abc = StockObj("abc", str(line))
            # conn = abc.create_connection("/Users/chenyanyang/tst.db")
            conn = abc.create_connection("/home/Aaron/PyStocks/tst.db")

            if abc.get_up(conn, days) is True:
                print(str(abc.stock))
                hk = hk + 1
        print(str(hk) + " hk stocks met requirements")

#        with open('./tks/SZtks') as f:
#            lines = f.read().splitlines()
#        sz = 0
#        for line in lines:
#            abc = StockObj("abc", str(line)+".SZ")
#            # conn = abc.create_connection("/Users/chenyanyang/tst.db")
#            conn = abc.create_connection("/home/Aaron/PyStocks/venv/tst.db")

#            if abc.get_up(conn, days) is True:
#                print(str(abc.stock))
#                sz = sz + 1
#        print(str(sz) + " sz stocks met requirements")

#        with open('./tks/SStks') as f:
#            lines = f.read().splitlines()
#        ss = 0
#        for line in lines:
#            abc = StockObj("abc", str(line)+".SS")
#            # conn = abc.create_connection("/Users/chenyanyang/tst.db")
#            conn = abc.create_connection("/home/Aaron/PyStocks/venv/tst.db")
#
#            if abc.get_up(conn, days) is True:
#                print(str(abc.stock))
#                ss = ss + 1
#        print(str(ss) + " ss stocks met requirements")
#
#
#def search_up_days4USA(days):
#
#    with open('./tks/USAtks') as f:
#        lines = f.read().splitlines()
#        usa = 0
#    for line in lines:
#        abc = StockObj("abc", str(line))
#        # conn = abc.create_connection("/Users/chenyanyang/tst.db")
#        conn = abc.create_connection("/home/Aaron/PyStocks/venv/tst.db")
#
#        if abc.get_upusa(conn, days) is True:
#            print(str(abc.stock))
#            usa = usa + 1
#    print(str(usa) + " usa stocks met requirements")
#
#
#search_up_days4USA(13)
search_up_days(1)
