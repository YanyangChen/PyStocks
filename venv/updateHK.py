from StockObj import StockObj

with open('/home/Aaron/PyStocks/venv/tks/HKtks') as f:
    lines = f.read().splitlines()

for line in lines:
    abc = StockObj("abc", str(line))
    # conn = abc.create_connection("/Users/chenyanyang/tst.db")
    conn = abc.create_connection("/home/Aaron/PyStocks/tst.db")
    abc.update("2020-03-01","2020-06-30")


