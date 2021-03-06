import sqlite3
import requests
import datetime
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

        sql = ''' INSERT INTO stocks(idx,stkdate,open,high,low,close,adjclose,volumn)
                  VALUES(?,?,?,?,?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, stock)
        return cur.lastrowid


    def web_scrap(self):
            # page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
            # page = requests.get("https://finance.yahoo.com/quote/0700.HK/history?period1=1471968000&period2=1535040000&interval=1d&filter=history&frequency=1d")
            # page = requests.get("https://finance.yahoo.com/quote/0700.HK/history?period1=1471968000&period2=1482336000&interval=1d&filter=history&frequency=1d")
            page = requests.get("https://finance.yahoo.com/quote/0700.HK/history?period1=1451232000&period2=1461600000&interval=1d&filter=history&frequency=1d")


            soup = BeautifulSoup(page.content, 'html.parser')
            # print(soup.prettify())
            # print("-----------------list(soup.children)-------------------")
            # print(list(soup.children)[1])
            # print("-----------------[type(item) for item in list(soup.children)]-------------------")
            # print([type(item) for item in list(soup.children)[1]])
            print(soup.find_all('td'))
            print([item.get_text() for item in list(soup.find_all('td'))])
            # for item in list(soup.find_all('td')):
            record_list=[]
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
                        sd1.Date = daylist[index]
                        sd1.Open = daylist[index + 1]
                        sd1.High = daylist[index + 2]
                        sd1.Low = daylist[index + 3]
                        sd1.Close = daylist[index + 4]
                        sd1.AdjClose = daylist[index + 5]
                        sd1.Volumn = daylist[index + 6]
                        print([sd1.Date, sd1.Open, sd1.High, sd1.Low, sd1.Close, sd1.AdjClose, sd1.Volumn])
                        record_list.append(sd1)
            return record_list
            # html = list(soup.children)[2]
            # body = list(html.children)[3]
            # print(list(body.children))
            # p = list(body.children)[1]
            # print(p.get_text())
            # p.get_text()

    def scrab2years_from_2016(self):
        period = [None] * 11
        period[0] = 1451232000
        period[1] = 1451232000 + 3600 * 24 * 122
        period[2] = 1451232000 + 3600 * 24 * 122 * 2
        period[3] = 1451232000 + 3600 * 24 * 122 * 3
        period[4] = 1451232000 + 3600 * 24 * 122 * 4
        period[5] = 1451232000 + 3600 * 24 * 122 * 5
        period[6] = 1451232000 + 3600 * 24 * 122 * 6
        period[7] = 1451232000 + 3600 * 24 * 122 * 7
        period[8] = 1451232000 + 3600 * 24 * 122 * 8
        period[9] = 1451232000 + 3600 * 24 * 122 * 9
        period[10] = 1451232000 + 3600 * 24 * 122 * 10
        twoYDaily_rec = []
        for i in range(1, 10):
            page = requests.get(
                "https://finance.yahoo.com/quote/"+self.stock+"/history?period1="+str(period[i-1] + 3600 * 24)+"&period2="+str(period[i])+"&interval=1d&filter=history&frequency=1d")

            soup = BeautifulSoup(page.content, 'html.parser')
            # print(soup.prettify())
            # print("-----------------list(soup.children)-------------------")
            # print(list(soup.children)[1])
            # print("-----------------[type(item) for item in list(soup.children)]-------------------")
            # print([type(item) for item in list(soup.children)[1]])
            # print(soup.find_all('td'))
            # print([item.get_text() for item in list(soup.find_all('td'))])
            # for item in list(soup.find_all('td')):
            record_list = []


            daylist = [item.get_text() for item in list(soup.find_all('td'))]

            #### ignore null tickets
            if daylist[0].find(".HK") != -1:     # what if other foreign tickets? need to test daylist when dealing with other cases
                break
            #### delete Dividend notes
            indexes = [index for index in range(len(daylist)) if daylist[index].find("Dividend") != -1]
            print(indexes)
            print([idx for idx in indexes])
            print(len(daylist))
            for idx in reversed(indexes): # Interesting! normal query may cause the index bigger than size
                print(idx)
                print("length in loop" + str(len(daylist)))
                daylist.pop(idx)
                daylist.pop(idx - 1)
                print(str(idx) + "poped")
            #### delete Stock Split notes
            split_indexes = [index for index in range(len(daylist)) if daylist[index].find("Stock Split") != -1]
            print(split_indexes)
            print([idx for idx in split_indexes])
            for idx in reversed(split_indexes):
                daylist.pop(idx)
                daylist.pop(idx - 1)
            # del daylist[[idx for idx in indexes]
            # daylist.remove("0.88 Dividend")

            for index in range(len(daylist)):
                # print(list(soup.find_all('td').count(item)))
                print(index)
                if (daylist[index].find("*") == -1):

                    print(daylist[index])
                    # if((list(soup.find_all('td'))[index].find('span').get_text().find("Dividend") != -1)):
                    #     index = index - 2

                    if index % 7 == 0:
                        sd1 = stkday()
                        sd1.Date = datetime.datetime.strptime(daylist[index], '%b %d, %Y').strftime('%Y-%m-%d')
                        sd1.Open = daylist[index + 1]
                        sd1.High = daylist[index + 2]
                        sd1.Low = daylist[index + 3]
                        sd1.Close = daylist[index + 4]
                        sd1.AdjClose = daylist[index + 5]
                        sd1.Volumn = daylist[index + 6]
                        print([sd1.Date, sd1.Open, sd1.High, sd1.Low, sd1.Close, sd1.AdjClose, sd1.Volumn])
                        record_list.append(sd1)
            # return record_list
            twoYDaily_rec = twoYDaily_rec + record_list
            print(len(twoYDaily_rec))
            # twoYDaily_rec.append(record_list)
        return twoYDaily_rec

    def update2today(self):

        # flags should be able to update
        flag_day_sec = 1538323200   # 2018-10-01
        flag_day = "2018-10-01"
        # flag_day_Date = datetime.datetime.strptime(flag_day, '%Y-%m-%d').strftime('%Y-%m-%d')
        dif = (datetime.datetime.now() - datetime.datetime.strptime(flag_day, '%Y-%m-%d')).days
        page = requests.get(
            "https://finance.yahoo.com/quote/" + self.stock + "/history?period1=" + str(flag_day_sec + 3600 * 24) + "&period2=" + str(flag_day_sec + 3600 * 24 * dif) + "&interval=1d&filter=history&frequency=1d")

        soup = BeautifulSoup(page.content, 'html.parser')
        # print(soup.prettify())
        # print("-----------------list(soup.children)-------------------")
        # print(list(soup.children)[1])
        # print("-----------------[type(item) for item in list(soup.children)]-------------------")
        # print([type(item) for item in list(soup.children)[1]])
        # print(soup.find_all('td'))
        # print([item.get_text() for item in list(soup.find_all('td'))])
        # for item in list(soup.find_all('td')):
        record_list = []
        updated_Daily_rec = []
        daylist = [item.get_text() for item in list(soup.find_all('td'))]

        #### ignore null tickets
        if daylist[0].find(".HK") != -1:  # what if other foreign tickets? need to test daylist when dealing with other cases
            return []
        #### delete Dividend notes
        indexes = [index for index in range(len(daylist)) if daylist[index].find("Dividend") != -1]
        print(indexes)
        print([idx for idx in indexes])
        print(len(daylist))
        for idx in reversed(indexes):  # Interesting! normal query may cause the index bigger than size
            print(idx)
            print("length in loop" + str(len(daylist)))
            daylist.pop(idx)
            daylist.pop(idx - 1)
            print(str(idx) + "poped")
        #### delete Stock Split notes
        split_indexes = [index for index in range(len(daylist)) if daylist[index].find("Stock Split") != -1]
        print(split_indexes)
        print([idx for idx in split_indexes])
        for idx in split_indexes:
            daylist.pop(idx)
            daylist.pop(idx - 1)
        # del daylist[[idx for idx in indexes]
        # daylist.remove("0.88 Dividend")

        for index in range(len(daylist)):
            # print(list(soup.find_all('td').count(item)))
            print(index)
            if (daylist[index].find("*") == -1):

                print(daylist[index])
                # if((list(soup.find_all('td'))[index].find('span').get_text().find("Dividend") != -1)):
                #     index = index - 2

                if index % 7 == 0:
                    sd1 = stkday()
                    sd1.Date = datetime.datetime.strptime(daylist[index], '%b %d, %Y').strftime('%Y-%m-%d')
                    sd1.Open = daylist[index + 1]
                    sd1.High = daylist[index + 2]
                    sd1.Low = daylist[index + 3]
                    sd1.Close = daylist[index + 4]
                    sd1.AdjClose = daylist[index + 5]
                    sd1.Volumn = daylist[index + 6]
                    print([sd1.Date, sd1.Open, sd1.High, sd1.Low, sd1.Close, sd1.AdjClose, sd1.Volumn])
                    record_list.append(sd1)
        return record_list

    def main(self):
        # database = "/Users/chenyanyang/tst.db"
        database = "C:\\stks\\tst.db"
        # create a database connection
        conn = self.create_connection(database)
        with conn:
            # print("1. Query task by priority:")
            # select_task_by_priority(conn, 1)
            # stk_r_list = self.web_scrap()
            stk_r_list = self.scrab2years_from_2016()
            stk_r_list = list(set(stk_r_list))
            print(len(stk_r_list))


            for stk in stk_r_list:
                try:
                    stock_1 = (self.stock, stk.Date, stk.Open, stk.High, stk.Low, stk.Close, stk.AdjClose, stk.Volumn)
                    self.create_stock(conn, stock_1)
                except sqlite3.IntegrityError:
                    print("duplicate data")
                finally:
                    print("2. Query all tasks")
                    # self.select_all_tasks(conn)

                    proxies = {
                        'http': 'http://proxy1.edb.gov.hk:8080/',
                    }
                # self.web_scrap()

# with open('./hkstks') as f:
#     lines = f.read().splitlines()
# print(lines)
#
# # there may be some stocks left before index 534
# #856
# for line in lines[1893:]:
#     print(str(line))
#     abc = StockObj("abc", str(line))
#     abc.main()
# abc = StockObj("abc", "1125.HK")
# abc.main()
# abc.main();

# List website:
# http://www.eoddata.com/stocklist/NYSE/A.htm?e=NYSE&l=A
#
# List download:
# http://investexcel.net/all-yahoo-finance-stock-tickers/


# thread running functions? https://www.tutorialspoint.com/python/python_multithreading.htm
# what if there're some new tickets on the market?
# stock symbols update?                 s*\)[^)]*\(                  https://regex101.com/
# plotting data
# relationships
# retrieve and presented processed data?

#1 step 1 product: pure world market data
#2 step 2 product: selecting of stocks: "up for 3 days"