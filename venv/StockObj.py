import sqlite3
import requests
from bs4 import BeautifulSoup
from sqlite3 import Error
from stkday import stkday

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
            # page = requests.get("https://finance.yahoo.com/quote/0700.HK/history?period1=1471968000&period2=1535040000&interval=1d&filter=history&frequency=1d")
            page = requests.get("https://finance.yahoo.com/quote/0700.HK/history?period1=1471968000&period2=1503504000&interval=1d&filter=history&frequency=1d")

            soup = BeautifulSoup(page.content, 'html.parser')
            # print(soup.prettify())
            # print("-----------------list(soup.children)-------------------")
            # print(list(soup.children)[1])
            # print("-----------------[type(item) for item in list(soup.children)]-------------------")
            # print([type(item) for item in list(soup.children)[1]])
            print(soup.find_all('td'))
            print([item.get_text() for item in list(soup.find_all('td'))])
            # for item in list(soup.find_all('td')):

            daylist = [item.get_text() for item in list(soup.find_all('td'))]
            indexes = [index for index in range(len(daylist)) if daylist[index].find("Dividend") != -1]
            print(indexes)
            print([idx for idx in indexes])
            for idx in indexes:
                daylist.pop(idx)
                daylist.pop(idx-1)
            # del daylist[[idx for idx in indexes]
            # daylist.remove("0.88 Dividend")

            for index in range(len(daylist)):
                # print(list(soup.find_all('td').count(item)))
                print(index)
                if(daylist[index].find("*") == -1):

                    print(daylist[index])
                    # if((list(soup.find_all('td'))[index].find('span').get_text().find("Dividend") != -1)):
                    #     index = index - 2

                    if index % 7 == 0:
                        sd1 = stkday()
                        sd1.Date = daylist[index];
                        sd1.Open = daylist[index + 1]
                        sd1.High = daylist[index + 2]
                        sd1.Low = daylist[index + 3]
                        sd1.Close = daylist[index + 4]
                        sd1.AdjClose = daylist[index + 5]
                        sd1.Volumn = daylist[index + 6]
                        print([sd1.Date, sd1.Open, sd1.High, sd1.Low, sd1.Close, sd1.AdjClose, sd1.Volumn])

            # html = list(soup.children)[2]
            # body = list(html.children)[3]
            # print(list(body.children))
            # p = list(body.children)[1]
            # print(p.get_text())
            # p.get_text()


    def main(self):
        # database = "/Users/chenyanyang/tst.db"
        database = "C:\\stks\\tst.db"
        # create a database connection
        conn = self.create_connection(database)
        with conn:
            # print("1. Query task by priority:")
            # select_task_by_priority(conn, 1)

            stock_1 = (self.stock, 'Jun-07-2036', 300, 302, 87000)
            try:

                self.create_stock(conn, stock_1)
            except sqlite3.IntegrityError:
                print("duplicate data")
            finally:
                print("2. Query all tasks")
                self.select_all_tasks(conn)

                proxies = {
                    'http': 'http://proxy1.edb.gov.hk:8080/',
                }
                self.web_scrap()


abc = StockObj("abc", "0701.HK")

abc.main();