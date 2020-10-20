from StockObj import StockObj
from operator import itemgetter

def search_rate_in_days(days):
        with open('/home/Aaron/PyStocks/venv/tks/HKtks2') as f:
            lines = f.read().splitlines()
        hk = 0
        rate_array=[]
        for line in lines:
            abc = StockObj("abc", str(line))
            # conn = abc.create_connection("/Users/chenyanyang/tst.db")
            conn = abc.create_connection("/home/Aaron/PyStocks/tst.db")
            rate_array.append([abc.stock, abc.get_diff_rates(conn,days)]);
        print(*sorted(rate_array, key=itemgetter(1)), sep='\n')

search_rate_in_days(20)
