import threading
import time
from StockObj import StockObj


exitFlag = 0


class myThread (threading.Thread):

    def __init__(self, period1, period2):
        threading.Thread.__init__(self)
        # self.threadID = threadID
        # self.name = name
        # self.counter = counter
        self.period1 = period1
        self.period2 = period2

    def run(self):
        print("Starting " + self.name)
        run_this(self.period1, self.period2)
        print("Exiting " + self.name)


def run_this(period1, period2):
  print("threads running")
  with open('./hkstks') as f:
     lines = f.read().splitlines()
  print(lines)

 # there may be some stocks left before index 534
  for line in lines[period1:period2]:
     print("threads running ---------------" + str(line))
     abc = StockObj("abc", str(line))
     abc.main()

print("threads running")
# thread1 = myThread(896, 1159)
# thread2 = myThread(1160, 1423)
# thread3 = myThread(1424, 1687)
# thread4 = myThread(1687, 1949)
thread1 = myThread(1895, 1907)
thread2 = myThread(1908, 1920)
thread3 = myThread(1921, 1934)
thread4 = myThread(1935, 1949)

thread1.start()
thread2.start()
thread3.start()
thread4.start()
