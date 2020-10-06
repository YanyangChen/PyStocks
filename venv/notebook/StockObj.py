import sqlite3
import requests
import datetime
from bs4 import BeautifulSoup
from sqlite3 import Error
from stkday import stkday

# http://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/


def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)


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

    def check_existence(self, conn):
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM STOCKS where idx ="+"'"+str(self.stock)+"'" )

        num = cur.fetchall()
        # print(num[0][0])
        if num[0][0] >= 1:
            return True
        else:
            return False

    def check_latest(self, conn):
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        cur = conn.cursor()
        cur.execute("SELECT max(stkdate) FROM STOCKS where idx ="+"'"+str(self.stock)+"'" )

        num = cur.fetchall()
        return str(num[0][0])
        # print(num[0][0])
        # if num[0][0] >= 1:
        #     return True
        # else:
        #     return False

    #http://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/
    def check_today_exist(self, conn):
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        cur = conn.cursor()
        # cur.execute("SELECT COUNT(*) FROM STOCKS where idx ="+"'"+str(self.stock)+"'" + "and stkdate ="+"'"+ (datetime.datetime.now() - datetime.timedelta(1)).strftime('%Y-%m-%d') +"'" )
        cur.execute("SELECT COUNT(*) FROM STOCKS where idx ="+"'"+str(self.stock)+"'" + "and stkdate ="+"'"+ (datetime.datetime.now().strftime('%Y-%m-%d')  +"'" ))

        num = cur.fetchall()
        # print(num[0][0])
        if num[0][0] >= 1: # if the stock in today's record existed, it will do nothing
            # print(num[0][0])
            print(str(self.stock) + "updated")
            return True # do nothing
        else:
            if self.check_existence(conn) is True: # the stock exist in the DB
                print(num[0][0])
                print(str(self.stock) + "needs update")
                return False # do download data
            else:
                print("No record")  # the stock does not exist in the DB
                return True     # So the next process won't continue

    def get_5_up(self, conn):
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """

        daysbefore = datetime.datetime.now()-datetime.timedelta(8)
        cur = conn.cursor()
        cur.execute("SELECT close, stkdate FROM STOCKS where idx = "+"'"+self.stock+"'"+"and stkdate between "+"'"+ daysbefore.strftime('%Y-%m-%d') +"'" + "and"+ "'"+ datetime.datetime.now().strftime('%Y-%m-%d') +"'" )

        num = cur.fetchall()

        # for t in num:
        #     for v in t:
        #         print(v)

        indlist=[]

        for t in num:
            # print(t[0])
            indlist.append(t[0])
        # print(indlist)

        for index in reversed(range(len(indlist))):
            if indlist[index] > indlist[index-1]:
                indlist[index] = 1
            else:
                indlist[index] = 0
        # print(indlist)

        if 4-sum(indlist[1:]) == 0:
            # print("True")
            return True
        else:
            # print("False")
            return False

    def get_up(self, conn, f_days, end_day):
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        #flag_day = "2018-10-01"
        #datetime.datetime.strptime(flag_day, '%Y-%m-%d')).days
        # dayset = datetime.datetime.now() - datetime.timedelta(int(3))
        if end_day == "":
            daysbefore = datetime.datetime.now() - datetime.timedelta(int(f_days) + 1) # this int should be updated when 'stock update' function is finished
            end_day = datetime.datetime.now()
        else:
            daysbefore = datetime.datetime.strptime(end_day, '%Y-%m-%d') - datetime.timedelta(int(f_days) + 1)
        # daysbefore = dayset - datetime.timedelta(int(f_days) + 1)  # this int should be updated when 'stock update' function is finished
        cur = conn.cursor()
        cur.execute(
            "SELECT close, stkdate FROM STOCKS where idx = " + "'" + self.stock + "'" + "and stkdate between " + "'" + daysbefore.strftime(
                '%Y-%m-%d') + "'" + "and" + "'" + end_day + "'")

        num = cur.fetchall()

        # for t in num:
        #     for v in t:
        #         print(v)

        indlist = []
        # print(num)
        for t in num:
            # print(t[0])
            indlist.append(float(str(t[0]).replace(",", "").replace("-", "0")))
            # indlist.append(t[0])
        # print(indlist)

        for index in reversed(range(len(indlist))):
            # print("True")
            if float(indlist[index]) > float(indlist[index - 1]):
                indlist[index] = 1
            else:
                indlist[index] = 0


        if int(f_days) - sum(indlist[-int(f_days):]) == 0:
            # print("True")
            print(indlist)
            return True
        else:
            # print("False")
            return False


        # print(num)
        # if num[0][0] >= 1:
        #     return True # do nothing
        # else:
        #     return False # do download data



    def get_down(self, conn, f_days, end_day):
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        #flag_day = "2018-10-01"
        #datetime.datetime.strptime(flag_day, '%Y-%m-%d')).days
        # dayset = datetime.datetime.now() - datetime.timedelta(int(3))
        if end_day == "":
            daysbefore = datetime.datetime.now() - datetime.timedelta(int(f_days) + 1) # this int should be updated when 'stock update' function is finished
            end_day = datetime.datetime.now()
        else:
            daysbefore = datetime.datetime.strptime(end_day, '%Y-%m-%d') - datetime.timedelta(int(f_days) + 1)
        # daysbefore = dayset - datetime.timedelta(int(f_days) + 1)  # this int should be updated when 'stock update' function is finished
        cur = conn.cursor()
        cur.execute(
            "SELECT close, volumn, stkdate FROM STOCKS where idx = " + "'" + self.stock + "'" + "and stkdate between " + "'" + daysbefore.strftime(
                '%Y-%m-%d') + "'" + "and" + "'" + end_day + "'")

        num = cur.fetchall()

        # for t in num:
        #     for v in t:
        #         print(v)

        indlist = []
        vollist = []
        # print(num)
        for t in num:
            # print(t[0])
            indlist.append(float(str(t[0]).replace(",", "").replace("-", "0")))
            vollist.append(float(str(t[1]).replace(",", "").replace("-", "0")))
            # indlist.append(t[0])
        # print(indlist)

        for index in reversed(range(len(indlist))):
            # print("True")
            if (float(indlist[index]) < float(indlist[index - 1])) and (vollist[index] * indlist[index] > 10000000):
                indlist[index] = 1
                vollist[index] = (vollist[index] * indlist[index])
            else:
                indlist[index] = 0


        if int(f_days) - sum(indlist[-int(f_days):]) == 0:
            # print("True")
            print(indlist)
            print(sum(vollist)/1000000)
            return True
        else:
            # print("False")
            return False


    def get_symtik(self, conn, delta_days, end_day):
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        #flag_day = "2018-10-01"
        #datetime.datetime.strptime(flag_day, '%Y-%m-%d')).days
        # dayset = datetime.datetime.now() - datetime.timedelta(int(3))
        if end_day == "":
            daysbefore = datetime.datetime.now() - datetime.timedelta(int(delta_days) + 1) # this int should be updated when 'stock update' function is finished
            end_day = datetime.datetime.now()
        else:
            daysbefore = datetime.datetime.strptime(end_day, '%Y-%m-%d') - datetime.timedelta(int(delta_days))
        # daysbefore = dayset - datetime.timedelta(int(delta_days) + 1)  # this int should be updated when 'stock update' function is finished
        cur = conn.cursor()
        cur.execute(
            "SELECT close, stkdate FROM STOCKS where idx = " + "'" + self.stock + "'" + "and stkdate between " + "'" + daysbefore.strftime(
                '%Y-%m-%d') + "'" + "and" + "'" + end_day + "'")

        num = cur.fetchall()

        # for t in num:
        #     for v in t:
        #         print(v)

        indlist = []
        # print(num)
        for t in num:
            # print(t[0])
			
            indlist.append(float(str(t[0]).replace(",", "").replace("-", "0")))
            # indlist.append(t[0])
        # print(indlist)

        for index in reversed(range(len(indlist))):
            # print("True")
            if float(indlist[index]) > float(indlist[index - 1]):
                indlist[index] = 1
            else:
                indlist[index] = 0


        if int(delta_days-1) - sum(indlist[-(int(delta_days)+1):-1]) == int(delta_days-1) and (len(indlist) != 0):
            # print("True")
			
            if (int(indlist[-1]) == 1) :
                #print(int(delta_days-1))
                #print(indlist[-int(delta_days+1):-1])
                #print(indlist[-1])
                print(indlist)
                return True
            else:
                return False
        else:
            # print("False")
            return False


    def get_delta_price(self, conn, delta_days, end_day):
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        #flag_day = "2018-10-01"
        #datetime.datetime.strptime(flag_day, '%Y-%m-%d')).days
        # dayset = datetime.datetime.now() - datetime.timedelta(int(3))
        if end_day == "":
            daysbefore = datetime.datetime.now() - datetime.timedelta(int(delta_days) + 1) # this int should be updated when 'stock update' function is finished
            end_day = datetime.datetime.now()
        else:
            daysbefore = datetime.datetime.strptime(end_day, '%Y-%m-%d') - datetime.timedelta(int(delta_days)+ 1)
        # daysbefore = dayset - datetime.timedelta(int(delta_days) + 1)  # this int should be updated when 'stock update' function is finished
        cur = conn.cursor()
        cur.execute(
            "SELECT close, stkdate FROM STOCKS where idx = " + "'" + self.stock + "'" + "and stkdate between " + "'" + daysbefore.strftime(
                '%Y-%m-%d') + "'" + "and" + "'" + end_day + "'")

        num = cur.fetchall()

        # for t in num:
        #     for v in t:
        #         print(v)

        indlist = []
        # print(num)
        for t in num:
            # print(t[0])
            # print(float(str(t[0]).replace(",", "").replace("-", "0")))
            indlist.append(float(str(t[0]).replace(",", "").replace("-", "0")))
        # print(len(indlist))
		
        if len(indlist) > (delta_days-1):
            # print((indlist[3]- indlist[0])/indlist[3])
			# delta_p = indlist[2] - indlist[1]
			# ratio = delta_p / delta_days
            return float((indlist[delta_days-1]- indlist[0])/indlist[delta_days-1])
        else:
            return float(0)

##        if int(delta_days-1) - sum(indlist[-(int(delta_days)+1):-1]) == int(delta_days-1) and (len(indlist) != 0):
##            # print("True")
##			
##            if (int(indlist[-1]) == 1) :
##                #print(int(delta_days-1))
##                #print(indlist[-int(delta_days+1):-1])
##                #print(indlist[-1])
##                print(indlist)
##                return True
##            else:
##                return False
##        else:
##            # print("False")
##            return False


    def get_match(self, conn, f_days):
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        # dayset = datetime.datetime.now() - datetime.timedelta(int(3))
        daysbefore = datetime.datetime.now() - datetime.timedelta(int(f_days) + 1) # this int should be updated when 'stock update' function is finished
        # daysbefore = dayset - datetime.timedelta(int(f_days) + 1)  # this int should be updated when 'stock update' function is finished
        cur = conn.cursor()
        cur.execute(
            "SELECT close, stkdate FROM STOCKS where idx = " + "'" + self.stock + "'" + "and stkdate between " + "'" + daysbefore.strftime(
                '%Y-%m-%d') + "'" + "and" + "'" + datetime.datetime.now().strftime('%Y-%m-%d') + "'")

        num = cur.fetchall()

        # for t in num:
        #     for v in t:
        #         print(v)

        indlist = []
        # print(num)
        for t in num:
            # print(t[0])
            indlist.append(float(str(t[0]).replace(",", "").replace("-", "0")))
            # indlist.append(t[0])
        # print(indlist)

        for index in reversed(range(len(indlist))):
            # print("True")
            if float(indlist[index]) < float(indlist[index - 1]):
                indlist[index] = 1
            else:
                indlist[index] = 0

        if int(f_days) - sum(indlist[-int(f_days):]) == 0:
            # print("True")
            print(indlist)
            return True
        else:
            # print("False")
            return False

    #def get_days_average(self, conn, f_days):

    #def get_week_average(self, conn, f_days):

    #def plot_price(self, conn, f_days):

    #def plot_volumn(self, conn, f_days):

    #def plot_averages_and_price(self, conn, f_days):

    def get_upusa(self, conn, f_days):
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        dayset = datetime.datetime.now() - datetime.timedelta(int(5))
        # daysbefore = datetime.datetime.now() - datetime.timedelta(int(f_days) + 1) # this int should be updated when 'stock update' function is finished
        daysbefore = dayset - datetime.timedelta(int(f_days))  # this int should be updated when 'stock update' function is finished
        cur = conn.cursor()
        cur.execute(
            "SELECT close, stkdate FROM STOCKS where idx = " + "'" + self.stock + "'" + "and stkdate between " + "'" + daysbefore.strftime(
                '%Y-%m-%d') + "'" + "and" + "'" + dayset.strftime('%Y-%m-%d') + "'")

        num = cur.fetchall()

        # for t in num:
        #     for v in t:
        #         print(v)

        indlist = []
        # print(num)
        for t in num:
            # print(t[0])
            indlist.append(float(str(t[0]).replace(",", "").replace("-", "0")))
        # print(indlist)

        for index in reversed(range(len(indlist))):
            # print("True")
            if float(indlist[index]) > float(indlist[index - 1]):
                indlist[index] = 1
            else:
                indlist[index] = 0

        weekends = 2 * (divmod(f_days, 7)[0])
        work_days = f_days - weekends
        if f_days - 7 * (divmod(f_days, 7)[0]) == 6:
            work_days = work_days - 1



        if work_days  - sum(indlist) == 0:
            # print("True")
            print(indlist)
            return True
        else:
            # print("False")
            return False


        # print(num)
        # if num[0][0] >= 1:
        #     return True # do nothing
        # else:
        #     return False # do download data




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

        sql = ''' INSERT INTO STOCKS(idx,stkdate,open,high,low,close,adjclose,volumn)
                  VALUES(?,?,?,?,?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, stock)
        return cur.lastrowid


    def web_scrap(self):
            # page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
            # page = requests.get("https://finance.yahoo.com/quote/0700.HK/history?period1=1471968000&period2=1535040000&interval=1d&filter=history&frequency=1d")
            # page = requests.get("https://finance.yahoo.com/quote/0700.HK/history?period1=1471968000&period2=1482336000&interval=1d&filter=history&frequency=1d")
            headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}

            page = requests.get("https://finance.yahoo.com/quote/0700.HK/history?period1=1451232000&period2=1461600000&interval=1d&filter=history&frequency=1d",headers)


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
            headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
            page = requests.get(
                "https://finance.yahoo.com/quote/"+self.stock+"/history?period1="+str(period[i-1] + 3600 * 24)+"&period2="+str(period[i])+"&interval=1d&filter=history&frequency=1d",headers)

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
            try:
                if daylist[0].find(".HK") != -1 or daylist[0].find(".SZ") != -1 or daylist[0].find(".") != -1 or daylist[0].find(".SS") != -1 or daylist[0].find("2") == -1 or hasNumbers(daylist[0]) is False or daylist[0] is None:
                    # what if other foreign tickets? need to test daylist when dealing with other cases
                    return []

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
                            print([daylist[index], daylist[index+1], daylist[index+2], daylist[index+3], daylist[index+4], daylist[index+5], daylist[index+6]])
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
            except IndexError:
                twoYDaily_rec = []

        return twoYDaily_rec

    def update2today(self, late_day, end_day):

        # flags should be able to update
        flag_day_sec = 1262275200   # 2019-01-01
        flag_day = "2010-01-01"
        # late_day = slef.check_latest(conn)
        # flag_day_Date = datetime.datetime.strptime(flag_day, '%Y-%m-%d').strftime('%Y-%m-%d')
        dif = (datetime.datetime.strptime(end_day, '%Y-%m-%d') - datetime.datetime.strptime(flag_day, '%Y-%m-%d')).days #difference between now and flag
        dif_late_flag = (datetime.datetime.strptime(late_day, '%Y-%m-%d') - datetime.datetime.strptime(flag_day, '%Y-%m-%d')).days #difference between start_date and flag
        headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
            
        page = requests.get(
            "https://finance.yahoo.com/quote/" + self.stock + "/history?period1=" + str(flag_day_sec + 3600 * 24 * dif_late_flag) + "&period2=" + str(flag_day_sec + 3600 * 24 * (dif + 1)) + "&interval=1d&filter=history&frequency=1d",headers)

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
        try:
            if daylist[0].find(".HK") != -1 or daylist[0].find(".SZ") != -1 or daylist[0].find(".") != -1 or daylist[0].find(".SS") != -1 or daylist[0].find("2") == -1 or hasNumbers(daylist[0]) is False or daylist[0] is None:
                # what if other foreign tickets? need to test daylist when dealing with other cases
                # what if other foreign tickets? need to test daylist when dealing with other cases
                return []
            #### delete Dividend notes
            # if hasNumbers(daylist[0]) is False:
                # return daylist[0]
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
        except IndexError:
            record_list = []
            return record_list



    def main(self):
        database = "/Users/chenyanyang/tst.db"
        # database = "D:\\stks\\tst.db"
        # create a database connection
        conn = self.create_connection(database)
        with conn:
            # print("1. Query task by priority:")
            # select_task_by_priority(conn, 1)
            # stk_r_list = self.web_scrap()
            test = self.check_existence(conn) #runs the follow only when the stock data does not exist
            if test is False:
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

    def mainO(self):
        database = "/Users/chenyanyang/tst.db"
        #database = "D:\\stks\\otst.db"
        # create a database connection
        conn = self.create_connection(database)
        with conn:
            # print("1. Query task by priority:")
            # select_task_by_priority(conn, 1)
            # stk_r_list = self.web_scrap()
            test = self.check_existence(conn) #runs the follow only when the stock data does not exist
            if test is False:
                stk_r_list = self.scrab2years_from_2016()
                stk_r_list = list(set(stk_r_list))
                print(len(stk_r_list))

                for stk in stk_r_list:
                    try:
                        stock_1 = (self.stock + ".O", stk.Date, stk.Open, stk.High, stk.Low, stk.Close, stk.AdjClose, stk.Volumn)
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

    def update(self):
        database = "/Users/chenyanyang/tst.db"
        #database = "D:\\stks\\tst.db"
        # create a database connection
        conn = self.create_connection(database)
        with conn:
            # print("1. Query task by priority:")
            # select_task_by_priority(conn, 1)
            # stk_r_list = self.web_scrap()
            test = self.check_today_exist(conn)  # runs the follow only when today's stock data does not exist
            if test is False:
                lateest_day = self.check_latest(conn)
                stk_r_list = self.update2today(lateest_day)
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
                        

    def manual_update(self,lateest_day, end_day):
        database = "/Users/chenyanyang/tst.db"
        #database = "D:\\stks\\tst.db"
        # create a database connection
        conn = self.create_connection(database)
        with conn:
            # print("1. Query task by priority:")
            # select_task_by_priority(conn, 1)
            # stk_r_list = self.web_scrap()
            #test = self.check_today_exist(conn)  # runs the follow only when today's stock data does not exist
            #if test is False:
            if 1 == 1:
                #lateest_day = self.check_latest(conn)
                stk_r_list = self.update2today(lateest_day, end_day)
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
# with open('./UStks') as f:
#     lines = f.read().splitlines()
# print(lines)
# #
# # # there may be some stocks left before index 534
# # #856
# for line in lines:
#     # print(str(line))
#     abc = StockObj("abc", str(line))
#     abc.main()



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

############=====================Business==========================================
# *1 batch update daily data on godaddy server
# *2 business model 1 : sell stock market data online
# *3 business model 2 : show data and plots on website
# *4 business model 3 : sell this technology and consultancy to other companies or individuals, price for different types of products
# *5 business model 4 : sell reports or post online, let customers order those reports
# *6 business model 5 : open up a website for general report download, and different web app function for user to input for their generic analysis

############=====================Ideas==========================================
#1 step 1 product: pure world market data "in the name of sharing experimental simulation data, not real market data, with warnings"
#2 step 2 product: selecting of stocks: "up for 3 days" "month average accelerating" "growth rate accelerating"
#15 In a day range, show the growth rate ranking list.
#3 step 3 relation informations
#4 step 4 prediction based on information: exp: "A and B are highly realated, A is known and has been up for 5 days,
# 'what are those Bs and has just been up for 3 days' or 'What are those Bs that's in different time zone'"
#5 step 5 list all that highly related stock pairs
#6 step 6 list all a=f(b,c,d) relation stocks, bonds by machine learning regression and validation.
#7 step 7 list all historical economic issues and find their relation with stock indexes, or bond, real estate or other financial product indexes
#8 step 8 Apply the same idea to different world trade datas or production datas
#9 step 9 Build up input combination functions
#10 simulate pprediction validation
#11 news title scraping
#12 Base on data, find out which company is the industry lead in a certain market(store industry stock lists)
#13 Find out how each type of market and company reacts based on global issues.
#14 In a certain industry, how each of the companies react, like "How HK companies' stock price compete on real estate"

############=====================Todos==========================================
#1 make a function that prints out 5 day stock price going up
#2 make a function that prints out monthly average stock price going up in a year
