from StockObj import StockObj


def search_rate_in_days(days):
        with open('/home/Aaron/PyStocks/venv/tks/HKtks2') as f:
            lines = f.read().splitlines()
        hk = 0
        rate_array=[]
        for line in lines:
            abc = StockObj("abc", str(line))
            # conn = abc.create_connection("/Users/chenyanyang/tst.db")
            conn = abc.create_connection("/home/Aaron/PyStocks/venv/tst.db")
            rate_array.append([abc.stock, abc.get_diff_rates(conn,days)]);
        print(rate_array, sep=' -> ')

search_rate_in_days(30)
