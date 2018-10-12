from StockObj import StockObj

with open('../hkstk') as f:
    lines = f.read().splitlines()

for line in lines:
    abc = StockObj("abc", str(line))
    # conn = abc.create_connection("/Users/chenyanyang/tst.db")
    conn = abc.create_connection("C:\\stks\\tst.db")

    if abc.get_up(conn, 2) is True:
        print(str(abc.stock))
