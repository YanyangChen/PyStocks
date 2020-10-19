from StockObj import StockObj
from datetime import * 

with open('/home/Aaron/PyStocks/venv/tks/HKtks2') as f:
    lines = f.read().splitlines()

for line in lines:
    abc = StockObj("abc", str(line))
    # conn = abc.create_connection("/Users/chenyanyang/tst.db")
    conn = abc.create_connection("/home/Aaron/PyStocks/tst.db")
    abc.update((datetime.today() - timedelta(days=3)).strftime("%Y-%m-%d"), datetime.today().strftime("%Y-%m-%d"))


