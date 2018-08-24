import sqlite3
import requests
from bs4 import BeautifulSoup
from sqlite3 import Error


# http://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/
class StockObj:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

    def create_connection(self, db_file):
        """ create a database connection to the SQLite database
            specified by the db_file
        :param db_file: database file
        :return: Connection object or None
        """
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)

        return None


    def select_all_tasks(self, conn):
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        cur = conn.cursor()
        cur.execute("SELECT * FROM STOCKS")

        rows = cur.fetchall()

        for row in rows:
            print(row)


    def select_task_by_priority(self, conn, priority):
        """
        Query tasks by priority
        :param conn: the Connection object
        :param priority:
        :return:
        """
        cur = conn.cursor()
        cur.execute("SELECT * FROM STOCKS")

        rows = cur.fetchall()

        for row in rows:
            print(row)


    def create_stock(self, conn, stock):
        """
        Create a new task
        :param conn:
        :param task:
        :return:
        """

        sql = ''' INSERT INTO stocks(idx,stkdate,open,close,volumn)
                  VALUES(?,?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, stock)
        return cur.lastrowid


    def web_scrap(self):
            # page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
            page = requests.get("https://finance.yahoo.com/quote/0700.HK/history?period1=1471968000&period2=1535040000&interval=1d&filter=history&frequency=1d")



            soup = BeautifulSoup(page.content, 'html.parser')
            print(soup.prettify())
            # print(list(soup.children))
            # print([type(item) for item in list(soup.children)])
            # html = list(soup.children)[2]
            # body = list(html.children)[3]
            # print(list(body.children))
            # p = list(body.children)[1]
            # print(p.get_text())
            # p.get_text()


    def main(self):
        database = "/Users/chenyanyang/tst.db"

        # create a database connection
        conn = self.create_connection(database)
        with conn:
            # print("1. Query task by priority:")
            # select_task_by_priority(conn, 1)
            stock_1 = (self.stock, 'Jun-02-2036', 300, 301, 87000)
            try:
                self.create_stock(conn, stock_1)
            except sqlite3.IntegrityError:
                print("duplicate data")
            finally:
                print("2. Query all tasks")
                self.select_all_tasks(conn)

                proxies = {
                'http': 'http://adb.def.hk:8080/',
                }

                self.web_scrap()


abc = StockObj("abc", "0701.HK")

abc.main()