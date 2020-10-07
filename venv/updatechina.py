from StockObj import StockObj

with open('./tks/HKtks') as f:
    lines = f.read().splitlines()

for line in lines:
    abc = StockObj("abc", str(line))
    # conn = abc.create_connection("/Users/chenyanyang/tst.db")
    conn = abc.create_connection("D:\\stks\\tst.db")
    abc.update()


with open('./tks/SZtks') as f:
    lines = f.read().splitlines()

for line in lines:
    abc = StockObj("abc", str(line) + ".SZ")
    # conn = abc.create_connection("/Users/chenyanyang/tst.db")
    conn = abc.create_connection("D:\\stks\\tst.db")
    abc.update()

with open('./tks/SStks') as f:
    lines = f.read().splitlines()

for line in lines:
    abc = StockObj("abc", str(line) + ".SS")
    # conn = abc.create_connection("/Users/chenyanyang/tst.db")
    conn = abc.create_connection("D:\\stks\\tst.db")
    abc.update()
