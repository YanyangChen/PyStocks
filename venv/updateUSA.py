from StockObj import StockObj
from datetime import *
# with open('./tks/HKtks') as f:
#     lines = f.read().splitlines()
#
# for line in lines:
#     abc = StockObj("abc", str(line))
#     # conn = abc.create_connection("/Users/chenyanyang/tst.db")
#     conn = abc.create_connection("D:\\stks\\tst.db")
#     abc.update()
#
#
# with open('./tks/SZtks') as f:
#     lines = f.read().splitlines()
#
# for line in lines:
#     abc = StockObj("abc", str(line) + ".SZ")
#     # conn = abc.create_connection("/Users/chenyanyang/tst.db")
#     conn = abc.create_connection("D:\\stks\\tst.db")
#     abc.update()
#
# with open('./tks/SStks') as f:
#     lines = f.read().splitlines()
#
# for line in lines:
#     abc = StockObj("abc", str(line) + ".SS")
#     # conn = abc.create_connection("/Users/chenyanyang/tst.db")
#     conn = abc.create_connection("D:\\stks\\tst.db")
#     abc.update()

with open('./tks/USAtks') as f:
    lines = f.read().splitlines()

for line in lines:
    abc = StockObj("abc", str(line) + "")
    # conn = abc.create_connection("/Users/chenyanyang/tst.db")
    conn = abc.create_connection("/home/Aaron/PyStocks/tst.db")
    abc.update((datetime.today() - timedelta(days=90)).strftime("%Y-%m-%d"), datetime.today().strftime("%Y-%m-%d"))

