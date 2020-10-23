from StockObj import StockObj
from datetime import *

count = 0
with open('./tks/USAtks') as f:
    lines = f.read().splitlines()

for line in lines:
    count += 1;
    if count >= 12848:
        abc = StockObj("abc", str(line) + "")
        # conn = abc.create_connection("/Users/chenyanyang/tst.db")
        conn = abc.create_connection("/home/Aaron/PyStocks/tst.db")
        abc.update((datetime.today() - timedelta(days=3)).strftime("%Y-%m-%d"), datetime.today().strftime("%Y-%m-%d"))

