from StockObj import StockObj

with open('../hkstk') as f:
    lines = f.read().splitlines()

for line in lines:
    abc = StockObj("abc", str(line))
    conn = abc.create_connection("/Users/chenyanyang/tst.db")
    if abc.get_5_up(conn) is True:
        print(str(abc.stock))