from StockObj import StockObj

#with open('/Users/chenyanyang/Documents/PyStockscyy0/venv/tks/HKtks_') as f:
with open('/Users/chenyanyang/Documents/PyStockscyy0/venv/notebook/HKtks') as f:

    lines = f.read().splitlines()

for line in lines:
    abc = StockObj("abc", str(line))
    conn = abc.create_connection("/Users/chenyanyang/tst.db")
    #conn = abc.create_connection("D:\\stks\\tst.db")
    abc.manual_update("2020-07-07", "2020-10-06")
